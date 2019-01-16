import re
from locators.book_locators import BookLocators


class ParsedItemLocators:
    """
    Locators for an item in the HTML page.

    This allows us to easily see what our code will be looking at as well as
    change it quickly if we notice it is now different.
    """


    # Isto é uma propriedade da classe, e não de um método e nem de uma instancia, não é possivel mudar
    # esse atributo através de um método do objeto ou instnacia dessa classe.
    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }




class BookParser:
    """
    Esta classe representa na verdade os dados contidos na pagina, os métodos para extrair informações da página não
    precisam estar nessa classe. Isso é reponsabilidade de classes em POO.
    """

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Book {self.name}, {self.price}, {self.rating} stars'

    @property
    def name(
            self):  # Ao inves de colocar item_name(self) colocamos name pois o name ja se refere ao item, não tem necessidade de colocar um nome tao especifico.
        locator = BookLocators.NAME_LOCATOR
        item_link = self.parent.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name

    @property
    def link(self):
        locator = BookLocators.LINK_LOCATOR
        item_link = self.parent.select_one(locator).attrs['href']
        return item_link

    @property
    def price(self):
        locator = BookLocators.PRICE_LOCATOR
        item_price = self.parent.select_one(locator).string
        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        return float(matcher.group(1))

    @property
    def rating(self):
        locator = BookLocators.RATING_LOCATOR
        star_rating_tag = self.parent.select_one(locator)
        classes = star_rating_tag.attrs['class']
        rating_classes = [r for r in classes if r != 'star-rating']
        rating_number = BookParser.RATINGS.get(rating_classes[0])  # none if not found ou get(rating_classes[0], default='alguma coisa')
        return rating_number
