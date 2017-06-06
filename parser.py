from selenium import webdriver
from selenium.webdriver.common.by import By


class MediumParser:
    def __init__(self):
        self._driver = webdriver.PhantomJS()
        self._medium_url = 'https://medium.com'

    def get_top_links_by_tag(self, tag):
        tag_url = "{0}/{1}/{2}".format(self._medium_url, 'tag', tag)
        self._driver.get(tag_url)
        links = self._driver.find_elements(By.PARTIAL_LINK_TEXT, "Read more")
        return [link.get_attribute('href') for link in links]
