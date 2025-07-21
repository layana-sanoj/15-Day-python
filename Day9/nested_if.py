# the code for printing 'weird' if the number is not a multiple of 2 or the number is between the numbers 6 and 20
num = input("Enter a number: ")
n=int(num)
if (n%2 !=0):
    print("Weird")
else:
    if (n>=2 and n<=5):
        print("Not Weird")
    elif(n >=6 and n<=20):
        print("Weird")
    else:
        print("not weird")
        
