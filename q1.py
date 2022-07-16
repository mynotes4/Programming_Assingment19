"""
Question1
Create a function that takes a string and returns a string in which each character is repeated
once.
Examples
double_char("String") ➞ "SSttrriinngg"
double_char("Hello World!") ➞ "HHeelllloo  WWoorrlldd!!"
double_char("1234!_ ") ➞ "11223344!!__  "
"""
def double_char(s):
    s1 = ''
    for i in s:
        s1 = s1 + i*2
    return s1

s = input("Enter String ")
s1 = double_char(s)
print(s1)