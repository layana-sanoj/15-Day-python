#a simple game of choice using if_else statement
print('Welcome to my game XD')
print('This is a simple game')
print('You have to choose the correct option to escape.')
ch1= input('you are in a room with 2 doors leading to the outside, one door is red and the other is blue. Which door do you choose: '.upper())
if ch1 == 'red':
    print('you chose the red door, you are trapped in a room with a lion that has not eaten for 3 years')
    print('you are dead')
elif ch1== 'blue':
    print('you got out of the room which leads to a beautiful garden')
    ch2 = input('you see a river and a bridge, do you want to cross the bridge or swim across the river? (bridge/swim): '.upper())
    if ch2 == 'bridge':
        print('you crossed the bridge and found a treasure chest full of gold coins')
        print('you win!')
    elif ch2 == 'swim':
        print('you swam across the river but got caught in a whirlpool')
        print('you are dead')
    else:
        print('invalid choice, you are dead')
else:
    print('invalid choice, you are dead')
