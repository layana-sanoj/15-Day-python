# multtplication table generator
# This script generates a multiplication table for a given number.
while True:
    num=input('Enter a number: (or "q" to quit): ')
    if num.lower()=='q':
        print('Exiting the program.')
        exit()
    try:
        num=int(num)
    except:
        print('Invalid input. Please enter a valid integer.')
        exit()

    print('The multiplication table for', num, 'is:')
    for i in range(1,11):
        ans=num*i
        print(num,'x',i,'=',ans)
