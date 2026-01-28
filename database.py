import sqlite3

connect=sqlite3.connect("db.sqlite3")
cursor=connect.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    username VARCHAR not NULL UNIQUE,
    password VARCHAR not NULL
)
""")
connect.close()

def add_user(name,username,password):
    connect=sqlite3.connect("db.sqlite3")
    cursor=connect.cursor()
    try:
        cursor.execute("INSERT INTO Users (name, username, password) VALUES (?, ?, ?)",(name,username,password))
        connect.commit()
    except Exception as e:
        print(f"Error: {e}")
    connect.close()

def verify_credentials(username,password):
    connect=sqlite3.connect("db.sqlite3")
    cursor=connect.cursor()
    try:
        result=cursor.execute("select * from Users where username=?",(username,))
        user=result.fetchone()
        if user[3]==password:
            return {"access_granted":True}
        else:
            return {"access_granted":False}
    except Exception as e:
        print(f"Error: {e}")
    connect.close()

def retrieve_user(username):
    connect=sqlite3.connect("db.sqlite3")
    cursor=connect.cursor()
    result=cursor.execute("select * from Users where username=?",(username,))
    user=result.fetchone()
    if user:
        # user = (id, name, username, password)
        return {
            "exists": True,
            "id": user[0],
            "name": user[1],
            "username": user[2]
        }    
    else:
        return{"exists":False}
    




