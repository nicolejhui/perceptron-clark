#take two integers and print the output
def addition(x, y):
    sum = x + y
    return sum

def subtraction(x, y):
    difference = x - y
    return difference

def multiply(x, y):
    product = x * y
    return product

def divide(x, y):
    quotient = x/y
    return quotient

# Pass in four numbers, add x, y, sub w, z, multiply (x+y, w-z), return value
def fun_time(w, x, y, z):
    xy_sum = x + y
    wz_difference = w - z
    fun_time_product =  xy_sum * wz_difference
    return fun_time_product

if __name__ == "__main__":
    x = 4
    y = 6
    w = 2
    z = 8
    total_addition = addition(x, y)
    print(str(x), '+', str(y), '=', total_addition)
    total_subtraction = subtraction(x, y)
    print(str(x), '-', str(y), '=',total_subtraction)
    total_multiplication = multiply(x, y)
    print(str(x), '*', str(y), '=', total_multiplication)
    total_division = divide(x, y)
    print(str(x), '/', str(y), '=', total_division)
    total_fun_time = fun_time(w, x, y, z)
    print('(', str(x), '+', str(y), ')', '*', '(', str(w), '-', str(z), ')', '=', total_fun_time)

