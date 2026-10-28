#where the information needed to be placed inside the shelves (database), goes
import random
import numpy as np
from faker import Faker
from datetime import datetime 
from sqlalchemy.orm import sessionmaker, Session
from database import SessionLocal
from models import CallRecord

# Generates fake data 
fake = Faker() 

# Create iterative generate 1000+ records

# Wait time calculation - takes hour of the day and the day of the week as inputs 
def work_hours(hour_of_day, day_of_week):
# The work hours - checking if call is during work hours 9-5
    # If the hour of the day is in the range of 9 to 17 then do the following random time
    if hour_of_day in range(9, 17):
        # Random wait time of 10-45 min 
        total_wait = random.randint(10, 45) 
    else: 
        #Random wait time of 2-15 min
        total_wait = random.randint(2, 15)

# Peak day multiplier 
    # If the day is Monday or friday add a random amount of wait time from 2-15 min    
    if day_of_week in ['Monday', 'Friday']: 
        total_wait = total_wait + np.random.randint(5, 16)
    return total_wait

#####################################################################################

# Runs loops to generate at least 1000+ records 
def record_generator(session: Session, count: int ): #'session' is our bridge to the database and 'count' is our goal (1000) 
    
    #count tells python how many times to repeat the loop, and we use faker to fill the variables with new, unique data
    #filling the variables with unique data every time 
    for names in range(count): 

        # Random time this year to simulate historical data
        call_time = fake.date_time_this_year() 
        
        # Generates unique buisness ID required for each customer
        customer_uuid = fake.uuid4()

        # faker creates a name for this record
        customer_name = fake.name()

        # Extract the day from the time we just picked 
        day = call_time.strftime('%A') #turns date into a string

        # Extract the hour so we can see if its work hours 
        hour = call_time.hour #gets the 24 hr integer 14 for 2 pm

        # Randomly picks 1 of the 4 categories management needs to track 
        issue_category = random.choice(['Billing', 'Technical', 'Service', 'Account'])

        # Randomly decides whether the problem was fixed (true or not)
        resolution_status = random.choice([True, False])

        # Calls the work_hours function to calculate wait time based on the day and hour
        #wait time variable is dependent on hour and day variable
        wait = work_hours(hour,day)

        # Here we 'package' all the variables above into our 'CallRecord' bookshelf blueprint
        new_call = CallRecord(
            customer_uuid = customer_uuid, 
            customer_name = customer_name,
            call_timestamp = call_time,
            day_of_week = day,
            hour_of_day = hour, 
            wait_time = wait, 
            issue_category = issue_category,
            resolution_status = resolution_status)
        
        # This 'stages' the finished record in the session so its ready to be saved 
        session.add(new_call)

#####################################################################################
        
# main() function
def main():

    # Sets up the clerk that will manage the data transfer btwn Python and techflow_support.db file 
    session = SessionLocal() 

    try:
        session.query(CallRecord).delete()
        # "starts the engine" of the loop written, passing in the session and the required count of 1000+ records
        record_generator(session, 1000)
        # Finalizes the save, oushes all the records into techflow_support.db
        session.commit()
        print("Success: 1000+ records have been saved!")
    # Blocks triggers if any error occurs while generating or saving records
    except Exception as e:
        # Display specific error in terminal if something wrong
        print(f"An error occurred: {e}")
        # If error happens, undoes all pending changes in current session, prevents partial data from affecting techflow_support.db 
        session.rollback()

    finally:
        # Safely ends the connection
        session.close()
        
# Standard python block, ensures main() function run only if code run directly        
if __name__ == "__main__":
    main()




    
    


