username = "admin"
password = "secret"
is_active = False

if not username:
    print("Missing username")
elif not password:
    print("MIssing password")
elif not is_active:
    print("Account inactive")
else:
    print("Login successful")