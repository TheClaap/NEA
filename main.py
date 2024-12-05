import Validate, enter, datetime, pytz
from flask import Flask, render_template, request, redirect, jsonify
app = Flask(__name__, template_folder='templates')

class Acc:
    def __init__(self,email,password,name):
        self.email=email
        self.password=password
        self.name=name

class Lesson:
    def __init__(self,date,month,time,account):
        self.date = date
        self.month=month
        self.time = time
        self.account = account

#class used to store the values or each account before they are added to the table
@app.route("/")
def index():
    return render_template('Index.html')

@app.route("/Register", methods=["GET","POST"])
def REG():
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
                return render_template("Login.html",type=3, ID=id)
#Only runs if the passwords and email meet the criteria
#The user is re-routed to /Cook before being sent to the home page
            else:
                num=2
                return render_template("Reg.html", type=num)
#if found to be false the second page is loaded for the user

@app.route("/Login", methods=["GET","POST"])
def LOG():
    if request.method == "GET":
        num= 1
        return render_template("Login.html", type=num)
#Get requests always load the first type from the template
    else:
        Email = request.form.get("Em")
        Password=request.form.get("Pass")
        id = enter.val(Email,Password)
#code to send the inputted credentials to be checked. If an id is found it is returned
        if id != False:
            return render_template("Login.html", type=3, ID=id)
        else:
            num=2
            return render_template("Login.html", type=num)
#if credentials don't match the database retry screen is loaded

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
        id=request.form["id"]
        hrs=request.form["hrs"]
        enter.Addhrs(hrs,id)
        return "True"
#adds the hours to the account then returns true to know it was a success

@app.route("/Confirm/<int:id>", methods=["GET"])
def conf(id):
    if request.method == "GET":
        return render_template("conf.html", Id = id)
#loads a page that shows a confirmation of the purchase

@app.route("/Book/<int:id>", methods=["GET","POST"])
def book(id):
    if request.method == "GET":
        date = datetime.datetime.now()
        return render_template("Booking.html",type = 1,Id=id,month = int(date.strftime("%m")), date = int(date.strftime("%w")))
    else:
        curr_lesson=Lesson(0,0,"",0)
        curr_lesson.account = int(id)
        curr_lesson.date = int(request.form["date-select"])
        curr_lesson.month = int(request.form["month-select"])
        curr_lesson.time = int(request.form["time-select"])
        date = datetime.datetime.now()
        tz = pytz.timezone('Europe/London')
        date = tz.localise(date)
        print(date.strftime("%I"))
        if curr_lesson.time == "" or curr_lesson.month=="" or curr_lesson.date=="":
            return render_template("Booking.html", type=2,Id=id,month = int(date.strftime("%m")), date= int(date.strftime("%w")))
        else:
            if curr_lesson.date==int(date.strftime("%w")) and int(date.strftime("%I"))>curr_lesson.time:
                return render_template("Booking.html", type=3,Id=id,month = int(date.strftime("%m")), date= int(date.strftime("%w")))
            else:
                if curr_lesson.date<int(date.strftime("%w")):
                    return render_template("Booking.html", type=3,Id=id,month = int(date.strftime("%m")), date= int(date.strftime("%w")))
                else:              
                    enter.AddLesson(curr_lesson)
                    return redirect("/Home/"+str(id))

if __name__ == "__main__":
    app.run()