# https://www.investopedia.com/terms/s/stock-analysis.asps

from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "test"

    def start_requests(self):
        urls = [
            "https://www.investopedia.com/terms/s/stock-analysis.asps",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = f"stock-analysis.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")