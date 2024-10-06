''' Write a python function find_duplicates(), which accepts a list of numbers and returns another list containing all the duplicate values in the input list and the order should be same as in the input list. If there are no duplicate values, it should return an empty list.'''
def find_duplicates(list_of_numbers):
    seen = set()  # Set to track numbers that have been encountered
    duplicates = []  # List to store duplicates
    
    # Dictionary to track the frequency of each number
    frequency = {}

    # Count occurrences of each number
    for number in list_of_numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1

    # Find duplicates based on frequency
    for number in list_of_numbers:
        if frequency[number] > 1 and number not in seen:
            duplicates.append(number)
            seen.add(number)

    return duplicates

# Test the function
list_of_numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
list_of_duplicates = find_duplicates(list_of_numbers)
print(list_of_duplicates)
