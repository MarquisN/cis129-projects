# Marquis Neely
# March 25, 2024
# code to check if something is a palindrome 

# Function to check if a string is a palindrome
def is_palindrome(s: str) -> bool:
    # Normalize the string: remove spaces, punctuation, and convert to lowercase.
    normalized_str = ""
    for char in s:
        if char.isalnum():  # Check if character is alphanumeric
            normalized_str += char.lower()

    # Use a list as a stack to reverse the string.
    stack = []
    for char in normalized_str:
        stack.append(char)  # Push each character onto the stack

    # Create the reversed string by popping from the stack.
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()

    # Compare the original normalized string with the reversed string.
    return normalized_str == reversed_str

# Ask the user to input a word or phrase to check for palindrome.
user_input = input("Enter a word or phrase to check if it's a palindrome: ")

# Check if the input is a palindrome and print the result.
if is_palindrome(user_input):
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")
