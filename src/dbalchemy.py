from sqlalchemy import Column, Integer, String, REAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

Base = declarative_base()


class IPC(Base):
    __tablename__ = 'ipc'

    ano = Column(Integer, primary_key=True)
    ipc = Column(REAL)
    va = Column(REAL)
    rem_min = Column(REAL)
    rem_max = Column(REAL)
    pib_per_cap = Column(REAL)
    rnb_per_cap_an = Column(REAL)
    rdb_per_cap_an = Column(REAL)
    rem_per_cap = Column(REAL)

# Create an engine that stores data in the local directory's
engine = create_engine('sqlite:///sqlalchemy_example.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)

engine = create_engine('sqlite:///sqlalchemy_example.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()