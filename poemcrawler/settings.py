# -*- coding: utf-8 -*-

# Scrapy settings for poemcrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'poemcrawler'

SPIDER_MODULES = ['poemcrawler.spiders']
NEWSPIDER_MODULE = 'poemcrawler.spiders'

ITEM_PIPELINES = {
    'poemcrawler.pipelines.DuplicatesPipeline': 300,
    'poemcrawler.pipelines.PoetryAndAlcoholPipeline': 800,
}

DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': 'postgres',
    'password': 'popcorn1',
    'database': 'poetryandalcohol'
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'poemcrawler (+http://www.yourdomain.com)'
