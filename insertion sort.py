# def helper(list, upper-index)
#       return the same list in which the elements from 0 to a upper-index are sorted ascendingly

def sum(num):
    if num < 1:
        raise ValueError ("invalid number")
    if num == 1:
        return 1
    return num + sum(num)


# def insertion(list:
#       return helper(list, len(list)-1) return the same sorted list