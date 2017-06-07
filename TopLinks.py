from selenium import webdriver
from selenium.webdriver.common.by import By


class TopLinks:
    """This class takes a keyword and return top medium articles urls related

    Args:
    tag (str): Keyword of the links you want to get
    """
    def __init__(self, tag):
        self._driver = webdriver.PhantomJS()
        self._medium_url = 'https://medium.com'
        self._initialize(tag)

    def _initialize(self, tag):
        tag_url = "{0}/{1}/{2}".format(self._medium_url, 'tag', tag)
        self._driver.get(tag_url)

    def get_links(self):
        links = self._driver.find_elements(By.PARTIAL_LINK_TEXT, "Read more")
        return [link.get_attribute('href') for link in links]

    def next(self):
        scroll_down = 'window.scrollTo(0, document.body.scrollHeight);'
        self._driver.execute_script(scroll_down)
        return self
