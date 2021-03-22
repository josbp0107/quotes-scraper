import scrapy

# Titulo = //h1/a/text()
# Citas = //span[@class="text" and @itemprop="text"]/text()
# Top ten tags = //div[contains(@class, "tags-box")]/span/a/text()).getall()

    # Es importante siempre crear la clase que hereda de scrapy
    # Estos atributos tienen que ir siempre en los archivos de spiders
class QuotesSpyder(scrapy.Spider):
    name = 'quotes' # nombre unico con el que scrapy se va a referir a este spyder dentro del proyecto
    start_urls = [  
        'http://quotes.toscrape.com/'
    ] # Esta lista contiene todas las URLS que nos vamos a apuntar, dirigir principalmente, la cual vamos a obtener 

    # Este metodo siempre tiene que estar en spyder con el nombre de parse
    # Analiza la respuesta HTTP que nos envia la peticion a esta pagina y a partir
    # de esta respuesta traer toda la inforamcion que queremos
    def parse(self, response):
        # print('*' * 10)
        # print('\n\n')
        # print(response.status, response.headers)
        # print('*' * 10)
        # print('\n\n')

        title = response.xpath('//h1/a/text()').get()
        #print(f'Title: {title}')
        #print('\n\n')

        quotes = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
        #print('Quotes')
        #for quote in quotes:
            #print(f'- {quote}')
        #print('\n\n')

        top_ten_tags = response.xpath('//div[contains(@class, "tags-box")]/span/a/text()').getall()
        #print('Top ten tags')
        #for tag in top_ten_tags:
            #print(f'- {tag}')
        #print('\n\n')

        yield{ # Return parcial de datos. En este caso devuelve un diccionario
            'title': title,
            'quotes': quotes,
            'top_ten_tags': top_ten_tags
        }
        # Para guardar en un archivo los datos scrapeado es con el siguiente comando:
        # scrapy crawl quote quote.extension (la extension puede  ser JSON CSV XML ETC)  