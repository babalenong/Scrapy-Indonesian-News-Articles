# run "scrapy crawl merdeka -o merdeka.csv" on terminal
# csv karena lebi nyaman dgn excel things

import scrapy

class MerdekaSpider(scrapy.Spider):
    name = "merdeka"

    # satu satu karena mager implementasi utk di auto in 🙏
    # dan karena fungsi utamanya mendapatkan dataset, 
    # jadi dipilih yang cocok
    start_urls = [
      "https://www.merdeka.com/uang/umkm-sumbang-61-persen-ke-pdb-tapi-nilai-ekspor-umkm-masih-rendah.html",
      "https://www.merdeka.com/uang/bantu-penanganan-corona-aice-group-sebar-apd-untuk-13-rumah-sakit-rujukan.html"
    ]

    def parse(self, response):
        for content in response.css("div.mdk-body-detail"):
            yield {
                'judul': content.css("div.mdk-dt-headline h1::text").get(),
                'berita': content.css("div.mdk-body-paragraph p::text").getall()
            }
