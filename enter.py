import sqlite3, hashlib

def details(acc):
    con = sqlite3.connect("databases/accounts.db")
    acc.password=Hash(acc.password)
#hashes the password before putting it in the table
    cur = con.cursor()
    cur.execute(f"INSERT INTO info(email, password, name, hours) VALUES('{acc.email}','{acc.password}','{acc.name}','0')")
#fetchs the ID from the account just added to the table
    id = cur.execute(f"SELECT Id FROM info WHERE email='{acc.email}'").fetchall()
    con.commit()
    con.close()
    return id

def Hash(password):
    m = hashlib.new("sha256")
    m.update(password.encode("utf8"))
    return m.hexdigest()
#hashes the password then hex digests it to make it usable in the table

def val(email,password):
    con = sqlite3.connect("databases/accounts.db")
    cur=con.cursor()
    try:
        m = cur.execute(f"SELECT password FROM info WHERE email='{email}'").fetchall()
#using a try and except to find if the details return a valid ID
    except:
        return False
    if m[0][0] == Hash(password):
        temp = cur.execute(f"SELECT * FROM info WHERE email='{email}'").fetchall() 
        return temp[0][0]
#returns the ID from the account
    else:
        return False

def hours(id):
    con=sqlite3.connect("databases/accounts.db")
    cur = con.cursor()
    try:
        h = cur.execute(f"SELECT hours FROM info WHERE Id={id}").fetchall()
#fetches the hours for an account from the table
        con.close()
        return h[0][0]
    except:
        return "False"

def Addhrs(hours,id):
    con = sqlite3.connect("databases/accounts.db")
    cur=con.cursor()
    try:
        h=cur.execute(f"SELECT hours FROM info WHERE ID={id}").fetchall()
        temp = h[0][0] + hours
        cur.execute(f"UPDATE info SET hours={temp} WHERE ID={id}")
#takes the current hours in the table, adds the new hours and updates the table to reflect this change
        con.commit()
        con.close()
    except:
        return "False"
#if a bad ID is entered the function won't go ahead with the addition


#details("adamcross109@gmail.com" ,"Acscscbt13","adam")
#print(val("adamcross109@gmail.com" ,"Acscscbt13"))
print(Addhrs(10,1))
