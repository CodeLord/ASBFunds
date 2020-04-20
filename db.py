from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, String, Integer, Float, ForeignKey
import pymysql

# Connect to DB
Base = declarative_base()

engine = create_engine('mysql+pymysql://nzdatauser:CodeLord2020@localhost:3306/nzdata', pool_recycle=3600)
Session = sessionmaker(bind=engine)
session = Session()


class AsbFundUnitPrice(Base):
    __tablename__ = 'asb_funds_unit_price'

    id = Column(Integer, primary_key=True)
    day = Column(Integer)
    month = Column(Integer)
    year = Column(Integer)
    week = Column(Integer)
    fund_id = Column(Integer, ForeignKey('asb_funds_name.id'))
    fund_price = Column(Float)

    def __repr__(self):
        return "%s Unit price is %s at %s-%s-%s" % (self.fund_id, self.fund_price, self.year, self.month, self.day)


class AsbFundsName(Base):
    __tablename__ = 'asb_funds_name'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "Fund %s is %s" % (self.name, self.id)


Base.metadata.create_all(engine)
