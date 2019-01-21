from bs4 import BeautifulSoup
import re

ITEM_HTML = '''
<html>
<head>
<title>A simple example page</title>
</head>
<body>
<div>
<p class="inner-text first-item" id="Primeiro ID">
                First paragraph.
            </p>
<p class="inner-text">
                Second paragraph.
            </p>
</div>
<p class="price_color">£51.77</p>
<p class="outer-text first-item" id="second">
<b>
                First outer paragraph.
            </b>
</p>
<p class="outer-text">
<b>
                Second outer paragraph.
            </b>
</p>
</body>
</html>
'''


"""
O que fizemos aqui em relação o modelo do arquivo 'middle_html.py' foi encapsulamento. 
Tornamos o codigo mais generico, nao importando a implementação dos métodos e sim o seu uso.
"""


class ParsedItemLocators:
    """
    Locators for an item in the HTML page.

    This allows us to easily see what our code will be looking at as well as
    change it quickly if we notice it is now different.


    Criando essa classe, não precisamos mais ficar alterando diretamente nos metodos, 
    agora precisamos alterar apenas nos LOCATORS abaixo:
    """
    NAME_LOCATOR = 'body p'
    LINK_LOCATOR = 'body p'
    PRICE_LOCATOR = 'body p.price_color'
    RATING_LOCATOR = 'body p.price_color'
class ParsedItem:
    """
    Esta classe representa na verdade os dados contidos na pagina, os métodos para extrair informações da página não
    precisam estar nessa classe. Isso é reponsabilidade de classes em POO.
    """
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def name(self): # Ao inves de colocar item_name(self) colocamos name pois o name ja se refere ao item, não tem necessidade de colocar um nome tao especifico.
        locator = ParsedItemLocators.NAME_LOCATOR
        title = self.soup.select_one(locator)    # select_one('p') só retorna uma tag 'p', e select('p') retorna uma lista de tags 'p'
        item = title.attrs['id']
        return item
    
    @property
    def nlink(self):
        locator = ParsedItemLocators.LINK_LOCATOR
        classe = self.soup.select_one(locator)
        item = classe.attrs['class']  # ele nos da uma lista de classes, nem sempre essas classes estarão na ordem em que podemos usar a indexação[0]...Para pode usar com segurança
                                  # precisamos criar uma nova lista a partir da lista item.
        lista = [classe for classe in item if classe != 'inner-text']
        return lista
    
    @property
    def price(self):
        locator = ParsedItemLocators.PRICE_LOCATOR
        price_c = self.soup.select_one(locator)
        return float(price_c.string[1:])

    @property
    def regex(self):
        locator = ParsedItemLocators.RATING_LOCATOR
        item_price = self.soup.select_one(locator).string  # £51.77
        pattern = '£([0-9]+\.[0-9]+)'    # Aqui ele cria dois grupos, 1 que tem o £ e outro que tem o numero em sí, o que é matched é apenas o numero, pois deixamos o £ de fora.
        matcher = re.search(pattern, item_price)
        return float(matcher.group(1))


item = ParsedItem(ITEM_HTML)
print(item.name)
