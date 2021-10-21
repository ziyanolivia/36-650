import psycopg2
def employees_update():
    conn = psycopg2.connect(host="localhost",
                            database="postgres", 
                            user="postgres", 
                            password="19961201", 
                            port= "5432")
    conn.autocommit = True
    cur = conn.cursor()
    sql = """INSERT INTO employees(id,fname,lname)
    SELECT generate_series(1,500), 
    repeat('XY',1+random()::integer), 
    repeat('XY',1+(random()*2)::integer);"""
    cur.execute(sql)
    print("VALUES INSERTED successfully")
    cur.close()
    conn.commit()
    conn.close()
employees_update()
