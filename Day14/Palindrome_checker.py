while True:
    sen=input("Enter a word (or 'q' to quit): ")
    if sen.lower() == 'q':
        print("Exiting the program.")
        break
    sen=sen.lower()
    if sen==sen[::-1]:
        print("The word is a palindrome.")
    else:
        print("The word is not a palindrome.")
