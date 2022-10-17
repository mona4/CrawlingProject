from scrapy.item import Item,Field

class CrawlingprojectItem(Item):
    title = Field()
    url= Field()

