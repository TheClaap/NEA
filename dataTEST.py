import sqlite3
#This file is used for debugging and manupulating database outside of website
 
def SelectAll():
    con = sqlite3.connect("databases/accounts.db")
    cur=con.cursor()
    statement = '''SELECT * FROM info;'''
    cur.execute(statement)
    print(cur.fetchall())
    con.close()

def DeleteAll():
    con=sqlite3.connect("databases/accounts.db")
    cur=con.cursor()
    statement = '''DELETE FROM info WHERE Id=4'''
    cur.execute(statement)
    con.commit()
    con.close()

def CAll():
    con=sqlite3.connect("databases.accounts.db")
    cur=con.cursor()
    cur.execute('''SELECT name FROM sqlite_master WHERE type="table" ''')
    print(cur.fetchall())
    con.close()

def Fetch():
    con = sqlite3.connect('databases/accounts.db')
    cur = con.cursor()
    m = cur.execute("SELECT * FROM info WHERE name='adam'")
    m=m.fetchall()
    print(m)
    con.commit()
    con.close()

SelectAll()
#DeleteAll()
#Fetch()

"""con=sqlite3.connect('databases/accounts.db')
cur = con.cursor()
statement = '''CREATE TABLE info (
    Id INTEGER NOT NULL PRIMARY KEY,
    email varchar(255),
    password varchar(255),
    name text,
    hours integer,
);'''
statement2 = '''INSERT INTO info VALUES('adamgmail','pass','Adam')'''
cur.execute(statement)
con.commit()
con.close()"""

#table has fields email,password,name,hours

