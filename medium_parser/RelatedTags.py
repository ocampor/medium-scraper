from selenium import webdriver
from selenium.webdriver.common.by import By


class RelatedTags:
    def __init__(self, tag):
        self._driver = webdriver.PhantomJS()
        self._medium_url = 'https://medium.com'
        self._initialize(tag)

    def __enter__(self):
        return self

    def _initialize(self, tag):
        tag_url = "{0}/{1}/{2}".format(self._medium_url, 'tag', tag)
        self._driver.get(tag_url)
        self._driver.maximize_window()

    @property
    def tags(self):
        identifier = 'ul.tags'
        ul_tags = self._driver.find_element(By.CSS_SELECTOR, identifier)
        tags = ul_tags.find_elements(By.TAG_NAME, 'li')
        return [tag.text for tag in tags]

    def to_json(self):
        return {
            'tags': self.tags
        }

    def __exit__(self, ext_type, ext_value, traceback):
        self._driver.quit()
