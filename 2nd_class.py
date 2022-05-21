# Fundamental Data Type
# 1. int 2. float 3. bool 4. string
# Collection of Data Type
# 1. list 2. tuple 3. dict 4. set

# print is a function

# How to see which type of Data
print(type(3+4))
print(type(3/4))

# Collection Of Data Type

# Set Data Type
set = {1, 2, 1}
print(set)
print(type(set))

# List Data Type
list = [1, 2, 3]
print(list)
print(type(list))

# Tuple Data Type [unchangeable value; if you assign a value, you can not change this value]
tuple = ('Mamun', 'Farhaan')
print(tuple)
print(type(tuple))

# Dictionary Data Type [dict is one kind of map]
dict = {'Name': 'Farhaan'}
print(dict)
print(type(dict))

# Precedence
# 1.(),[],{} 2.** 3.*,/ 4.+,-
# // => Means Result; Is that 3)4(1
# %(Modules) => Means Remainder
# ** => Means Power or Square

# Example of **
print(3 ** 2)
# Example of //
print(3 // 2)
# Example of %
print(3 % 2)
# Example of (), +, -, *, /
print(37 + 34 * (3 + 7) / 32)

# Round Function == { [.0] to [.4] is called Floor and [.5] to [.9] is called Ceiling }
print(round(3.3))
print(round(3.9))

# Absolute Function
print(abs(-5.7))

# Code from Neeti

# math
print(5+3)
print(5-3)
print(5*3)
print(5/3)
print(5 % 3)
print(5 & 3)
print("Neeti")
print("2122")


# type
print(type(5+3))
print(type(5-3))
print(type(5*3))
print(type(5/3))
print(type(5 % 3))
print(type(5 & 3))
print(type("Neeti"))
print(type("2122"))


# If-else

if(5 > 2):
    print("Five is Greater than 2")

if(5 < 10):
    print("10 is Greater than 5")

x = 5
y = "Python"
print(x)
print(y)

#This is Comment

"""
This is a comment
written in 
more that just one line
"""

x = 5
y = 10
print(x + y)

x = 5
y = 10
z = x-y
print(z)
print(x-y)
print(abs(x - y))

x = 5
y = 10
z = x+y
print(z)
print(x * y)


x = 5
y = 10
z = x/y
print(z)
print(x / y)


x = 5
y = 10
z = x*y
print(z)
print(x * y)


x = 4
x = "Neeti"
print(x)


x = str(3)
y = int(36)
z = float(369)
print(x)
print(y)
print(z)


# Legal Variable Name
myName = "Neeti"
my_name = "Sen"
_my_name = "Srabonti"
myNamE = "Jashore"
MYNAME = "KHAjura"
myname9 = "Python"
myNAME98 = "Editor"

print(myName)
print(my_name)
print(_my_name)
print(myNamE)
print(MYNAME)
print(myname9)
print(myNAME98)


# Illegal variable names:
# Remember that variable names are case-sensitive
"""
2my_name= "Neeti"
my-name = "Sen"
my name = "Srabonti"
"""

"""
Multi Words Variable Names:
1.Camel Case: Each word, except the first, starts with a capital letter=> 
myVariavleName = "Neeti"
2.Pascal Case: Each word starts with a capital letter=>
MyVariableName = "John"
3.Snake Case: Each word is separated by an underscore character=>
my_variable_name = "John"
"""


# Python Variables - Assign Multiple Values
x, y, z = "Neeti", "Briti", "Nandini"
print(x)
print(y)
print(z)
print(x, y, z)

# One Value to Multiple Variables
x = y = z = "Neeti"
print(x)
print(y)
print(z)
print(x, y, z)


# Unpack a Collection
# you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

sisters = ["Neeti", "Briti", "Nandini"]
x, y, z = sisters
print(x)
print(y)
print(z)
print(x, y, z)
print(sisters)
print(type(sisters))


x = "Python "
y = "is "
z = "Easy to Learn"
print(x + y + z)
print(x, y, z)

# tuple
tuple = ("Mango", "Watermelon", "Grape")
print(tuple)
print(type(tuple))

# set
a = {1, 2, 3}
print(a)
print(type(a))

# dictionary
a = {"name": "Apple"}
print(a)
print(type(a))


# math
print(20+9*2)
print(20+(12-8)*2)
print(3**2)
print(3//2)
print(round(5.4))
print(round(5.6))
print(abs(9-11))

a = ["a", "r", "b", "o", "b"]
print(a)
print(type(a))


# Complex Number
a = 15 + 15j
print(a)
print(type(a))


x = (39+13j)
y = (3+1j)
print(x+y)
print(x*y)
print(x-y)
print(x/y)


# int to bin,hex,oct
a = bin(4)
print(a)
b = hex(10)
print(b)
c = oct(8)
print(c)

print(int("0b101", 2))
print(int("A", 16))
print(int("100", 36))
