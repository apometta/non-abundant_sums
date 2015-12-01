#Program written by Andrew H. Pometta for Project Euler problem number
#23: "Non-abundant sums" at https://projecteuler.net/problem=23
#See README for details

import sets
import math #sqrt()

#For checking if a number is abundant: go from 2 to sqrt(number), and 
#when we find a zero modulo, add both that and number/that.  There is 
#a faster way for checking if a number is prime or not but 
#since we need a list of all factors that's a no go here.

def abundance_check(num, even):
    sqrt = math.sqrt(num)
    divisor_sum = 1
    if even:
        for n in xrange(2, int(sqrt) + 1):
            if num % n == 0:
                divisor_sum += (n + num / n)
                if n == sqrt:
                    divisor_sum -= n #no double counting
    else:
        #no odd number has an even factor
        for n in xrange(3, int(sqrt) + 1, 2):
            if num % n == 0:
                divisor_sum += (n + num / n)
                if n == sqrt:
                    divisor_sum -= n
    return divisor_sum > num


ab_set = sets.Set()
abundants = []
#abundants contains all abundant numbers in the range, and every possible 
#sum of those two numbers is added to ab_set
for n in xrange(1, 28124):
    if abundance_check(n, n % 2 == 0):
        abundants.append(n)
        for abundant in abundants:
            ab_set.add (abundant + n)

#the sum of all numbers not in ab_set is the answer
non_sums = 0
for n in xrange(1, 28124):
    if n not in ab_set:
        non_sums += n

print non_sums
