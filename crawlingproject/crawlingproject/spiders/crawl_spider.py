from scrapy import Spider
from scrapy.selector import Selector

from crawlingproject.items import CrawlingprojectItem


class StackSpider(Spider):
    name = "crawlingproject"
    allowed_domains = ["theguardian.com"]
    start_urls = [
        "https://www.theguardian.com/world",
    ]

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="fc-item__header"]/h2')

        for question in questions:
            item = CrawlingprojectItem()
            item['title'] = question.xpath(
                'a[@class="fc-item__link"]/span[@class="u-faux-block-link__cta fc-item__headline"]/span[@class="js-headline-text"]/text()').extract()
            item['url'] = question.xpath(
                'a[@class="fc-item__link"]/@href').extract()
            yield item

