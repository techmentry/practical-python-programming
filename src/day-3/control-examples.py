# Ternary operator - condition ? <if_true> : <if_false>
'''
<if_true> if <condition> else <if_false>
if condition:
    if_true
else:
    if_false
'''
# Example 1 - If a number is positive
# step 1 : take a number from the user
user_input = input("Please enter any integer: ")
# step 2 : convert the user input string to a integer
int_value = int(user_input)
# step 3 : print the result
print("The number is: ", "Positive" if int_value >
      0 else ("Zero" if int_value == 0 else "Negative"))


# in operator
'''
Checks or handles assignment of a value from a collection
Check - It verifies if a value is present
Handles Assignment - It also tackles putting the value in a variable
Collection - It is a set of values
'''

'''
Example of in in case of strings

We want to see if el is present in the string hello
'''
if 'el' in 'Heoll':
    print("el is present in Hello")
else:
    print("el is not present in Hello")


# example - calculation of income tax

'''
Define problem - 
if our income is < 250000 py then 0 IT
if our income is > 250000 but less than 500000 py then 10% of the difference above 250000 IT
if our income is > 500000 but less than 1200000 py then 20% for amount between 5l-12l and then 10% of 5l and 2.5l IT
if our income is > 1200000 py then 25% for amount > 12l and then 10% of 5l and 2.5l IT
'''
tax_bracket_1 = 2.5e5
tax_bracket_2 = 5e5
tax_bracket_3 = 12e5
user_salary = float(input("Please enter your annual gross income: "))
user_tax = 0.0

# if user_salary <= tax_bracket_1:
#     user_tax = 0.0
# elif user_salary > tax_bracket_1 and user_salary <= tax_bracket_2:
#     user_tax = (user_salary - tax_bracket_1) * 0.1
# elif user_salary > tax_bracket_2 and user_salary <= tax_bracket_3:
#     user_tax = ((user_salary - tax_bracket_2) * 0.2 +
#                 (tax_bracket_2 - tax_bracket_1) * 0.1)
# elif user_salary > tax_bracket_2 and user_salary <= tax_bracket_3:
#     user_tax = (
#         (user_salary - tax_bracket_3) * 0.25 +
#         (tax_bracket_3 - tax_bracket_2) * 0.2 +
#         (tax_bracket_2 - tax_bracket_1) * 0.1)

bracket_1_amount, bracket_1_multiplier = 0, 0
bracket_2_amount, bracket_2_multiplier = 0, 0
bracket_3_amount, bracket_3_multiplier = 0, 0

if user_salary > tax_bracket_1:
    bracket_1_amount = user_salary
    bracket_1_multiplier = 1
    if user_salary > tax_bracket_2:
        bracket_1_amount = tax_bracket_2
        bracket_2_amount = user_salary
        bracket_2_multiplier = 1
        if user_salary > tax_bracket_3:
            bracket_2_amount = tax_bracket_3
            bracket_3_amount = user_salary
            bracket_3_multiplier = 1

user_tax = ((bracket_3_amount - tax_bracket_3) * 0.25 * bracket_3_multiplier +
            (bracket_2_amount - tax_bracket_2) * 0.2 * bracket_2_multiplier +
            (bracket_1_amount - tax_bracket_1) * 0.1 * bracket_1_multiplier)


print("Tax that the user has to pay: ", user_tax)