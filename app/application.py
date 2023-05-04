from Pages.search_results_page import Search_result
from Pages.header import Header
from Pages.main_page import MainPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.search_results_page = Search_result(self.driver)
