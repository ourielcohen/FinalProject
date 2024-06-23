str1 = input("input your name:  ")
str2 = input("input your password:  ")
str3 = (str1,str2)
print(str3)
if str3 == ("Sagi","123456"):
        print("Authorized")
elif str3 == ("Moshe","123456"):
        print("Authorized")
elif str3 == ("admin","admin"):
        print("admin","admin")
else:
    print("unauthorized")
   
