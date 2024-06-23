# input age
# if age < 


age = input("input your age:")
age_int=int(age)
if age_int < 18 :
    print("underage")
elif age_int <= 30 :
    print("can drive")
elif age_int >= 18 and age_int < 80:
    print("Matim")
elif age_int >= 80 :
    print("old age")
    