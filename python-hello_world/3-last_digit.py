#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a=str(number)

if int(a[-1]) > 5:
   print("Last digit of" , a , "is" , int(a[-1]) , "and is greater than 5")
elif int(a[-1]) < 6 and int(a[-1]) != 0:
     print("Last digit of" , a , "is" , int(a[-1]) , "and is less than 6 and not 0") 
else:
    print("Last digit of" , a , "is" , int(a[-1]) , "and is 0")      
