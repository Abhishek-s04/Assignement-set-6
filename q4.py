''' A 10-substring of a number is a substring of its digits that sum up to 10.

For example, the 10-substrings of the number 3523014 are:
3523014, 3523014, 3523014, 3523014

Write a python function, find_ten_substring(num_str) which accepts a string and returns the list of 10-substrings of that string.

Handle the possible errors in the code written inside the function.

Sample Input : '3523014'

Expected Output: ['5230', '23014', '523', '352']

'''
#lex_auth_01269442545042227276
def find_ten_substring(num_str):
    try:
        # Validate that the input string contains only digits
        if not num_str.isdigit():
            raise ValueError("Input must be a string of digits.")
        
        ten_substrings = []
        length = len(num_str)
        
        # Loop over every possible starting point of the substring
        for i in range(length):
            current_sum = 0
            substring = ""
            
            # Generate substrings starting from index i
            for j in range(i, length):
                current_sum += int(num_str[j])  # Add the digit to the current sum
                substring += num_str[j]         # Append the digit to the substring
                
                # If the sum equals 10, store the substring
                if current_sum == 10:
                    ten_substrings.append(substring)
                
                # If the sum exceeds 10, stop this substring search
                elif current_sum > 10:
                    break
        
        return ten_substrings
    
    except ValueError as e:
        print("Error:", e)

# Test the function
num_str = "2825302"
print("The number is:", num_str)
result_list = find_ten_substring(num_str)
print(result_list)

