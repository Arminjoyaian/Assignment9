import random
print('10 : "1play"  , 11 : "2play"' )
Play = int(input("Enter number :"))
if Play == 10:
    for i in range(3):
        player = input('rock , paper , scissors    : ')
        r = random.randint(0 , 2)
        if r ==0 :
             computer = 'rock'
        elif r == 1 :
             computer = 'paper'
        else:
             computer = 'scissors '
        print(player)
        print(computer)

        if player == computer:
            print('equal')
        elif player == 'rock':
            if computer == 'scissors':
                print("player win")
            else:
                print("computer win")
        elif player == 'paper':
            if computer == 'rock':
                print('player win')
            else:
                 print('computer win')
        elif player == 'scissors':
            if computer == 'paper':
                 print('player win')
            else:
                print("computer win")
        else:
             print("No")
elif Play == 11:
    for i in range(3):
         player_1 = input('rock , paper , scissors    : player_1 : ')
         player_2 = input('rock , paper , scissors    : player_2 : ')
         print(player_1)
         print(player_2)

         if player_1 == player_2:
             print('equal')
         elif player_1 == 'rock':
             if player_2 == 'scissors':
                 print("player_1 win")
             else:
                 print("player_2 win")
         elif player_1 == 'paper':
             if player_2 == 'rock':
                 print('player_1 win')
             else:
                 print('player_2 win')
         elif player_1 == 'scissors':
             if player_2 == 'paper':
                 print('player_1 win')
             else:
                 print("player_2 win")
         else:
             print("No _2")
else:
     print("The entered number is incorrect")
    