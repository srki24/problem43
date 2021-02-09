#  -- Project Eulers Problem 43

# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17

from itertools import permutations as perm
from datetime import datetime
start = datetime.now()


def is_divisible(tup:tuple):
    
    divisors = [2,3,5,7,11,13,17]
    first_digit = list(range(1,8))

    if tup [0] != '0':  
        string_number = "".join(tup)

        for l_slice, divisor in zip(first_digit, divisors):

            r_slice = l_slice + 3

            if int(string_number[l_slice : r_slice]) % divisor != 0:
                return False
        return True
    else:
        return False

        

number_list = [str(x) for x in list(range(10))] # Generating a string in order to convert tuple to a number
total = 0


for permutation in perm(number_list): # Permutations of number list are pandigital by definition
    if is_divisible(permutation):
        pandigital_number = int("".join(permutation))
        total += pandigital_number

print(total, datetime.now()- start, sep='\n')


