#Write a program to loop through a list of numbers and add +2 to every value to elements in list
a=[1,2,3,4 ,5]
for i in a:
	print(i+2)

#Write a program to get the below pattern
#54321
#4321
#321
#21
#1
n=int(input("enter the num of pattern:"))
for i in range (n,0,-1):
	for a in range (1,i+1):
		print(a,end="")
	print()


#Python Program to Print the Fibonacci sequence
n = int(input("Enter the value of 'n': "))
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci Series: ")
while(count <= n):
  print(sum)
  count += 1
  a = b
  b = sum
  sum = a + b

#Explain Armstrong number and write a code with a function
num = int(input("Enter a number: "))  
sum = 0  
temp = num  
while temp > 0:  
   digit = temp % 10  
   sum += digit ** 3  
   temp //= 10  
if num == sum:  
   print(num,"is an Armstrong number")  
else:  
   print(num,"is not an Armstrong number") 

#Write a program to print the multiplication table of 9
num = 9
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)

#Check if a program is negative or positive
num = float(input("Enter a number: "))
if num >= 0:
   if num == 0:
       print("Zero")
   else:
       print("Positive number")
else:
   print("Negative number")

#Write a program to convert the number of days to ages
from datetime import date 
def calculateAge(birthDate): 
    days_in_year = 365.2425    
    age = int((date.today() - birthDate).days / days_in_year) 
    return age
print(calculateAge(date(2000, 11, 19)), "years") 

#Solve Trigonometry problem using math function write a program to solve using math function
import math 
a = math.pi/2
print ("The value of sine of pi/6 is : ") 
print (math.sin(a)) 
print ("The value of cosine of pi/6 is : ") 
print (math.cos(a)) 

#Create a calculator only on a code level by using if condition (Basic arithmetic calculation)
def add(num1, num2): 
    return num1 + num2 
def subtract(num1, num2): 
    return num1 - num2 
def multiply(num1, num2): 
    return num1 * num2 
def divide(num1, num2): 
    return num1 / num2 
print("Please select operation -\n" 
        "1. Add\n" 
        "2. Subtract\n" 
        "3. Multiply\n" 
        "4. Divide\n") 
select = int(input("Select operations form 1, 2, 3, 4 :")) 
number_1 = int(input("Enter first number: ")) 
number_2 = int(input("Enter second number: ")) 
if select == 1: 
    print(number_1, "+", number_2, "=", 
                    add(number_1, number_2)) 
elif select == 2: 
    print(number_1, "-", number_2, "=", 
                    subtract(number_1,number_2))
elif select == 3: 
    print(number_1, "*", number_2, "=", multiply(number_1,number_2))
elif select == 4: 
    print(number_1, "/", number_2, "=", 
                    divide(number_1, number_2)) 
else: 
    print("Invalid input") 




OUTPUT:

icrosoft Windows [Version 10.0.18363.1198]
(c) 2019 Microsoft Corporation. All rights reserved.

C:\Users\SAYUZ\Desktop\Python-Internship>C:/Users/SAYUZ/Anaconda3/Scripts/activate.bat

(base) C:\Users\SAYUZ\Desktop\Python-Internship>python ./Day6.py
3
4
5
6
7
enter the num of pattern:5
12345
1234
123
12
1
Enter the value of 'n': 8
Fibonacci Series: 
0
1
1
2
3
5
8
13
Enter a number: 7
7 is not an Armstrong number
9 x 1 = 9
9 x 2 = 18
9 x 3 = 27
9 x 4 = 36
9 x 5 = 45

(base) C:\Users\SAYUZ\Desktop\Python-Internship>python ./Day6.py
3
4
5
6
7
enter the num of pattern:7
1234567
123456 
12345  
1234   
123    
12
1
Enter the value of 'n': 7
Fibonacci Series: 
0
1
1
2
3
5
8
Enter a number: 9
9 is not an Armstrong number
9 x 1 = 9
9 x 2 = 18
9 x 3 = 27
9 x 4 = 36
9 x 5 = 45
9 x 6 = 54
9 x 7 = 63
9 x 8 = 72
9 x 9 = 81
9 x 10 = 90
Enter a number: 8
Positive number
20 years
The value of sine of pi/6 is : 
1.0
The value of cosine of pi/6 is :
6.123233995736766e-17
Please select operation -
1. Add
2. Subtract
3. Multiply
4. Divide

Select operations form 1, 2, 3, 4 :1
Enter first number: 8
Enter second number: 7
8 + 7 = 15

(base) C:\Users\SAYUZ\Desktop\Python-Internship>    
