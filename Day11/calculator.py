# a simple calculator that can add, subtract, multiply, and divide two numbers
#input the numbers
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
except:
    print("Invalid input. Please enter numeric values.")
    quit()
#input the operation
while True:
    op=input ('Enter the operation (+,-,*,/): ')
    if op == '+' or op == '-' or op == '*' or op == '/':
        break
    else:
        print("Invalid operation. Please enter one of +, -, *, /.")
        quit()
#perform the operation
if op=='+':
    ans= num1+num2
elif op=='-':
    ans=num1-num2
elif op=='*':
    ans=num1*num2  
elif op=='/':
    # check for division by zero
    if num2==0:
        print('Error!')
        print('Division by zero is not allowed.')
        quit()
    else:
        ans=num1/num2
print('The answer is:', round(ans, 2))
