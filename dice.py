import random as r
player = []
num = 0
side = 0

i = "Yes"
while i:
    reset = len(player)
    print('Total player\'s: ' + str(reset))
    print ("""
    1. Add a player
    2. Remove a player
    3. Clear all players
    4. Roll the dice
    5. Choose number of sides
    """)
    opt = input('Choose an option: ')
    if opt == '1':
        addPlayer = input('Who would you like to add: ')
        player.append(addPlayer)
        print('Player Added!')
        for x in player:
            print(x)
    elif opt == '2':
        name = input('What player would you like to remove: ')
        if name in player:
            player.remove(name)
            print(player)
        else:
            print('Player does not exist')
    elif opt == '3':
        print('Player\'s Cleared!')
        del player [:]
    elif opt == '4':
        if side == 0:
            side = 6
            print('Defualt sides set to 6')
        if reset >= 1:
            print("Num is currently set at: " + str(num))
            if num == reset:
                num = 0
            print(player[num] + "'s roll!")
            roll = r.randint(1, int(side))
            print(roll)
            num = num + 1
        elif reset == 0:
            print('No players added, add a player to roll')
    elif opt == '5':
        side = input('What number of sides: ')
        times = input('How many times: ')
        if side == '':
            print('Incorrect value, please enter a number of sides!')
    elif opt > '5':
        print('Invalid option!')
