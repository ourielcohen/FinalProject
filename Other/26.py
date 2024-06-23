def calc(in_func_arr):
    sum=0
    for i in range(1,len(in_func_arr)):
        sum += in_func_arr[i]
    return sum
arr = [1,2,3,4,5]
result=calc(arr)
print(result)