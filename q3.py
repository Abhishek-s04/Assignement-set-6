''' Write a python function find_smallest_number() which accepts a number n and returns the smallest number having n divisors.
Handle the possible errors in the code written inside the function.

Sample Input: 16
Expected Output 120
'''
import math

# Function to count the divisors of a number
def count_divisors(x):
    count = 0
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            if i == x // i:
                count += 1  # Both divisors are the same
            else:
                count += 2  # Divisors are different
    return count

# Function to find the smallest number with exactly 'num' divisors
def find_smallest_number(num):
    try:
        if num < 1:
            raise ValueError("Number of divisors must be a positive integer.")
        
        # Start checking numbers from 1 upwards
        smallest_number = 1
        while True:
            if count_divisors(smallest_number) == num:
                return smallest_number
            smallest_number += 1

    except ValueError as e:
        print("Error:", e)

# Test the function
num = 16
print("The number of divisors:", num)
result = find_smallest_number(num)
print("The smallest number having", num, "divisors:", result)
