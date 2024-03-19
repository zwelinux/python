user = 'zwe'
passcode = '1234admin'
username = input("Username : ")
password = input("Password : ")

if username == user and password == passcode:
    print("Hello, " + username)
elif username == user and password != passcode:
    print("Wrong Password")
elif username != user or password != passcode:
    print("Username or Password Error. Try again")
else:
    print("Something went wrong try again")
