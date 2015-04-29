from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from poemcrawler.items import PoemItem


class PoetrySpider(CrawlSpider):
    name = "poemhunter"
    allowed_domains = ["poemhunter.com"]
    start_urls = [
        "http://www.poemhunter.com/classics/"
                ]
    rules = (
        Rule(LinkExtractor(
            allow="classics/(.*?)",
            # We never want any 'members' profiles
            deny=["members", "poets"],
            restrict_xpaths="//div[contains(@class, 'pagination')]/ul/li[contains(@class, 'next')]"),
            follow=True),
        Rule(LinkExtractor(            
            deny=["members", "poets"],
            restrict_xpaths="//a[contains(@class, 'name')]"),
            follow=True),
        Rule(LinkExtractor(
            # After first follow, exclude anything that doesn't contain "poems"
            allow="(.*?)/poems",
            deny=["members", "/(.*?)/"],
            restrict_xpaths="//a[contains(@class, 'name')]/poems"),
            follow=True),
        Rule(LinkExtractor(
            allow="/poem/(.*?)",
            deny=["members", "/(.*?)/poems", "/(.*?)/comments"],
            restrict_xpaths=["//a",]),
            callback='parse_item',
            follow=True),
    )

    # These are the exact XPath's to the required text.
    def parse_item(self, response):
        for sel in response.xpath("//html"):
            item = PoemItem()
            item['author'] = sel.xpath("//body/div/div[contains(@id, 'content')]/h2/text()").extract()
            item['title'] = sel.xpath("//body/div/div/div/div/div/div/div/div/a/span[contains(@itemprop, 'title')]/text()").extract()
            item['poem'] = sel.xpath("//div[contains(@class, 'poem-detail')]/div/div[contains(@class, 'KonaBody')]/p/text()").extract()
            item['url']  = response.request.url
            yield item
