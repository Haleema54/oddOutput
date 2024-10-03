'''

9) Raju is a 3rd grade kid, he is struggling to find which is "even" number and which is a "odd" number. So, his teacher gave him a task to find how many even numbers and how many odd numbers are there in the given collection of values and print "Even" if even count is more than odd count, else print "Odd", if odd count is more and print "Equal" if both even count and odd count are same. Help Raju to understand the difference of even and odd.
Sample Input:
1 2 3 4 5
Sample Output:
Odd
program:
# Input: Read the numbers as a single line of space-separated integers
values = list(map(int, input().split()))

# Initialize counters for even and odd numbers
even_count = 0
odd_count = 0

# Iterate through the values to count even and odd numbers
for number in values:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Determine the result based on the counts
if even_count > odd_count:
    print("Even")
elif odd_count > even_count:
    print("Odd")
else:
    print("Equal")
'''
