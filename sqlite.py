import sqlite3
conn=sqlite3.connect("./database.db")
cursor=conn.cursor()
sql="""
CREATE TABLE IF NOT EXISTS user(
userID INTEGER,
name VARCHAR(60),
family VARCHAR(60),
email VARCHAR(60)
);
"""
cursor.execute(sql)
conn.commit()
conn.close()