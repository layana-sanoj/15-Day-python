# Random 6-faced Dice roller

import random
while True:
    qn=input("Press Enter to roll the dice (or type 'q' to quit): ")
    if qn.lower()=='q':
        print('Exiting the game.')
        exit() 
    
    # generate a random number between 1 and 6
    dice=random.randint(1,6)
    print("You rolled a", dice)
    if dice == 1:
        print(" ⚀") 
    elif dice == 2:
        print(" ⚁")
    elif dice == 3:
        print(" ⚂")
    elif dice == 4: 
        print(" ⚃")
    elif dice == 5:
        print(" ⚄")
    elif dice == 6:
        print(" ⚅")
    
    again=input ("Do you want to roll again? (y/n): ")
    if again.lower()== 'n':
        print("Thanks for playing!")
        exit()
