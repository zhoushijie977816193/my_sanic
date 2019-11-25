# !/usr/bin/python
# ! -*- coding: utf-8 -*-
# 2019.11.25


from manage import Base

from sqlalchemy import Column, Integer, String, DECIMAL


class BookBookModels(Base):
    __tablename__ = "book_book"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False, default="")
    status = Column(Integer, nullable=False, default=1)
    author = Column(String(16), nullable=False, default="")
    word_count = Column(Integer, nullable=False, default=0)
    cover = Column(String(255), nullable=False, default="")
    brief = Column(String(255), nullable=False, default="")
    keywords = Column(String(16), nullable=False, default="")
    keywords = Column(String(16), nullable=False, default="")
    complete_status = Column(Integer, nullable=False, default=1)
    score = Column(String(4), nullable=False, default="8.0")
    price = Column(DECIMAL(4, 2), nullable=False, default="8.00")
    isvip = Column(Integer, nullable=False, default=0)
    copyright_info = Column(String(64), nullable=False, default="")
    popularity = Column(Integer, nullable=False, default=0)
    create_time = Column(Integer, nullable=False, default=0)
    update_time = Column(Integer, nullable=False, default=0)
    uuid = Column(String(64), nullable=False, default="")
    source = Column(Integer, nullable=False, default=1)

    def __repr__(self):
        return f"id:{self.id}"

    def to_json(self):
        res = {
            "name": self.name,
            "author": self.author,
            "word_count": self.word_count
            }
        return res
