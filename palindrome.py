# determine wether number is palindrome or not
def palindrome(value):
    initial_value = value
    temp = value
    while temp != 0:
        mod = temp % 10
        temp = int((temp - mod) / 10)
        #print(temp)
    rev = (initial_value - mod) + mod
    return rev


if __name__ == "__main__":
    value = int(input("Enter a number"))
    rev_number = palindrome(value)
    #print(rev_number)
    if rev_number == value:
        print(value, "is a palindrome")
    else:
        print(value, "is not a palindrome")



