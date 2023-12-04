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

# Function to check if a given word is a palindrome
def is_palindrome(word):
    """
    Check if the given word is a palindrome.
    
    Returns: - bool: True if the word is a palindrome, False otherwise
    """
    # Convert the word to lowercase to make the comparison case-insensitive,
    word_lower = word.lower()
    
    # Compare the original word with its reverse
    return word_lower == word_lower[::-1]

word_example = "radar"
result = is_palindrome(word_example)
print(f"The word '{word_example}' is a palindrome: {result}.")


