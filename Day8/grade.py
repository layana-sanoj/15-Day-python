# find grade by entering marks
mrk= input('Enter your mark:')
try:
    m=float(mrk)
except:
    print("Error! please enter numeric input")
    exit()

if m>100 or m<0:
    print("Error! marks cannot be greater than 100")
elif m>=90:
    print("Grade A")
elif m>=80:
    print("Grade B")
elif m>=70:
    print("Grade C")
elif m>=60:
    print("Grade D")
else:
    print("Grade F")
