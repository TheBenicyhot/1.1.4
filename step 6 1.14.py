#   a114_divisible.py

# get two numbers from user
number1 = input("please selct one number")
number2 = input("please selct another number")
even = 2,4,6,8,10
odd = 1,3,5,7,9
# loop while the numbers are not divisible (the remainder is 0)
rem = number1/number2
if ( rem == even):
    print("yay its even")
  # inform user of result 
if (rem == odd):
    print("sorry its odd")
  # gather user input again
  
# inform user of result 