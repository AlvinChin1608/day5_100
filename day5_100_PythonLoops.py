#Simple introduction

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit)
  print(fruit + " Pie")
  print(fruits)

# Exercise Challenge
"""
Writea program that calculates the highest score from a list of scores. 

eg. student_scores = [78, 65, 89]

important you are not allowed to use the max or min functions. The output words must match the example

The highest score in the class is: x
"""

#Input a list of student score
student_scores = input("Please input the list with spaces ").split()

for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
#write your code here

highest = student_scores[0]

for num in student_scores:
  if num > highest:
    highest = num # we keep checking the highest variable and then update the highest
print("The highest score in the class: ", highest)

"""
Range
for number in range (a, b):
  print(number)
"""

for number in range(1,10):
  print(number)

#let's say we want the step size to 3
for number in range(1,10,3):
  print(number) #1,4,7

"""
Interesting thought process
https://letstalkscience.ca/educational-resources/backgrounders/gauss-summation#:~:text=Gauss%20used%20this%20same%20method,arrive%20at%20his%20answer%3A%205050.
"""
sum = 0
for number in range(1,101):
  sum += number
  print(sum)

# Exercise challege - adding even numbers

"""
Write a program calculates the sum of all the even numbers from 1 to X. if X is 100 then the first even nhmber would be 2 and the last one is 100 

important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

also, we will constrain the inputs to take only number from 0 to a max of 1000
"""

user_input = int(input("Please insert a number "))
sum_number = 0 

if user_input > 0 and user_input < 1001:
  for n in range(2, int(user_input+1),2): #here we add the range and the 3rd is the step which is 2
    sum_number += n
else:
  print("Invalid, please insert number 1 - 1000")
print(sum_number)

#Method 2 
target = int(input()) #number 0 and 1000
even_sum = 0
for number in range (2, target + 1): #adding 1 because computer start from 0
  if number % 2 ==0:
    even_sum += number
print(even_sum)

# Exercise Challenge FizzBuzz
"""
You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:

* Your program should print each number from 1 to 100 in turn and include number 100.
* When the number is divisible by 3 then instead of printing the number it should print "Fizz".
* When the number is divisible by 5, then instead of printing the number it should print "Buzz"
* And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

"""

for n in range (1,101):
  if n % 3 ==0 and n % 5 == 0:
    print("FizzBuzz")
  elif n % 3 == 0:
    print("Fizz")
  elif n % 5 == 0:
    print("Buzz")
  else:
    print(n)

"""
What I have learnt:
The if condition for checking if a number is divisible by both 3 and 5 (FizzBuzz) should come before the conditions for checking divisibility by 3 or 5. Otherwise, numbers that are divisible by both 3 and 5 will be caught by the first condition (n % 3 == 0)
"""

