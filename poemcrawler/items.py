# PoemItem model

import scrapy


class PoemItem(scrapy.Item):
    # we'll need the url field to make sure there are no duplicates
    author = scrapy.Field()
    title = scrapy.Field()
    poem = scrapy.Field()
    url = scrapy.Field()
