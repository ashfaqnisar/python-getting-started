# Print
print("I love python")

print("+" * 50)

# Variables, Casting and typeof
# Reassignment is allowed
x = 10.51 + 5
x = "Hello"
x = 2
print(int("10") - x)
x = str(x)
print(x)
x = float(x)
print(x)
print(type(x))

print("+" * 50)

# Case Sensitive, Naming Conventions, Concatenation
X = "Hello"
_Y = "World"
# This is not allowed
# x-y = "test"
print(X + _Y)

print("+" * 50)

# Assigning multiple values
# Cannot do this in python.
# a=1, b=2, c=3
a, b, c = 1, 2, 3
print(a, b, c)
a = b = c = 1
print(a, b, c)

print("+" * 50)

# Unpack a collection, similar to spread operator.
abc = ["list", "of", "values"]
a, b, c = abc
print(a, b, c)
xyz = ["list", "of"]
# p, q, r = xyz
# This is not allowed, and will cause an error.
test = ["sample", "list", "of", "values"]
# a, b, c = test
# This is not allowed, we should have the same number of items in the variables and list.
# print(a, b, c)

print("+" * 50)

# Functions, Global Variables;
# Global Variable
xy = "test"


def printTest():
    print(xy)


def printSample():
    # Local Variable.
    xy = "Sample Test"
    print(xy)


printSample()
printTest()

print("+" * 50)

# Global Variables from function
sample = "Sample Test"
def updateSample():
    global sample
    sample = "Updated Sample"
updateSample()

print(sample)

print("+" * 50)

age = int(input("How old are you? "))
if age >= 18 and age <= 65:
    print("You can vote")

else:
    # So the spacing  only matters, in the specific code block.
    print("You cannot vote")
