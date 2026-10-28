import pandas as pd # Import pandas library to handle data organization and file export 
from database import engine # Import enigne from database.py file, acts as bridge from databse import engine

# Main function to extract data from database and save it as a csv file
def main() -> None:
    # Use pandas to read 'call_records' table from databse into DateFrame 
    # con=eninge tells pandas which databse connection to use 
    df = pd.read_sql_table("call_records", con=engine)
    # Export DataFrame to physical file named 'All_Call_Records.csv'
    # index=False, keeps data clean, prevents pandas from adding extra column
    df.to_csv("All_Call_Records.csv", index=False)

# Standard python block, ensures main() function run only if code run directly
if __name__ == "__main__":
    main()