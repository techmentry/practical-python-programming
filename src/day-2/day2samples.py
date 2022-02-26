"""
Day 2: Boolean variables, conditionals, control structures, loops
"""

int_var = 1
frac_var = 2.333333
string_var = "Hello class hope you are doing well!"
print(int_var)
print(frac_var)
print(string_var)

'''
Boolean variables/ bool
They can only have one of 2 values
True or False

Logical operators
and operator
or operator
xor operator
not operator

binary and unary operators 

Binary operator - works on 2 operand
Unary operator - works on 1 operand

<val1> logical_operator <val2> - boolean expression which gives boolean value
'''
bool_var_1 = True
bool_var_2 = False
print(bool_var_1)
print(bool_var_2)

# == - equality operator, it is a binary operator. checks if the value on both sides are equal
print(1 == 2)
print(1 == 1)
var_1 = 2.4
var_2 = 2.4
print(var_1 == var_2)

# > - greater than operator - checks if the value on LHS is greater than RHS
# < - less than operator - checks if the value on LSH is less than RHS
var_1 = 2.4
var_2 = 2.4
print(var_1 > var_2)
var_1 = 2.44
var_2 = 2.46
print(var_1 < var_2)

# >= - greater than or equal to operator - checks if the value on LHS is greater than or equal to RHS
# <= - less than or equal to operator - checks if the value on LSH is less than or equal to RHS
var_1 = 123
var_2 = 123
print(var_1 >= var_2)
var_1 = 456
var_2 = 789
print(var_1 <= var_2)

# not operator - logical not. flips the boolean value
expression_1 = 123 == 123
print(not expression_1)

# '!' equals operator - checks if one value is not equal to the other
expression_1 = 123 != 123
expression_2 = not(123 == 123)
print("exp_1 ", expression_1)
print("exp_2 ", expression_2)

# and operator - True only if LHS and RHS are true, else results in false
print("----------------------------------------")
expression_1 = True and True
print(expression_1)
expression_1 = False and True
print(expression_1)
expression_1 = True and False
print(expression_1)
expression_1 = False and False
print(expression_1)
print("----------------------------------------")

# or operator - True if either values are true. Only false when both are false
print("----------------------------------------")
expression_1 = True or True
print(expression_1)
expression_1 = False or True
print(expression_1)
expression_1 = True or False
print(expression_1)
expression_1 = False or False
print(expression_1)
print("----------------------------------------")

print("----------------------------------------")


def test():
    print("I was called")
    return 1 == 1


print("----------------------------------------")


print("----------------------------------------")
# short circuit operators - and & or
print("Short circuit happens here------------------------")
expression_1 = False and test()
print(expression_1)
expression_1 = True or test()
print(expression_1)
print("Short circuit DOES NOT happen here------------------------")
expression_1 = True and test()
print(expression_1)
expression_1 = False or test()
print(expression_1)
print("----------------------------------------")

# xor operator ^
print("----------------------------------------")
expression_1 = True ^ True
print(expression_1)
expression_1 = False ^ True
print(expression_1)
expression_1 = True ^ False
print(expression_1)
expression_1 = False ^ False
print(expression_1)
print("----------------------------------------")

'''
Decision making - basically is that you want to control the flow of your code
Primary - if else or if elif else

if <condition>:
print()
'''
if False:
    print("Condition was true")
    print("Another statement")
print("----------------------------------------")

if True:
    print("Inside the if block")
else:
    print("Inside the else block")

print("----------------------------------------")

# example of odd even numbers
num = 11
if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

print("----------------------------------------")

# if-elif ladder
'''
'''
titanic_available = False
tanhaji_available = True
two_states_available = True
spiderman_available = True
golmaal_available = True

if titanic_available:
    print("Tickets for titanic are available")
elif tanhaji_available:
    print("Tickets for tanhaji are available")
elif two_states_available:
    print("Tickets for two_states are available")
elif spiderman_available:
    print("Tickets for spiderman are available")
elif golmaal_available:
    print("Tickets for golmaal are available")
else:
    print("No tickets are available")

print("----------------------------------------")

if titanic_available:
    print("Tickets for titanic are available")
if tanhaji_available:
    print("Tickets for tanhaji are available")
if two_states_available:
    print("Tickets for two_states are available")
if spiderman_available:
    print("Tickets for spiderman are available")
if golmaal_available:
    print("Tickets for golmaal are available")
else:
    print("No tickets are available")
print("----------------------------------------")

# Nested if else

td_available = True

if titanic_available:
    if td_available:
        print("Titanic is available in 3d")
    else:
        print("Titanic is available, but not in 3d")
else:
    print("Titanic is not available")


if titanic_available or tanhaji_available:
    print("Booking a ticket for a movie")
else:
    print("Did not find tickets for desired movie")

# example of logical operator chaining
if tanhaji_available or golmaal_available or spiderman_available:
    print("Booking a ticket for a movie")
else:
    print("Did not find tickets for desired movie")

print("----------------------------------------")
# BODMAS or PEDMAS
'''
B- brackets
O - of
Div/Mult - similar hierarchy
Add/Sub - similar hierarchy
'''
print(5 * 2 + 8)
print(5 * (2 + 8))

rice_available = True
spices_available = False
chicken_available = True
lamb_available = False
peas_available = True
carrots_available = True
mushrooms_available = True

# chaining of logical operators and use of brackets for grouping expressions
if (rice_available
            and spices_available
            and (
                (
                    chicken_available
                    or lamb_available
                    or (
                        peas_available
                        and carrots_available
                        and mushrooms_available
                        )
                )
            )
        ):
    print("Biryani can be made")
else:
    print("Biryani can not be made")

print("----------------------------------------")
'''
Loops - what are they?
When we want execute a certain instructions multiple times, then we use loops

Python - 2 types of loops
for 
while 

In other languages like JAVA C++ C C# etc
for
while
do while
'''

# while <condition>:
#    write statements here

counter = 10

while counter >= 0:
    print("Current counter value is ", counter)
    counter = counter - 1

print("Loop over")
print("----------------------------------------")


# Loop control statements - continue and break

counter = 10
while True:
    if counter < 0:
        break
    print("Current counter value is ", counter)
    counter = counter - 1
print("----------------------------------------")
counter = 10
while counter >= 0:
    if counter % 2 == 0:
        counter = counter - 1
        continue

    print("Current counter value is ", counter)
    counter = counter - 1

print("Loop over")
print("----------------------------------------")

# function range

# range(10) - generate numbers from 0-9

# for loop - for iteration_variable in [collection]:
#
print("For loop example --------")
for num in range(10):
    print(num)
print("For loop example --------")


# range(stop_number) - uniformly spaced integers between 0 and stop_number in steps of 1
# range(start_number, stop_number) - uniformly spaced integers between start_number and stop_number in steps of 1
# range(start_number, stop_number, step_number)

print("range(stop_number) example-=---------")
for num in range(10):
    print(num)
print("range(start_number, stop_number) example-=---------")
for num in range(4, 12):
    print(num)
print("range(start_number, stop_number, step_number) example-=---------")
for num in range(5, 26, 3):
    print(num)
