# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['python123.io']
    start_urls = ['http://python123.io/ws/demo.html']

    def parse(self, response):
        fname = 'D://pycodes/txts/'+response.url.split('/')[-1]
        print(fname)
        with open(fname,'wb')  as f:
            f.write(response.body)
        #slef.log("emm")
        pass
