# Functions

'''
def function_name():
    code goes here
'''


def print_hello():
    print("Printing from print_hello function")
    print("Hello world")


def add_integers(a, b):
    print("Sum of a and b:", a+b)


def product(a, b):
    my_sum = 0
    for _ in range(b):
        my_sum += a
    return my_sum


print_hello()
add_integers(1, 2)
add_integers(-5, 16)
print("Product of 3 integers:", product(3, 9))


'''
Function overloading and overriding
'''


# def my_sum(a, b):
#     return a+b


# def my_sum(a, b, c):
#     return a+b+c


# def my_sum(a, b, c, d):
#     return a+b+c+d


# def my_sum(a, b, c, d, e):
#     return a+b+c+d+e


# print(my_sum(3, 2, 3, 4, 5))
# print(my_sum(3, 3, 3))


# iterative solution
def iter_solution(arg):
    for ch in arg:
        print(ch)

# recursive solution


def recur_solution(arg, i=0):
    print(arg)
    # does something with this argument
    if len(arg) > 0:
        print(arg[0])
        recur_solution(arg[i+1:], i)


# recur_func("hello")
# iter_solution("hello")
recur_solution("sarthak")

'''
1. recur_solution("hello")

def recur_solution(arg, i=0):
    # does something with this argument
    if len(arg) > 0:
        print(arg[0])
        recur_solution(arg[i+1:], i)


recur_solution("hello")
recur_solution("ello")
recur_solution("llo")
recur_solution("lo")
recur_solution("o")
recur_solution("")

hello -> h
ello -> e
llo -> l |
lo -> l  |
o -> o   |
'''

# implementing fibbonacci numbers using recursion
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 . ..


def sum_and_prod(a, b):
    return a+b, a*b


def sum_prod_diff(a, b):
    return a+b, a*b, a-b


s, p = sum_and_prod(5, 6)
print("Sum and product: ", s, p)
sp = sum_and_prod(5, 6)  # [a+b, a*b]
print("Sum and product: ", sp[0], sp[1])

s, p, d = sum_prod_diff(7, 9)
print("Sum, product and difference: ", s, p, d)

spd = sum_prod_diff(7, 9)
print("Sum, product and difference: ", spd[0], spd[1], spd[2])
