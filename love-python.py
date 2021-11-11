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
testList = ["test"]
print(type(testList))

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

# Datatypes:
# Numbers
# Integers
x = 10; y =-1
print(x, type(x))
# Floats
x = 10.51
print(x, type(x))
# Complex
x = 1 + 2j
print(x, type(x))
# Strings
x = "Hello"
print(x, type(x))
# Lists
x = ["Hello", "World"]
print(x, type(x))
# Tuples
x = ("Hello", "World")
print(x, type(x))
# Dictionaries
x = {"key": "value"}
print(x, type(x))
# Sets
x = {"Hello", "World"}
print(x, type(x))
# Booleans
x = True
print(x, type(x))
# None
x = None
print(x, type(x))

print("+" * 50)

# Random Numbers
import random

print(random.randrange(1, 10))

print("+" * 50)

# Mutiline Strings
print(""""Multiline String""")

print("+" * 50)

# Strings as array.
string = "Hello"
print(string[0])

for i in string:
    print(i)

# Length of string
print(string, "Length:", len(string))

# In String
# It is case sensitive
print("Hello" in string)

# Not in String
print("World" not in string)

# Slicing in String
print(string[0:2])

# Slice to end in String
print(string[:4])

# Slice from start in String
print(string[4:])

# upper and lower case
print(string.upper())
print(string.lower())

# trim in string
string1 = "   Strip   "
print(string1.strip())


# Replace in String
string2 = "Hello World World"
print(string2.replace("World", "Python"))

# Split in String
string3 = "Hello World World"
print(string3.split(" "))

# Format in string similar to template string
print("I {1} {0}".format("python", "love"))

# Escape characters
print("Hello\nWorld")
print("\"I Love Python\"")

print("+" * 50)

# Booleans
print(("Booleans:").upper())
print("Hello", bool("Hello"))
print("\"\"", bool(""))
print(0, bool(0))
print({}, bool({}))
print(None, bool(None))

print("")
# isInstance
print("isInstance hello str", isinstance("Hello", str))
print("isInstance 1 int", isinstance(1, int))

print("+" * 50)

# identity operators - is & is not
print("Identity Operators:")
print("id(x)", id(x))
print("id(y)", id(y))
print("id(x) == id(y)", id(x) == id(y))
print("x is y", x is y)
print("x is not y", x is not y)

print("+" * 50)

# membership operators
print("Membership Operators:")
y = ["apple", "banana"]
x = "apple"

print("x in y", x in y)
print("x not in y", x not in y)

print("+" * 50)

# Lists in python.
print("Lists: ")
sampleList = ["sample", "list", "of", "values"]
print(sampleList)

# sortting the list
x = sampleList
x.sort()
print(x)

x = [1,12,2,9,85]
x.sort()
print(x)
x.sort(reverse=True)
print(x)

x = ["1","12","2","9","85"]
x.sort()
print(x)

# Negative indexing starts from -1
print("negative indexing", x[-1])

# Range in lists
print("Range in lists", x[-5:])


print("+" * 50)
# age = int(input("How old are you? "))
# if age >= 18 and age <= 65:
#     print("You can vote")

# else:
#     # So the spacing  only matters, in the specific code block.
#     print("You cannot vote")
