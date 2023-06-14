import sqlite3

db_conn = sqlite3.connect("task.db")
c = db_conn.cursor()
c.execute("""CREATE TABLE task_user(
            task text,
            date text
            

)""")
db_conn.commit()
db_conn.close()
