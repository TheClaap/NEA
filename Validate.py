import re
def Val(Em, P):
    if len(P)<8:
        return "0"
    capital = False
    email=False
    number=False
    for i in P:
        if i.isdigit():
            number=True
        elif i.upper() == i:
            capital = True
                
    
    if re.match(".+[@]{1}.+[.]+", Em):
        email = True
    
    if email == True and capital == True and number ==True:
        return True
    else:
        return False

