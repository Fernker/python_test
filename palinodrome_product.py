"""A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 99.Find the largest
palindrome made from the product of two 3-digit numbers."""

first = 100
first_result = 0
second_result = 0
highest = 0

#loop through first set of 3 digit numbers
while first < 1000:
    second = 100
    #loop through second set of 3 digit numbers for every first set up numbers
    while second < 1000:
        result = first*second

        #cast as string
        string = str(result)

        #split string in half
        first_half, second_half = string[::2], string[1::2]

        #flip second half
        second_half = second_half[::-1]

        #compare to see if they are the same
        if first_half == second_half:
            #if current value is higher than previous high
            if result > highest:
                highest = result
                first_result = first
                second_result = second
        second += 1
    first += 1

print "The highest palindromic number is %s by %s * %s" % (highest, first_result, second_result)

