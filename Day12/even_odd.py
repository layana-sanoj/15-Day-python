# tells if a number is even or odd

while True:
    num=input("Enter a number (or 'q' to quit): ")
    if num.lower()=='q':
        print("Exiting the program.")
        exit()
    try:
        num=int(num)
        if num%2==0:
            print(num,'is an even number.')
        else:
            print(num,'is an odd number.')
    except:
        print("Please enter a valid integer.")
