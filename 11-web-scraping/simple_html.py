from bs4 import BeautifulSoup

# Parsing: é apenas um termo de programação para 'entender algo que tem uma estrutara'.


SIMPLE_HTML = '''
<html>
  <head>
    <meta charset="utf-8">
    <title>Minha página de teste</title>
  </head>
  <body>
  <p class="subtitle">Subtitulo da minha pagina</p>
  <p>Paragrafo2</p>
  <ul>
    <li>Rolf</li>
    <li>Charlie</li>
  </ul>
    <img src="imagens/firefox-icon.png" alt="minha página de teste">
  </body>
</html>
'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')

# print(simple_soup.find('title'))
# print(simple_soup.find('title').string)

def find_title():
    title_tag = simple_soup.find('title')
    print(title_tag.string)


def find_list_items():
    li_tag = simple_soup.find_all('li')
    lista = [item.string for item in li_tag]
    return lista

def find_subtitle():
    p_tag = simple_soup.find('p', {"class":"subtitle"})  # Posso fazer também: find('p', class_="subtitle")
    print(p_tag.string)
find_subtitle()


def find_other_paragraph():
    paragraphs = simple_soup.find_all('p')
    other_paragraph = [p for p in paragraphs if 'subtitle' not in p.attrs.get('class', [])]     # Podemos retornar [] quando não for encontrado
                                                                                                # p.attrs é um dicionario, entao podemos usar p.attrs['class'] no lugar do .get('class'),
                                                                                                # porém o get nao da keyError.
    print(other_paragraph[0].string)

find_other_paragraph()
