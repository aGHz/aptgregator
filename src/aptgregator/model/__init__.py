from sqlalchemy import Column, Integer, String, Unicode, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Listing(Base):
    __tablename__ = 'listing'
    id = Column(Integer, primary_key=True)
    external_id = Column(String(50))
    title = Column(Unicode(250))
    url = Column(String(250))
    price = Column(Float(asdecimal=True))
    has_image = Column(Boolean)
    posted_on = Column(DateTime)
    map_url = Column(String(250))

