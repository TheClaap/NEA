import re, datetime, zoneinfo
def Val(Em, P): #takes the Email and Password as EM and P
    if len(P)<8:
        return "0"
    capital = False
    email=False #sets all of the things i will check to False
    number=False
    for i in P:
        if i.isdigit():
            number=True
        elif i.upper() == i:
            capital = True
    #uses the for loop to iterate through the password and check for 2 variables at the same time
                
    if re.match(".+[@]{1}.+[.]+", Em):
#uses regular expresion to ensure the email is the correct format
        email = True
#returns the value depending if the check values are true or false
    if email == True and capital == True and number ==True:
        return True
    else:
        return False

def clean(month):
    month+=1
    if month==1:
        month = "January"
        return month
    elif month==2:
        month = "February"
        return month
    elif month ==3:
        month = "March"
        return month
    elif month == 4:
        month = "April"
        return month
    elif month == 5:
        month = "May"
        return month
    elif month == 6:
        month = "June"
        return month
    elif month == 7:
        month = "July"
        return month
    elif month == 8:
        month = "August"
        return month
    elif month == 9:
        month = "September"
        return month
    elif month == 10:
        month="October"
        return month
    elif month == 11:
        month = "November"
        return month
    elif month == 12:
        month = "december"
        return month

def BookingCheck(curr_lesson):
        date = datetime.datetime.now()
        print(curr_lesson.date)
        print(curr_lesson.month)
        if curr_lesson.time == "" or curr_lesson.month=="" or curr_lesson.date=="":
            return 2
        else:
            curr_lesson.date = int(curr_lesson.date)
            curr_lesson.month = int(curr_lesson.month)
            if curr_lesson.date==int(date.strftime("%w"))+1 and int(date.strftime("%I"))+1>int(curr_lesson.time[0,1]):
                return 3
            else:
                if curr_lesson.date<int(date.strftime("%w"))+8 and curr_lesson.month+1 == int(date.strftime("%m")):
                    return 3
                else:
                    return 1
