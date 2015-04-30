# PoemItem model
import scrapy
from scrapy.contrib.loader.processor import MapCompose, Join


class PoemItem(scrapy.Item):
    # we'll need the url field to make sure there are no duplicates
    author = scrapy.Field(input_processor=MapCompose(unicode.strip), output_processor=Join(),)
    title = scrapy.Field(input_processor=MapCompose(unicode.strip), output_processor=Join(),)
    poem = scrapy.Field(input_processor=MapCompose(unicode.strip), output_processor=Join(),)
    url = scrapy.Field()
