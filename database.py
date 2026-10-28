# How to structure of the information for TechFlows
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import DBModelBase

# The container for the data
DATABASE_URL = "sqlite:///techflow_support.db"

# Creates the "communicator" that allows the python code to send instructions to the SQLite database
engine = create_engine(DATABASE_URL)

# Gathers all columns definitions into one place so physically created in database file 
DBModelBase.metadata.create_all(engine)

# Temporary connections to database/ save records generated 
SessionLocal = sessionmaker(bind=engine)
    

