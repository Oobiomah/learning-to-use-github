#Password strength checker
def password_strength(password):
    if len(password) < 8:
        return 'Weak'
    elif (len(password) >= 8 and password.isalpha()) or (len(password) >= 8 and password.isdigit()):
        return 'Medium'
    else:
        return 'Strong'
       
   

print(password_strength('<enter argument'))
