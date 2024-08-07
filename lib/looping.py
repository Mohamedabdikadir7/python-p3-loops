#!/usr/bin/env python3

def happy_new_year():
   counter = 10
   while counter > 0:
       print(counter)
   counter -= 1
print("Happy New Year!")


   
  

def square_integers(numbers):
  """Squares each integer in the given list.

  Args:
    numbers: A list of integers.

  Returns:
    A new list containing the squares of the input integers.
  """

  squared_numbers = [num**2 for num in numbers]
  return squared_numbers

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
       return "FizzBuzz"
    elif num % 3 == 0:
       return "Fizz"
    elif num % 5 ==0:
       return "Buzz"
    else :
       return num
    
print(fizzbuzz(3))    # Output: Fizz
print(fizzbuzz(5))    # Output: Buzz
print(fizzbuzz(15))   # Output: FizzBuzz
print(fizzbuzz(7))    # Output: 7