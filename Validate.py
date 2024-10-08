import re
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

