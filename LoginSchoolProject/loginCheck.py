username = input("Enter your username:")
password = input("Enter your password:")

#check if teacher
if len(username) == 7:
    file = open("loginTeacher.txt", "r")
    info = file.read()
    info = info.split()
    if username in info:
        index = info.index(username) + 1
        user_pass = info[index]
        if user_pass == password:
            print("welcome", username, ",you have teacher permissions!")
        else:
            print("Password is Wrong")
    else:
        print("Username not found")

    

#check if student
elif len(username) == 8:
    file = open("loginStudent.txt", "r")
    info = file.read()
    info = info.split()
    if username in info:
        index = info.index(username) + 1
        user_pass = info[index]
        if user_pass == password:
            print("welcome", username, ",you only have student permissions!")
        else:
            print("Password is Wrong")
    else:
        print("Username not found")

#yeh the users gone crazy
else:
    print("Invalid Credentials")