import sqlite3, hashlib

def details(acc):
    con = sqlite3.connect("databases/accounts.db")
    password=Hash(acc.password)
    cur = con.cursor()
    cur.execute(f"INSERT INTO info(email, password, name, hours) VALUES('{acc.email}','{password}','{acc.name}','0')")
    id = cur.execute(f"SELECT Id FROM info WHERE email='{acc.email}'").fetchall()
    con.commit()
    con.close()
    return id

def Hash(password):
    m = hashlib.new("sha256")
    m.update(password.encode("utf8"))
    return m.hexdigest()

def val(email,password):
    con = sqlite3.connect("databases/accounts.db")
    cur=con.cursor()
    try:
        m = cur.execute(f"SELECT password FROM info WHERE email='{email}'").fetchall()
    except:
        return False
    if m[0][0] == Hash(password):
        temp = cur.execute(f"SELECT * FROM info WHERE email='{email}'").fetchall()
        return temp[0][0]
    else:
        return False

def hours(id):
    con=sqlite3.connect("databases/accounts.db")
    cur = con.cursor()
    try:
        h = cur.execute(f"SELECT hours FROM info WHERE Id={id}").fetchall()
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
        con.commit()
        con.close()
    except:
        return "False"


#details("adamcross109@gmail.com" ,"Acscscbt13","adam")
#print(val("adamcross109@gmail.com" ,"Acscscbt13"))
print(Addhrs(10,1))
