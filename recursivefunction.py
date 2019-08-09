# using a recursion function, calculate the sum of integers from 1 ro n
def addition(n):
    if n == 0:
        return 0
    return n + (addition(n - 1))


# fibonacci sequence
def fib(index):
    if index <= 1:
        return 1
    else:
        return((fib(index - 1)) + (fib(index - 2)))


if __name__ == "__main__":
    n = int(input("please enter a number: "))
    index = int(input("please enter another number: "))
    addition(n)
    print('the sum of integers from 1 to', n, '==', addition(n))
    fib(index)
    print('the', str(index) + 'nd/th', 'term of the fibonacci sequence is:', fib(index))
