import requests

from pages.quotes_page import QuotesPage


"""
Aqui iniciamos o programa
1- Fazemos o request da pagina
2- Criamos um objeto QuotesPage com a pagina, a classe QuotesPage recebe uma pagina de requests e cria um BS4
"""
page_content = requests.get('http://quotes.toscrape.com').content
page = QuotesPage(page_content)


for quote in page.quotes: # page.quotes retorna uma lista de objtos QuoteParser() que tem métodos para
                          # extrair as informações de uma quote tag especifica.
    print(quote)
