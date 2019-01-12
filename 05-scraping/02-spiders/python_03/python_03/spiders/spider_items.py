import scrapy
from python_03.items import ItemProducto

class SpiderItems(scrapy.Spider):
    name = 'spider_items'

    start_urls = [
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Delectronics-intl-ship&field-keywords=macbook&rh=i%3Aelectronics-intl-ship%2Ck%3Amacbook'
    ]

    def parse(self, response):
        lista_macbooks = response.css('ul.s-result-list > li')

        for macbook in lista_macbooks:
            titulo = macbook.css('.s-access-title::text').extract_first()
            precio = macbook.css('.a-offscreen::text').extract_first()
            link = macbook.css('.s-access-detail-page::attr(href)').extract_first()
            titulo_truncado = titulo[:50]
            id_producto = link.split('/')[-1]
            shortLink = 'https://www.amazon.com/dp/'+id_producto

            item_producto = ItemProducto()

            item_producto['titulo'] = titulo_truncado
            item_producto['precio'] = precio
            item_producto['link'] = shortLink

            yield item_producto