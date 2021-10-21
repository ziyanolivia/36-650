import psycopg2
def display():
    conn = psycopg2.connect(host="localhost",
                            database="postgres", 
                            user="postgres", 
                            password="19961201", 
                            port= "5432")
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""SELECT * FROM employees LIMIT 10;""")
    result = cur.fetchall()
    print(result)
    conn.commit()
    conn.close()
display()
