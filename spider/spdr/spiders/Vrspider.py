
import scrapy
import urllib
from scrapy.spiders import Spider
from spdr.items import NewsItem


class Meiri(Spider):
    name = "vrspider"
    allowd_domains = ["http://www.vrcun.com", ]
    start_urls = ["http://www.vrcun.com/?page=%s" % nu for nu in xrange(0,4)]

    def parse(self, response):
        items = []
        for site in response.xpath('//ul[@class="hot-news-list"]/li'):
            item = NewsItem()
            picture = site.xpath('a[@*]/img/@src').extract()
            url = site.xpath('a/@href').extract()
            tit = site.xpath(
                'div[@class="hnews-info"]/div[@class="tit"]/a[@*]/text()').extract()
            date = site.xpath(
                'div[@class="hnews-info"]/div[@class="info"]/text()').extract()
            summary = site.xpath(
                'div[@class="hnews-info"]/div[@class="summary"]/span/text()').extract()

            picture_url = "http://www.vrcun.com/" + picture[0]
            picture_path_name = "/home/cdc/cdc/SpiderVR/gitvr/vrworld/static/images/" + picture[0].replace("/", "")
            urllib.urlretrieve(picture_url, picture_path_name)
            item['myurl'] = url[0]
            item['picture'] = picture[0].replace("/", "")
            item['title'] = tit[0]
            item['date'] = date[0]
            item['summary'] = summary[0]

            items.append(item)
        return items
