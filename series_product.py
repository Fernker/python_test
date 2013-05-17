"""Complete this program to find the greatest produdct of five consecutive
digits in the list"""
in_file = open('array.txt')

#read contents, and replace \n
file_contents = in_file.read().replace('\n','')

#Get length of file for while loop
length = file_contents.__len__()


position = 0

highest_number = 0
highest_chunk = None

while position < length-4:
    #get chunk of numbers
    chunk = file_contents[0+position:5+position]

    number = 1
    #put each number into a list and iterate through
    for i in list(chunk):
        #cast number as an int and multiply against previous numbers (or 1 for first iteration)
        number *= int(i)

    #if newly multiplied number is higher than previous high, replace it
    if number > highest_number:
        highest_number = number
        highest_chunk = chunk

    #move the chunk window
    position += 1

print "The highest product is %s produced from chunk %s" % (highest_number, highest_chunk)

