# -*- coding: utf-8 -*-
from scrapy import Spider,FormRequest

class WeiboSpider(Spider):
    name = 'weibo'
    allowed_domains = ['weibo.cn']
    search_urls = 'https://weibo.cn/search/mblog'
    max_page = 100


    def start_requests(self):
        keyword = '000001'
        url = '{url}?keyword={keyword}'.format(url=self.search_urls, keyword=keyword)
        for page in range(self.max_page):
            data = {
                'mp': str(self.max_page),
                'page': str(page)
            }
            yield FormRequest(url, callback=self.parse_index, formdata=data)

    def parse_index(self, response):
        print(response.text)
