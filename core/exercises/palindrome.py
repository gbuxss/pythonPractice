# Write a program to check input string is palindrome or not

user_input = input("Enter Word:\t")
reversed_word = user_input[::-1]
if user_input == reversed_word:
    print("word is palindrome")
else:
    print("Word is not palindrome")
