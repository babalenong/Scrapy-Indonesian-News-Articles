# run "scrapy crawl cnnindonesia -o cnnindonesia.csv" on terminal
# csv karena lebi nyaman dgn excel things

import scrapy

class CNNIndonesiaSpider(scrapy.Spider):
    name = "cnnindonesia"

    # satu satu karena mager implementasi utk di auto in 🙏
    # dan karena fungsi utamanya mendapatkan dataset, 
    # jadi dipilih yang cocok
    start_urls = [
        "https://www.cnnindonesia.com/ekonomi/20200624185815-78-517083/pnm-minta-suntikan-rp15-t-untuk-raih-target-66-juta-nasabah"
    ]

    def parse(self, response):
        yield {
          'judul': response.css('h1.title::text').get(),
          'berita': response.css("div.detail_text p::text").getall(),
        }
