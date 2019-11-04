# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import re

from ..items import GethouescsvItem


class RentingSpider(scrapy.Spider):
    name = 'renting'
    # allowed_domains = ['zf.szhome.com/search.html?sor=2']
    start_urls = ['http://zf.szhome.com/Search.html?sor=2&aom=1&kwd=&xzq=0&pq=0&price=0&prif=0&prit=0&barea=0&baf=0&bat=0&hx=0&ord=0&dtyx=0&dtst=0&scat=0&sx=0&schid=0&page=1']
    # start_urls = ['http://zf.szhome.com/Search.html?sor=2']
    state = True

    def start_requests(self):
        start_url = 'http://zf.szhome.com/Search.html?sor=2&aom=1&kwd=&xzq=0&pq=0&price=0&prif=0&prit=0&barea=0&baf=0&bat=0&hx=0&ord=0&dtyx=0&dtst=0&scat=0&sx=0&schid=0&page={}'
        i = 1
        while self.state:
            url = start_url.format(str(i))
            yield scrapy.Request(url, callback=self.parse)
            i += 1

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        res_url = soup.select(r'div.mianbox a.tit')
        if res_url != []:
            for res in res_url:
                url = 'http://zf.szhome.com' + res.get('href')
                yield scrapy.Request(url, callback=self.child_parse)
        else:
            self.state = False

    def child_parse(self, response):
        item = GethouescsvItem()

        item['name'] = re.findall(r'<a href=".*" class="blue-14">(.*)</a>', response.text)[0]
        item['rant'] = ''.join(re.findall(r'<p class="red-fe"><strong class="f45">(\d*)</strong>(.*)</p>',response.text)[0])
        item['root_type'] = re.findall(r'<strong class="left">([^<]*)</strong>', response.text)[0]
        item['area'] = re.findall(r'<strong class="left ml40">(.*)</strong>', response.text)[0]
        item['decoration'] = re.findall(r'<li class="two"><strong class="f16">(.*)</strong></li>', response.text)[0]
        item['elevator'] = re.findall(r'<li class="three"><strong class="f16">(.*)</strong></li>', response.text)[0]
        item['toward'] = re.findall(r'<p class="left w200"><em class="gray-95">.*</em>(.*)</p>', response.text)[0]
        item['url'] = response.url

        yield item


