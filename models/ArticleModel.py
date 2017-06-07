from mongoengine import Document, fields


class ArticleModel(Document):
    _id = fields.StringField()
    body = fields.StringField()
    title = fields.StringField()
    tags = fields.ListField()
