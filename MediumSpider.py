from ArticleInfo import ArticleInfo
from TopLinks import TopLinks
from models import ArticleModel
from multiprocessing import Pool
from controllers import MongoController
from mongoengine import connect


class MediumSpider:
    def __init__(self, seeds):
        self._seeds = seeds
        self.start_requests()

    def start_requests(self):
        for seed in self._seeds:
            self.save_links(seed)

    def save_links(self, seed):
        links = TopLinks(seed).links
        Pool().map(self.save, links)

    def parse(self, link):
        return ArticleInfo(link).to_json()

    def save(self, link):
        article = self.parse(link)
        with MongoController():
            connect(host=MongoController.host, port=int(MongoController.port))
            ArticleModel(**article).save()


if __name__ == '__main__':
    import time
    start_time = time.time()
    MediumSpider(['python', 'machine learning'])
    print("time: {0}".format(time.time() - start_time))
