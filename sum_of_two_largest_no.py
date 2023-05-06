num_1=int(input("enter the first number:"))
num_2=int(input("enter the second number:"))
num_3=int(input("enter the third number:"))

if num_1>num_3 and num_2>num_3:
    sum_1 = num_1+num_2
    print(sum_1,'is larger')
elif num_2>num_1 and num_3>num_1:
    sum_2 = num_2+num_3
    print(num_2,"is largest") 
elif num_3>num_1 and num_1>num_2:
    sum_3 = num_3+num_1
    print(sum_3,"is largestest")