import Validate, enter
from flask import Flask, render_template, request, redirect, jsonify
app = Flask(__name__, template_folder='templates')

class Acc:
    def __init__(self,email,password,name):
        self.email=email
        self.password=password
        self.name=name
#class used to store the values or each account before they are added to the table
@app.route("/")
def index():
    return render_template('Index.html')

@app.route("/Register", methods=["GET","POST"])
def REG():
    global id
    if request.method=="GET":
        num = 1
        return render_template("Reg.html", type=num)
#sends the nunmber 1 with the template to select the first page from the file to display
    else:
        Email = request.form.get("Email")
        Pass1 = request.form.get("P1")
        Pass2 = request.form.get("P2")
        First = request.form.get("Name")
#using request.form.get to retrieve the values in the given id's from the hmtl form
        if Pass1!=Pass2:
            num=2
            return render_template("Reg.html", type=num)
#first check is if the passwords match. If they dont the retry page is shown
        else:
            if Validate.Val(Email,Pass1) == True:
                account = Acc(Email,Pass1,First)
                id = enter.details(account)
                return redirect("/Cook")
#Only runs if the passwords and email meet the criteria
#The user is re-routed to /Cook before being sent to the home page
            else:
                num=2
                return render_template("Reg.html", type=num)
#if found to be false the second page is loaded for the user

@app.route("/Login", methods=["GET","POST"])
def LOG():
    global id
    if request.method == "GET":
        num= 1
        return render_template("Login.html", type=num)
#Get requests always load the first type from the template
    else:
        Email = request.form.get("Em")
        Password=request.form.get("Pass")
        account = Acc(Email,Password,0)
        id = enter.val(Email,Password)
#code to send the inputted credentials to be checked. If an id is found it is returned
        if id != False:
            return redirect("/Cook")
        else:
            num=2
            return render_template("Login.html", type=num)
#if credentials don't match the database retry screen is loaded

@app.route("/Cook")
def cook():
    return render_template("SaveCookie.html")
#loads a page which creates a cookie

@app.route("/Home/<int:id>", methods = ["GET","POST"])
#<int: id> creates a dynamic URL which can be altered depending on who is logged in
def Home(id):
#the id is passed into the function so it can be used.
    if request.method == "GET":
        Hrs = enter.hours(id)
#retrieving hours from table
        return render_template("Home.html", hours=Hrs, Id=id)

@app.route("/id", methods = ["GET","POST"])
def Id():
    if request.method == "GET":
        print(id)
        return jsonify(id)
#This URL is only used to Get the ID that is global at the time
    else:
        I = request.form["Id"]
        return jsonify(enter.hours(I))
#takes Id from the given form and returns hours 

@app.route("/BuyHours/<int:id>", methods = ["GET","POST"])
def Purchase(id):
#ID also used in this Page to make it unique for each person
    if request.method == "GET":
        return render_template("Purchase.html", Id=id)
    else:
        id=request.form.get["id"]
        hrs=request.form.get["hrs"]
        enter.Addhrs(hrs,id)
        return "True"
#adds the hours to the account then returns true to know it was a success

@app.route("/Confirm", methods=["GET"])
def conf():
    if request.method == "GET":
        return render_template("conf.html")

if __name__ == "__main__":
    app.run()