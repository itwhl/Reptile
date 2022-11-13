from sqlalchemy import Column, Integer, String, Numeric

from database import Base


class DoubanMovie(Base):
    __tablename__ = 'tb_douban_movie'

    id = Column('id', Integer, primary_key=True)
    title = Column(String(255))
    rank = Column(Numeric)
    motto = Column(String(255))
    category = Column(String(50))
    country = Column(String(50))
    language = Column('lang', String(50))
    duration = Column(Integer)