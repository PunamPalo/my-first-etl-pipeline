import psycopg2
import pandas as pd
from sqlalchemy import create_engine

# 1. Connect to your Database

engine = create_engine('postgresql+psycopg2://punampalo:@localhost/my_first_db')
conn = engine


##conn = psycopg2.connect(
  #  host = "localhost",
   # database = "my_first_db",
    #user = "punampalo",
    #password = ""
##)

# 2. Extract - Read rom employees table
df = pd.read_sql("SELECT * from employees", conn)
print("Data from postgress:")
print (df)


# 3. Transfoprm - Clean it in Python
print("\nAverage Salary:", df['salary'].mean())

# 4. Transform - Add a new column
df['salary_after_bonus'] = df['salary'] * 1.10
print("\nWith 10% bonus:")
print(df[['name', 'salary', 'salary_after_bonus']])

# 5.  Load - Save it back to Postgress as a new table
df.to_sql('employees_cleaned', conn, if_exists='replace', index = False)
print("\n Saved as new table 'employees_cleaned")

conn.dispose()