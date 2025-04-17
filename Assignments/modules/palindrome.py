def palindrome():
    s = input("Enter a string: ")
    if s == s[::-1]:
        print("Given string is palindrome.")
    else:
        print("Given string is not palindrome.")