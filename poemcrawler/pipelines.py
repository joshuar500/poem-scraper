# import json
from sqlalchemy.orm import sessionmaker
from models import Poem, db_connect, create_poetry_table
from scrapy.exceptions import DropItem


class PoemcrawlerPipeline(object):
    def process_item(self, item, spider):
        return item


# Compare URLs so there are no duplicates in our json file
class DuplicatesPipeline(object):
    def __init__(self):
        self.urls_seen = set()

    def process_item(self, item, spider):
        if item['url'] in self.urls_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.urls_seen.add(item['url'])
            return item


class PoetryAndAlcoholPipeline(object):
    """PoetryAndAlcohol pipeline for storing scraped items in the database"""
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates poetryandalcohol table.
        """
        engine = db_connect()
        create_poetry_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save poems in the database.

        This method is called for every item pipeline component.

        """
        session = self.Session()
        # author = Author(item['author'])
        poem = Poem(**item)

        try:
            # TODO: IF AUTHOR EXISTS, ADD ONLY POEM
            # session.add(author)
            session.add(poem)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item

# # Output in clean Json format
# class JsonWriterPipeline(object):
#     def __init__(self):
#         self.file = open('items.jl', 'wb')

#     def process_item(self, item, spider):
#         line = json.dumps(dict(item)) + "\n"
#         self.file.write(line)
#         return item
