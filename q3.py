"""
Question3
Create a function that returns the thickness (in meters) of a piece of paper after folding it
n number of times. The paper starts off with a thickness of 0.5mm.
Examples
num_layers(1) ➞ "0.001m"
# Paper folded once is 1mm (equal to 0.001m)
num_layers(4) ➞ "0.008m"
# Paper folded 4 times is 8mm (equal to 0.008m)
num_layers(21) ➞ "1048.576m"
# Paper folded 21 times is 1048576mm (equal to 1048.576m)
"""

def thickness(n):
    return (2 ** n) * 0.5 / 1000

n = int(input("Enter no of layers "))
t = thickness(n)
print("num_layers(",n,") ➞",t,"m")