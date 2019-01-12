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

soup = BeautifulSoup(ITEM_HTML, 'html.parser')



def find_item_name():
    locator = 'body p'
    title = soup.select_one(locator)    # select_one('p') só retorna uma tag 'p', e select('p') retorna uma lista de tags 'p'
    item = title.attrs['id']
    print(item)

find_item_name()

def find_item_nlink():
    locator = 'body p'
    classe = soup.select_one(locator)
    item = classe.attrs['class']  # ele nos da uma lista de classes, nem sempre essas classes estarão na ordem em que podemos usar a indexação[0]...Para pode usar com segurança
                                  # precisamos criar uma nova lista a partir da lista item.
    lista = [classe for classe in item if classe != 'inner-text']
    print(lista)

find_item_nlink()


def find_price():
    locator = 'body p.price_color'
    price_c = soup.select_one(locator)
    print(float(price_c.string[1:]))
    
find_price()

def find_price_regex():
    locator = 'body p.price_color'
    item_price = soup.select_one(locator).string  # £51.77
    print(item_price)

    pattern = '£([0-9]+\.[0-9]+)'    # Aqui ele cria dois grupos, 1 que tem o £ e outro que tem o numero em sí, o que é matched é apenas o numero, pois deixamos o £ de fora.
    matcher = re.search(pattern, item_price)
    print(matcher.group(0))
    print(float(matcher.group(1)))

find_price_regex()
