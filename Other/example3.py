number="123q456d789"
first_three=number[0:3]
last_three=number[-3:]
#emtsa = 5 
middle_three=int(number[len(number)//2])
middle_str=number[middle_three-1:middle_three +2]
print(first_three)
print(last_three)
print(middle_three)
print(middle_str)
print(first_three , middle_str , last_three)