# trying out try/except function
number=input("Enter a number: ")
try:
    numb =int(number)
    print("You entered:", numb)
except:
    print("That's not a valid number!")
