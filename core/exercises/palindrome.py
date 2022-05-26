# Write a program to check input string is palindrome or not
def palindrome(input_word):
    reversed_word = input_word[::-1]
    if user_input == reversed_word:
        print(f"Word '{input_word}' is palindrome")
    else:
        print(f"Word '{input_word}' is not palindrome")


user_input = input("Enter Word:\t")
palindrome(user_input)