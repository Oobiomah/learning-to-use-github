

def username_authentication():
    correct_credentials = "Admin"
    attempt = 0

    print("Enter username")

    while attempt < 4:
        username = input()
        if username == correct_credentials:
            return True
        else:
            print("Incorrect username")
            attempt += 1
            if attempt == 4:
                print("Account locked")


           
def password_authentication():
    correct_credentials = "Admin"
    attempt = 0
    print("Enter password")
    
    while attempt < 4:
        password = input()
        if password == correct_credentials:
            print("Login successful")
            break
        else:
            print("Incorrect password")
            attempt += 1
            if attempt == 4:
                print("Account locked")

username_authentication() and password_authentication()



        