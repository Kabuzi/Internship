from selenium.webdriver.common.by import By
from Pages.Base_page import Page


class Search_result(Page):
    ITEM = (By.ID, "ProductCount")

    def find_items(self, items):
        actual_results = self.verify_partial_text(items, *self.ITEM)
        expected_results = '23 results found for “cure”'
        assert actual_results == expected_results, f'Expected {expected_results}, but got {actual_results}'
