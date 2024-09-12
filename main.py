import Validate, enter
from flask import Flask, render_template, request, redirect, jsonify
app = Flask(__name__, template_folder='templates')

class Acc:
    def __init__(self,email,password,name):
        self.email=email
        self.password=password
        self.name=name

@app.route("/")
def index():
    return render_template('Index.html')
@app.route("/Register", methods=["GET","POST"])
def REG():
    global id
    if request.method=="GET":
        return render_template("Reg.html")
    else:
        Email = request.form.get("Email")
        Pass1 = request.form.get("P1")
        Pass2 = request.form.get("P2")
        First = request.form.get("Name")
        if Pass1!=Pass2:
            return redirect("/Register/retry")
        else:
            if Validate.Val(Email,Pass1) == True:
                account = Acc(Email,Pass1,First)
                id = enter.details(account)
                return redirect("/Cook")
            else:
                return redirect("/Register/retry")
@app.route("/Login", methods=["GET","POST"])
def LOG():
    global id
    if request.method == "GET":
        return render_template("Login.html")
    else:
        Email = request.form.get("Em")
        Password=request.form.get("Pass")
        account = Acc(Email,Password,0)
        id = enter.val(Email,Password)
        if id != False:
            return redirect("/Cook")
        else:
            return redirect("Login/retry")

@app.route("/Register/retry")
def Rretry():
    return render_template("RegRetry.html")

@app.route("/Cook")
def cook():
    return render_template("SaveCookie.html")

@app.route("/Login/retry")
def Lretry():
    return render_template("LogRetry.html")

@app.route("/Home", methods = ["GET","POST"])
def Home():
    if request.method == "GET":
        return render_template("Home.html")

@app.route("/id", methods = ["GET","POST"])
def Id():
    if request.method == "GET":
        print(id)
        return jsonify(id)
    else:
        I = request.form["Id"]
        return jsonify(enter.hours(I))

@app.route("/BuyHours", methods = ["GET","POST"])
def Purchase():
    if request.method == "GET":
        return render_template("Purchase.html")
    else:
        id=request.form.get["id"]
        hrs=request.form.get["hrs"]
        enter.Addhrs(hrs,id)
        return "True"

@app.route("/Confirm", methods=["GET"])
def conf():
    if request.method == "GET":
        return render_template("conf.html")

if __name__ == "__main__":
    app.run()