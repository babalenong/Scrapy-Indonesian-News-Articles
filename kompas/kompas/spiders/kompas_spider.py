# run "scrapy crawl kompas -o kompas.csv" on terminal
# csv karena lebi nyaman dgn excel things

import scrapy

class KompasSpider(scrapy.Spider):
    name = "kompas"

    # satu satu karena mager implementasi utk di auto in 🙏
    # dan karena fungsi utamanya mendapatkan dataset, 
    # jadi dipilih yang cocok
    start_urls = [
        "https://money.kompas.com/read/2020/06/29/142550626/tergerus-ponsel-bagaimana-produsen-kamera-digital-bertahan?page=all#page2",
        "https://money.kompas.com/read/2020/06/29/151814026/selama-psbb-penjualan-pertamina-anjlok-hingga-50-persen",
        "https://money.kompas.com/read/2020/06/30/151729226/sepanjang-2019-jumlah-investor-pasar-modal-indonesia-tembus-248-juta",
        "https://money.kompas.com/read/2020/06/30/150255326/netflix-dkk-wajib-laporkan-pungutan-pajak-per-3-bulan?page=all#page2",
        "https://money.kompas.com/read/2020/06/30/140900026/ada-pandemi-covid-19-produksi-batu-bara-diproyeksi-masih-capai-target",
        "https://money.kompas.com/read/2020/06/30/104449626/lippo-karawaci-raup-pendapatan-rp-310-triliun-pada-kuartal-i-2020?page=all#page2",
        "https://money.kompas.com/read/2020/06/30/102741726/produksi-pesawat-menciut-40-persen-airbus-bakal-phk-20000-karyawan?page=all#page2",
        "https://money.kompas.com/read/2020/06/30/090300826/di-tengah-pandemi-amazon-gelontorkan-rp-7-1-triliun-untuk-bonus-karyawan",
        "https://money.kompas.com/read/2020/06/30/084300926/jual-20-persen-sahamnya-perusahaan-kosmetik-kim-kardashian-kini-bernilai-rp-14",
        "https://money.kompas.com/read/2020/06/29/190023026/bfi-finance-bakal-bagi-dividen-rp-180-miliar",
        "https://money.kompas.com/read/2020/06/29/173800826/-alfamart-bikin-coworking-space-di-lingkungan-kampus",
        "https://money.kompas.com/read/2020/06/29/163046026/sri-mulyani-serapan-anggaran-kesehatan-dalam-pen-sudah-468-persen",
        "https://money.kompas.com/read/2020/06/29/161241126/subsidi-listrik-dan-solar-diusulkan-turun-tahun-depan?page=all#page2",
        "https://money.kompas.com/read/2020/06/29/151814026/selama-psbb-penjualan-pertamina-anjlok-hingga-50-persen",
        "https://money.kompas.com/read/2020/06/29/121830926/bank-bumn-pakai-dana-rp-30-triliun-dari-pemerintah-untuk-salurkan-kredit?page=all#page2",
        "https://money.kompas.com/read/2020/06/29/063956526/pria-40-tahun-salip-jack-ma-jadi-orang-terkaya-nomor-2-china-ini-penyebabnya?page=all#page2",
        "https://money.kompas.com/read/2020/06/28/145035426/imbas-virus-corona-nike-rugi-rp-112-triliun",
        "https://money.kompas.com/read/2020/06/28/141217926/arus-modal-asing-masuk-ke-sbn-capai-rp-58-triliun",
        "https://money.kompas.com/read/2020/06/28/125400326/etf-indonesia-tertinggi-di-asean?page=all#page2",
        "https://money.kompas.com/read/2020/06/28/091800926/gara-gara-coca-cola-kekayaan-mark-zuckerberg-lenyap-rp-102-6-triliun?page=all#page2",
        "https://money.kompas.com/read/2020/06/28/083459526/erick-thohir-larang-bumn-ambil-proyek-kecil-yang-jadi-jatah-umkm?page=all#page2",
        "https://money.kompas.com/read/2020/06/28/070800426/ada-pandemi-industri-tambak-udang-dan-es-batangan-di-bangka-tetap-tumbuh",
        "https://money.kompas.com/read/2020/06/27/200000826/kemenkeu-prediksi-pertumbuhan-ekonomi-kuartal-ii-2020-negatif-3-8-persen",
        "https://money.kompas.com/read/2020/06/27/180600926/di-jakarta-baru-0-04-persen-angkutan-umum-gunakan-kendaraan-listrik",
        "https://money.kompas.com/read/2020/06/27/173700726/sri-mulyani-covid-19-timbulkan-efek-domino-yang-luar-biasa"
    ]

    def parse(self, response):
        for content in response.css("div.container.clearfix"):
            yield {
                'judul': content.css("h1.read__title::text").get(),
                'berita': content.css("div.read__content p::text").getall()
            }
