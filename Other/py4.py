username = input("input your name:  ")
password = input("input your password:  ")
str3 = (str1,str2)
print(str3)
if username == "Sagi":
    if password =="123456":
        print("Authorized")
    else:
        print("Unauthorized")
elif username == "admin":
    if password == "admin":
        print("admin","admin")
    else:
        print("Unauthorized")
   
