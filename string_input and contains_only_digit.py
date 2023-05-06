string = input("enter the string:")
for i in string:
     string_i = i.isnumeric()
     if string_i is False:
         print("There is no digit",string_i)
     elif string_i is True:
         print("There is digit",string_i)
         