# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def start_requests(self):
        cookies = "EDUWEBDEVICE=b2e2152bd55441f68d08b6de7113f0e2; P_INFO=13023686323|1536934821|1|imooc|00&99|null&null&null#zhj&330200#10#0|&0|null|13023686323; __utma=63145271.1344858778.1536934788.1539591463.1539934175.8; WM_TID=naV%2FzUb9keRERRABURM9bcSOTozlR4ie; mp_MA-A976-948FFA05E931_hubble=%7B%22sessionReferrer%22%3A%20%22https%3A%2F%2Fwww.icourse163.org%2Fhome.htm%3FuserId%3D1143548757%22%2C%22updatedTime%22%3A%201539934179533%2C%22sessionStartTime%22%3A%201539934175204%2C%22sendNumClass%22%3A%20%7B%22allNum%22%3A%207%2C%22errSendNum%22%3A%200%7D%2C%22deviceUdid%22%3A%20%225379350e-7fba-43b5-8754-ef99a1fb8193%22%2C%22persistedTime%22%3A%201536934787981%2C%22LASTEVENT%22%3A%20%7B%22eventId%22%3A%20%22da_screen%22%2C%22time%22%3A%201539934179533%7D%2C%22sessionUuid%22%3A%20%22e7cf9947-6b4e-4e58-ba42-fc7c47bc2694%22%7D; hasVolume=true; videoVolume=0.8; WM_NI=uu%2BUD2dnwFYL1GpvA1zbYcKxkjV6r441T%2BRKhTANKmZO1qhow7IF8gcK6xmxBKBXOo%2BH%2BBjRFnA%2FDNs7HLIHFDGWGSE7NaqmwHKUnsqbkX21FJwIWuwYzlnf1trQzOODTXQ%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed0b24d8ea8e1a4aa3ff8bc8eb7c84e869f8faabc6a8f8686b8c445f3b498b6ae2af0fea7c3b92ab7abe5b6c73aa8b2b9a7dc48f399c097c43bbabe9784ca74a9b69ad7f140f8ef9cccd141ac8c8fafca679a91ff92eb65b5e987a7bb6da195fa99f07482958eb9ce65e998e5a3e95a86b28fd0c746b1e988adcc44869c89b8c65987e98282f467b59885b6ed79b3bea5b9b13b8696b9aad67fb587b68ded6ef3acbeb2f9458d9c9cb9d437e2a3"
        cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split(";")}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies,
        )

    def parse(self, response):
        pass
