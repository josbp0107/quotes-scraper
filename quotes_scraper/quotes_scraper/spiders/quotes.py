import scrapy

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
        print('*' * 10)
        print('\n\n')
        print(response.status, response.headers)
        print('*' * 10)
        print('\n\n')