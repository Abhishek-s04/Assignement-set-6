'''Write a recursive function, is_palindrome() to find out whether a string is a palindrome or not. The function should return true, if it is a palindrome. Else it should return false. 

Note- Perform case insensitive operations wherever necessary.'''
def is_palindrome(word):
    word = word.lower()  # Convert the word to lowercase for case-insensitive comparison
    
    # Base case: If the word has 0 or 1 characters, it's a palindrome
    if len(word) <= 1:
        return True
    if word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    return False

#Provide different values for word and test your program
result=is_palindrome("MadAMa")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")