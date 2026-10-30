correct_username = "admin"
correct_password = "1234"
attempts = 0
max_attempts = 4
user_name_check = False
password_check = False

while attempts < max_attempts:
    if not user_name_check:
        username = input("Enter username: ")
        if username == correct_username:
            user_name_check = True
            attempts = 0
            continue
        else:
            if attempts < 3:
                print("Incorrect username. Try again")
                attempts += 1
            else:
                print("Account locked.")
                break
    elif not password_check:
        password = input("Enter password: ")
        if password == correct_password:
           print("Login successful.")
           attempts = 0
           break
        else:
            if attempts < 3:
                print("Incorrect password. Try again.")
                attempts += 1
            else:
                print("Account locked.")
                break