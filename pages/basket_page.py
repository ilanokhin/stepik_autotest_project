from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS_LIST), "Basket contains products in it"

    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "Text about empty basket is not present"
