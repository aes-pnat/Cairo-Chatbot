from pathlib import Path

import scrapy


class MorningstarSpider(scrapy.Spider):
    name = "morningstar"

    def start_requests(self):
        sitemap_urls = [
            "https://www.morningstar.com/sitemap.xml",
        ]
        for url in sitemap_urls:
            yield scrapy.Request(url=url, callback=self.parse_sitemap)

    def parse_sitemap(self, response):
        for loc in response.xpath("//*[local-name()='loc']/text()").extract():
            yield scrapy.Request(url=loc, callback=self.parse_subsitemap)

    def parse_subsitemap(self, response):
        for loc in response.xpath("//*[local-name()='loc']/text()").extract():
            yield scrapy.Request(url=loc, callback=self.parse)

    def parse(self, response):
        print(response.url)
        # page = response.url.split("/")[-2]
        # filename = f"quotes-{page}.html"
        # Path(filename).write_bytes(response.body)
        # self.log(f"Saved file {filename}")