import psycopg2
def employees():
   conn = psycopg2.connect(host="localhost", port="5432", user="postgres", 
                           password="19961201", database="postgres")
   cur = conn.cursor()
   cur.execute("DROP TABLE IF EXISTS employees")
   sql ='''CREATE TABLE employees(
      id SERIAL,
      fname VARCHAR(10),
      lname VARCHAR(10)
      )'''
   cur.execute(sql)
   print("Table created successfully")
   conn.commit()
   cur.close()
   conn.close()
employees()
