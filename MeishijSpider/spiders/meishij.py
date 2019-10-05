# -*- coding: utf-8 -*-
import scrapy

class MeishijSpider(scrapy.Spider):
    name = 'meishij'
    allowed_domains = ['meishij.net']
    start_urls = ['http://meishij.net/']

    def parse(self, response):
        if 'https://www.meishij.net/zuofa' in response.url:
            name = response.css('#tongji_title::text').get()
            craft = response.css('#tongji_gy::text').get()
            taste = response.css('#tongji_kw::text').get()
            header_img = response.css(
                'body > div.main_w.clearfix > div.main.clearfix > div.cp_header.clearfix > div.cp_headerimg_w > img::attr(src)').get()
            main_material = response.css(
                'body > div.main_w.clearfix > div.main.clearfix > div.cp_body.clearfix > div.cp_body_left > div.materials > div > div.yl.zl.clearfix > ul > li > div > h4 > a::text').getall()
            main_material_amount = response.css(
                'body > div.main_w.clearfix > div.main.clearfix > div.cp_body.clearfix > div.cp_body_left > div.materials > div > div.yl.zl.clearfix > ul > li > div > h4 > span::text').getall()
            main_materials = {}
            for a, i in zip(main_material, main_material_amount):
                main_materials[a] = i
            auxiliary_matrials = {}
            auxiliary_matrial = response.css(
                'body > div.main_w.clearfix > div.main.clearfix > div.cp_body.clearfix > div.cp_body_left > div.materials > div > div.yl.fuliao.clearfix > ul > li > h4 > a::text').getall()
            auxiliary_matrial_amount = response.css(
                'body > div.main_w.clearfix > div.main.clearfix > div.cp_body.clearfix > div.cp_body_left > div.materials > div > div.yl.fuliao.clearfix > ul > li > span::text').getall()
            for a, i in zip(auxiliary_matrial, auxiliary_matrial_amount):
                auxiliary_matrials[a] = i

            measures = {}
            measure = response.css(
                'body > div.main_w.clearfix > div.main.clearfix > div.cp_body.clearfix > div.cp_body_left > div.measure > div.editnew.edit > div > div > p::text').getall()
            imgs = response.css(
                'body > div.main_w.clearfix > div.main.clearfix > div.cp_body.clearfix > div.cp_body_left > div.measure > div.editnew.edit > div > div > p:nth-child(2) > img::attr(src)').getall()
            for a, i in zip(measure, imgs):
                measures[a] = i
            yield {'name': name, 'craft': craft, 'taste': taste, 'header_img': header_img,
                   'main_materials': main_materials, 'auxiliary_matrials': auxiliary_matrials, 'measures': measures}
        for url in response.css('a::attr(href)').extract():
            if 'list.php' in url:
                continue
            yield response.follow(url)
