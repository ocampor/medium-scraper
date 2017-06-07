from selenium import webdriver
from selenium.webdriver.common.by import By


class ArticleInfo:
    def __init__(self, url):
        self._driver = webdriver.PhantomJS()
        self._url = url
        self._initialize()

    def _initialize(self):
        self._driver.get(self._url)

    @property
    def id(self):
        identifier = 'postArticle-content'
        body = self._driver.find_element(By.CLASS_NAME, identifier)
        return body.get_attribute('data-post-id')

    @property
    def title(self):
        return self._driver.title

    @property
    def body(self):
        identifier = 'postArticle-content'
        body = self._driver.find_element(By.CLASS_NAME, identifier)
        return body.text

    @property
    def tags(self):
        identifier = 'ul.tags'
        ul_tags = self._driver.find_element(By.CSS_SELECTOR, identifier)
        tags = ul_tags.find_elements(By.TAG_NAME, 'li')
        return [tag.text for tag in tags]

    def to_json(self):
        return {
            '_id': self.id,
            'title': self.title,
            'body': self.body,
            'tags': self.tags
        }
