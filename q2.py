"""
Question2
Create a function that reverses a boolean value and returns the string "boolean expected" if
another variable type is given.
Examples
reverse(True) ➞ False
reverse(False) ➞ True
reverse(0) ➞ "boolean expected"
reverse(None) ➞ "boolean expected"
"""

def reverse(s):
    if s == 'True':
        return 'False'
    elif s == 'False':
        return 'True'
    return "boolean expected"

s = input("Enter Input ")
s1 = reverse(s)
print("reverse(",s,") ➞",s1)