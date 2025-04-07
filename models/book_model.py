from datetime import datetime

from sqlalchemy import Integer, String, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from resources import db


class BookModel(db.Model):

    #
    # id = db.Column(db.Integer, primary_key=True)
    # title = db.Column(db.String(100), nullable=False)
    # author = db.Column(db.String(100), nullable=False)
    # description = db.Column(db.String(500), nullable=False)
    # price = db.Column(db.Float, nullable=False)
    # quantity = db.Column(db.Integer, nullable=False)
    #
    # def __init__(self, title, author, description, price, quantity):
    #     self.title = title
    #     self.author = author
    #     self.description = description
    #     self.price = price
    #     self.quantity
    __tablename__ = 'books'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    author: Mapped[str] = mapped_column(String(255), nullable=False)
    publish_time: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author,
            'publish_time': self.publish_time.isoformat()
        }