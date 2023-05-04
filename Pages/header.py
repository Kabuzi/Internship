from selenium.webdriver.common.by import By
from Pages.Base_page import Page


class Header(Page):
    CURE_SKIN_SEARCH_FIELD = (By.ID, "Search-In-Modal")
    SEARCH = (By.CSS_SELECTOR, "search-modal.header__search")
    SEARCH_FIELD = (By.ID, "predictive-search-option-search-keywords")
    EXIT_BTN = (By.CSS_SELECTOR, ".popup-close")


    def click_popup(self):
        self.wait_for_element_click(*self.EXIT_BTN)

    def input_search_text(self, product):
        self.input_text(product, *self.CURE_SKIN_SEARCH_FIELD)

    def click_search(self):
        self.click(self.SEARCH)

    def click_search_field(self):
        self.wait_for_element_click(*self.SEARCH_FIELD)



