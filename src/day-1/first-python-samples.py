# you can run this program on https://www.jdoodle.com/python3-programming-online/ and practice more things there.


# This is a single line comment. this is my first python program and I am happy to be here.

"""
This is called a multi-line comment in python.
What this means is that whatever I type between the quoted section no matter how many lines are used is a comment.
"""

'''
This is also called a multi-line comment in python. there is not difference between writing a multi-line comment using double-quotes or single quotes.
'''

"""
In python, to print something to the console/ result window/ output window, we can use the function print
print is a function.
"""
print("Hello world!")

"""
What is a function?
Functions are a set or group of instructions.

Calling a function - basically means executing a set of instructions together

E.g.  
calculate_income_tax(gross_salary, total_deductions):
    # return calculated tax based on the formulas.
    
income_tax = calculate_income_tax(100000, 4000)

Function has 3 components
1. Function name - the name that you give to a function to call it/ use it (Mandatory)
2. Function parameters - allow you to give them (called as passing) values, which it can use and do something (Optional)
3. Function return value - A function can have a return value based on what the function does (Optional)
"""

"""
Variables - Are quantities whose values are not fixed, because variables are used to create a generalized logic or algorithm in such a way that no matter what value is present in that variable, the
output can be determined.
"""

# in programming languages, variables have a data-type
# what does a data-type mean? integer, floating point values, strings, char,
"""
What a data type is telling you is what kind of data does a variable store.

Everything that the computer deals with is binary. 

E.g. even this text that I am typing the computer understands this as binary.

ASCII UTF-n encoding
"""


"""
(0101 1001) read as int, then it will give me 89
if I tell the computer to read this as a character, then it will read it as 'Y'
if I tell the computer to read this as something else, then it will it read it as that something which is defined concretly

5    9
-- how do you know to read this as alphabet Y, or number (59)decimal or hexadecimal, or something else.
"""

# define a variable
'''
1. You can only use numbers, alphabets, and underscore in your variable name. All other characters like #,$,- are not allowed.
2. Your variable name needs to start with either an alphabet or an underscore e.g. a, a1, b2, _a, _1 are valid. 1a, 1_a 1_2, 1_ are not valid.
3. You need to have at least 1 character as a part of your variable name a aa aaaaaaa aaaa_aaaa _aasdfadsfasd adfasdfasdf_ _adsfadsf23423_asdfads_asdf_123
4. Variable names are case sensitive. i.e. var1, Var1, vAr1, vaR1 are all DIFFERENT variables. They are not the same.
'''

'''
Snake case.
'''
# Integer
int_var = 59
# to convert a int or any other value to a string, you need to call the str(value) function with the value.
print("My first integer variable: " + str(int_var))

# Fractional value or Floating point value in computers
fractional_var = 62.887
print("My first fractional or floating point value is: " + str(fractional_var))

# String values
string_var = "Sarthak"
print("My name is: " + string_var)


"""
Basic operations - addition, multiplication, subtraction, division
"""
"""
Python is converting 1+2+3 -> an object and then this object gets passed to the print function implicitly.
Then, this object is converted to string explicitly
"""

int_sum = 1+2+5+8+9+6
print("My integer sum is: " + str(int_sum))

frac_sum = 1.05 + 0.006 + 1 + 40.7789
print("My fractional sum is: " + str(frac_sum))

int_var_1 = 22
int_var_2 = 56
sum_var = int_var_1 + int_var_2 + 5 + int_sum
print("My complex integer sum is: " + str(sum_var))
print("This is an example of directly printing the sum of a variable without storing it in another variable: " + str(int_var_1 + int_var_2 + 5 + int_sum))

int_diff = 89-100
print("My first integer difference is: " + str(int_diff))
print("Another example of integer difference is: " + str(88-47))
print("An example of fractional difference is: " + str(55.239-47))
print("An example of integer multiplication is: " + str(55*2))
print("An example of fractional multiplication is: " + str(0.1*2))
print("An example of division multiplication is: " + str(4/2))


'''
Learn how to convert from a data type to another data type
'''

# to convert from any data type to string - use str() function
print(str(2))
print(str(2.35))


# to convert from any data type to int - use int() function
print(int(str(2)))
# print(int(str(2.35))) # this will give you an error because str(2.35) gives '2.35' and int cannot convert any non-number characters.
print(int(2.35))
print(int("56") + int("22"))

# print(int(str(2.35)))
print(int(2.35))

# to convert from any data type to float - use float() function
print(float(str(2)))  # str(2) -> float('2') -> 2.0
# print(int(str(2.35))) # this will give you an error because str(2.35) gives '2.35' and int cannot convert any non-number characters.
print(float(str(2.35)))
print(float("56.33") + float("22"))


# function evaluation order - inside out. e.g. print(float(str(55.6))) will first evaluate str(55.6) as "55.6",
# then this will be passed to float("55.6") which will then return 55.6 which is passed to print function.


"""
input function is used to ask user for an input on the console.
"""
value = float(input("Please enter a integer number- "))
print("the value entered by you multiplied by 2 is: " + str(value * 2))
print("the value entered by you divided by 3 is: " + str(value / 3))


# modulo operator - %
# division has 4 parts - the dividend, the divisor, the quotient, the remainder

# e.g. 7 / 3 - quot = 2 and rem = 1

print("The quot of a division between 7 and 3 is: " + (str(int(7 / 3))))
print("The remainder of a division between 7 and 3 is: " + (str(7 % 3)))

'''
power operator - a**b
e.g. a raised to b - a * a * a * a * ..... * a
e.g. 2 raised to 2 - 2 * 2 = 4 (squared)
'''

print("An example of exponents: " + str(3*3*3*3*3*3*3*3*3*3))
print("An example of exponents: " + str(3**10))


print("An example of square of a number: " + str(9**2))


print("The square root of 4 is: " + str(4**(1/2)))
print("The cube root of 27 is: " + str(27**(1/3)))
print("The fourth root of 81 is: " + str(81**(1/4)))
