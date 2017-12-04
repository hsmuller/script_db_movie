# -*- coding: utf-8 -*-
import scrapy


class SpiderMovieSpider(scrapy.Spider):
    name = 'spider_movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=20']

    def parse(self, response):
        movie = response.xpath('//*[@id="content"]/div/div[1]/div/div[4]/div/a')
        for each_movie in movies:
        	item = MovieItem()
        	item['name'] = each_movie.xpath('./p').extract()[0]
        	yield item
