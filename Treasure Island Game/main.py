from art import logo


def game():
    choice1 = input("left or right? ").lower()
    if choice1 == 'left':
        print('''You've come to a lake. There is an island in the middle of the lake.
    Type "wait" to wait for a boat. Type "swim" to swim across.''')

        choice2 = input("wait or swim? ").lower()
        if choice2 == 'wait':
            print('''You arrive at the island unharmed. There is a house with 3 doors.
    One red, one yellow and one blue. Which colour do you choose?''')

            choice3 = input("red, yellow or blue? ").lower()
            if choice3 == 'yellow':
                print("You found the treasure! You Win!")
            else:
                print('You chose the wrong door. Game Over.')
        else:
            print('You got attacked by an angry trout. Game Over.')

    else:
        print('You fell into a hole. Game Over.')


print(logo)
print('''Welcome to Treasure Island.
Your mission is to find the treasure.
You are at the cross road where do you want to go? Type "left" or "right"''')
game()
