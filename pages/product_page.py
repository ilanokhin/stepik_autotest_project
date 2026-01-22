from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_add_product_do_basket_button()
        self.should_be_product_name()
        self.should_be_product_price()

    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_add_product_do_basket_button(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button link is not presented"

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"

    def product_added_message_should_contain_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_added_message = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_MESSAGE).text
        assert product_name == product_added_message, "Product added message does not contain product name"

    def basket_cost_message_should_contain_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_cost_message = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_COST_MESSAGE).text
        assert product_price == basket_cost_message, "Basket cost message does not contain product price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message does not disappear"
