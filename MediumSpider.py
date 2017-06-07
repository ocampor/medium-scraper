from ArticleInfo import ArticleInfo
from TopLinks import TopLinks
from multiprocessing import Pool


class MediumSpider:
    def __init__(self, seeds):
        self._seeds = seeds
        self.start_requests()

    def start_requests(self):
        for seed in self._seeds:
            print(self.parse_links(seed))

    def parse_links(self, seed):
        links = TopLinks(seed).links
        return Pool().map(self.parse, links)

    def parse(self, link):
        return ArticleInfo(link).to_json()
