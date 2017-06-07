from pymongo import MongoClient
from dotenv import Dotenv
import os

dotenv_path = os.path.join(os.path.dirname("__file__"), '.env')
dotenv = Dotenv(dotenv_path)
os.environ.update(dotenv)


class MongoController:
    host = os.environ.get("MONGO_SERVER")
    port = os.environ.get("MONGO_PORT")

    def __enter__(self):
        self.client = MongoClient(
            host=self.host,
            port=int(self.port),
            connect=False
        )
        return self.client

    def __exit__(self, type, value, traceback):
        self.client.close()
