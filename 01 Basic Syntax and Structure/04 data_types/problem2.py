# problem 02 : Write a Python program to calculate the length of a string.

# step 1 : fetting input from user 
user_input = input (" Enter the string ")
# step 2 : calculate the lenth of the string 
lenth_of_string = len(user_input)
#step 3 : print the lenth of the string
print (" \n ---------- the Lenth of sting Dashboard -----------")
print (" the Lenth of sting is :", lenth_of_string)
print ( " the lenth of string is : ", user_input.upper())
print (" the lenth of string is : ", user_input.lower())
#print (" frist and last  3 char of string is :", user_input[0:3] = user_input[-0:3])

if lenth_of_string > 3 :
    print (f" The leth of the string is {user_input [:3]}{user_input[-3:]} and it is greater than 3")
else :
    print (f" The leth of the string is {user_input [:3]}{user_input[-3:]} and it is less than 3")





print (" \n ---------- the Lenth of sting Dashboard -----------")