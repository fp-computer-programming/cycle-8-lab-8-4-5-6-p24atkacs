"""
Create a Python file named lab_8-4.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Write a function count_a(word) that takes in a string word and returns the number of a's in the word. 
The function should count both lowercase (a) and uppercase (A)
_____________________________________________________________________________________

Create a Python file named lab_8-5.py

Write a function factorial(num) that takes in a number num 
and returns the product of all numbers from 1 up to and including num

_______________________________________________________________________________________

Create a Python file named lab_8-6.py

Write a function is_palindrome(word) that takes in a string word 
and returns the true if the word is a palindrome, false otherwise. 

A palindrome is a word that is spelled the same forwards and backwards.



"""
# Author: Andrew Tkacs

# Function to calculate the factorial of a given number
def factorial(num):
    """
    Calculate the factorial of the given number.
    
    Returns:
    - int: The factorial of the number
    """
    # Initialize the result to 1
    result = 1
    
    # Multiply numbers from 1 to num
    for i in range(1, num + 1):
        result *= i
    
    # Return the final result
    return result

num_example = 5
result = factorial(num_example)
print(f"The factorial of {num_example} is {result}.")

