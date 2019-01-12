import scrapy
nombre_archivo = 'book_titles.txt'

class MiPrimerSpider(scrapy.Spider):
    name = 'intro_spider_01'

    def start_requests(self): #self = this
        urls = [
            'http://books.toscrape.com/catalogue/page-1.html',
            'http://books.toscrape.com/catalogue/page-2.html',
            'http://books.toscrape.com/catalogue/page-3.html',
            'http://books.toscrape.com/catalogue/page-4.html',
            'http://books.toscrape.com/catalogue/page-5.html',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        #guardar nombre css xpath
        # precio css
        # stock xpath


        nombreLibro =response.css('a::attr(title)').extract()
        precioLibro=response.css('article > div > p > product_price::text').extract()
        stockLibro = response.xpath("//div/div/div/div/section/div/ol/li/article/div/p/text()").extract()
        agregar_a_archivo(nombre_archivo, nombreLibro, stockLibro, precioLibro)



def agregar_a_archivo(path, *lineas_a_escribir):
    try:
        archivo_abierto = open(path, "a")  # por defecto es la r -> read
        for linea in lineas_a_escribir:
            archivo_abierto.write("\n"+linea)

        archivo_abierto.close()
    except Exception:
        print("")