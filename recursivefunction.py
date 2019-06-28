# using a recursion function, calculate the sum of integers from 1 ro n

n = int(input("please enter a number"))


def addition(n):
    if n == 0:
        return 0
    return n + (addition(n - 1))


print(addition(n))

# fibonacci sequence

index = int(input("please enter another number"))


def fib(index):
    if index <= 1:
        return 1
    else:
        return((fib(index - 1)) + (fib(index - 2)))


print(fib(index))

# write a recursive function that calculates (m  n) using pascal formula

m =
n =

def coefficent(num):
    if num == 0:
        return 0
    return(coefficent()

def binary_Search(sorted_list, num):
    if num == 400:
        return 0

