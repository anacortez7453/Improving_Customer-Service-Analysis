# This is the blueprint area so focus on defining the tables (UUID, Name, Waitimes...)
# Thus create columns for information the company neeeds to track (Customer UUID and name, call timestamp, day of the week, hour of the day, wait time, issue category resolution status)
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

# Define it to build foundation so possibole to read the DBModelBase below
DBModelBase = declarative_base()

# Create class where code column 
class CallRecord(DBModelBase):
    # Name for table in SQL
    __tablename__ = 'call_records' 
    # Primary Key: every database table needs a unique ID set as the primary_key=true so sql can track records
    id = Column(Integer, primary_key=True) 
    # Unique identifier for each customer 
    customer_uuid = Column(String) 
    # Full name of customer
    customer_name = Column(String)
    # Exact date and time call was received 
    call_timestamp = Column(DateTime)
    # Day of the week
    day_of_week = Column(String)
    # Hour of the day
    hour_of_day = Column(Integer)
    # How long customer waited in minutes
    wait_time = Column(Integer)
    # Type of issue reporting 
    issue_category = Column(String)
    # Indicating true or false whether issue was solved or not
    resolution_status = Column(Boolean)