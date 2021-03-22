import scrapy

# Titulo = //h1/a/text()
# Citas = //span[@class="text" and @itemprop="text"]/text()
# Top ten tags = //div[contains(@class, "tags-box")]/span/a/text()).getall()
# Next page button = response.xpath('//ul[@class="pager"]/li[@class="next"]/a/@href').get()

    # Es importante siempre crear la clase que hereda de scrapy
    # Estos atributos tienen que ir siempre en los archivos de spiders
class QuotesSpyder(scrapy.Spider):
    name = 'quotes' # nombre unico con el que scrapy se va a referir a este spyder dentro del proyecto
    start_urls = [  
        'http://quotes.toscrape.com/'
    ] # Esta lista contiene todas las URLS que nos vamos a apuntar, dirigir principalmente, la cual vamos a obtener 
    # custom_settings nos ayuda a guardar el archivo en lugar de usar el flag -o en consola
    custom_settings = {
        'FEED_URI': 'quotes.json', # Nombre del archivo
        'FEED_FORMAT': 'json', # Formato del archivo
        'LOG_ENCODING': 'utf-8'
    }

    def parse_only_quotes(self, response, **kwargs):
        if kwargs:
            quotes = kwargs['quotes']
        quotes.extend(response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall())
        
        next_page_button_link = response.xpath('//ul[@class="pager"]/li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback = self.parse_only_quotes, cb_kwargs= {'quotes':quotes})
        else:
            yield {
                'quotes': quotes
            }

    # Este metodo siempre tiene que estar en spyder con el nombre de parse
    # Analiza la respuesta HTTP que nos envia la peticion a esta pagina y a partir
    # de esta respuesta traer toda la inforamcion que queremos
    def parse(self, response):

        title = response.xpath('//h1/a/text()').get()

        quotes = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()

        top_ten_tags = response.xpath('//div[contains(@class, "tags-box")]/span/a/text()').getall()

        yield{ # Return parcial de datos. En este caso devuelve un diccionario
            'title': title,
            'top_ten_tags': top_ten_tags
        }
        # Para guardar en un archivo los datos scrapeado es con el siguiente comando:
        # scrapy crawl quote quote.extension (la extension puede  ser JSON CSV XML ETC)  

        next_page_button_link = response.xpath('//ul[@class="pager"]/li[@class="next"]/a/@href').get()
        # Valida si existen el boton y lo pasea donde guarda el link
        # y vuelve a ejecutar la funcion parse con el callback = self.parse
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback = self.parse_only_quotes, cb_kwargs= {'quotes':quotes})
            # callback -> una funcion que se va a ejecutar luego de hacer la request al link