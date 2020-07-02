# run "scrapy crawl cnnindonesia -o cnnindonesia.csv" on terminal
# csv karena lebi nyaman dgn excel things

import scrapy

class CNNIndonesiaSpider(scrapy.Spider):
    name = "cnnindonesia"

    # satu satu karena mager implementasi utk di auto in 🙏
    # dan karena fungsi utamanya mendapatkan dataset, 
    # jadi dipilih yang cocok
    start_urls = [
        "https://www.cnnindonesia.com/ekonomi/20200624185815-78-517083/pnm-minta-suntikan-rp15-t-untuk-raih-target-66-juta-nasabah",
        "https://www.cnnindonesia.com/ekonomi/20200701123109-78-519463/bank-bumn-incar-kredit-rp90-t-tripel-dari-celengan-negara",
        "https://www.cnnindonesia.com/ekonomi/20200701082954-78-519345/iuran-bpjs-kesehatan-naik-49-ribu-peserta-turun-kelas",
        "https://www.cnnindonesia.com/ekonomi/20200701092409-78-519366/rupiah-melorot-ke-rp14270-jelang-rilis-inflasi-siang-ini",
        "https://www.cnnindonesia.com/ekonomi/20200701162043-78-519622/rupiah-keok-ke-rp14282-per-dolar-as-pada-rabu-sore",
        "https://www.cnnindonesia.com/ekonomi/20200701152630-78-519592/ramai-nasabah-bank-bukopin-batasi-antrean-150-orang-per-hari",
        "https://www.cnnindonesia.com/ekonomi/20200618080425-78-514582/rerata-harga-pasar-koin-rp1000-sawit-viral-cuma-rp2000",
        "https://www.cnnindonesia.com/ekonomi/20200617200959-78-514495/koin-rp1000-bergambar-kelapa-sawit-dijual-online-rp100-juta",
        "https://www.cnnindonesia.com/ekonomi/20200616184714-78-514009/bri-akan-utang-rp14-t-dengan-bunga-19-persen-dari-bank-asing",
        "https://www.cnnindonesia.com/ekonomi/20200615154010-83-513500/operasi-usus-buntu-yang-dijalani-yogi-lancar-berkat-jkn-kis",
        "https://www.cnnindonesia.com/ekonomi/20200613152751-78-512973/akses-umkm-terbatas-kur-belum-terserap-capai-rp129-t",
        "https://www.cnnindonesia.com/ekonomi/20200611160813-78-512311/pandemi-bikin-masyarakat-makin-melek-keuangan",
        "https://www.cnnindonesia.com/ekonomi/20200612073157-78-512480/bank-artos-ganti-nama-jadi-bank-jago",
        "https://www.cnnindonesia.com/ekonomi/20200611195334-78-512418/bpjs-kesehatan-tanggung-utang-rp65-t-ke-rumah-sakit",
        "https://www.cnnindonesia.com/ekonomi/20200611170057-78-512345/iuran-naik-defisit-bpjs-kesehatan-tinggal-rp185-m-pada-2020",
        "https://www.cnnindonesia.com/ekonomi/20200611172436-78-512353/menko-pmk-sebut-iuran-bpjs-harusnya-di-atas-rp200-ribu",
        "https://www.cnnindonesia.com/ekonomi/20200529205105-78-508122/new-normal-mandiri-pangkas-kantor-cabang-dengan-realokasi",
        "https://www.cnnindonesia.com/ekonomi/20200529145231-78-507958/bi-akan-tambah-bunga-simpanan-pemerintah-di-bank-sentral",
        "https://www.cnnindonesia.com/ekonomi/20200528201605-78-507773/dapat-setoran-modal-rp255-m-bni-syariah-naik-jadi-buku-iii",
        "https://www.cnnindonesia.com/ekonomi/20200528141055-78-507638/bank-korea-selatan-pangkas-bunga-acuan-jadi-05-persen",
        "https://www.cnnindonesia.com/ekonomi/20200528144615-78-507639/sarankan-jual-reksa-dana-sinarmas-dirut-bibit-dicopot",
        "https://www.cnnindonesia.com/ekonomi/20200608164322-78-511126/laba-bank-mandiri-tumbuh-melambat-ke-rp792-t-kuartal-i-2020",
        "https://www.cnnindonesia.com/ekonomi/20200528092007-78-507517/harga-emas-antam-turun-ke-rp908-ribu-per-gram",
        "https://www.cnnindonesia.com/ekonomi/20200527180659-78-507408/tumbuh-satu-digit-laba-bca-rp66-t-pada-kuartal-i-2020",
        "https://www.cnnindonesia.com/ekonomi/20200527071106-78-507179/ojk-bekukan-sementara-7-reksa-dana-sinarmas-asset-management"
    ]

    def parse(self, response):
        yield {
          'judul': response.css('h1.title::text').get(),
          'berita': response.css("div.detail_text::text").getall(),
        }
