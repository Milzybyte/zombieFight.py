


from random import randint

game_running = True

def calculate_zombie_attack():
    return randint(zombie['grab_attack'], zombie['bite_attack'])

while game_running == True:
    new_find = True
    print('---' * 7)
    name = input('Enter Player Name: ')
    print('---' * 7)
    
    player = {'player_name': name, 'attack': 12, 'heal': 15, 'health': 100}
    zombie = {'name': 'zombie', 'grab_attack': 8, 'bite_attack': 15, 'health': 120}

    print(player['player_name'] + ' has ' + str(player['health']) + ' health ')
    print(zombie['name'] + ' has ' + str(zombie['health']) + ' health ')

    while True:

        player_won = False
        zombie_won = False

        print('---' * 7)
        print('Action Select')
        print('(1) Attack')
        print('(2) heal')
        print('(3) Run')
        print('(9) quit')
        
        player_choice = input()
        
        if player_choice == '9':
            print('Exiting game!')
            break
                    
        if player_choice == '1':
            zombie['health'] = zombie['health'] - player['attack']
            if zombie['health'] <= 0:
                player_won = True

            else:
                player['health'] = player['health'] - calculate_zombie_attack()
                if player['health'] <= 0:
                    zombie_won = True

        elif player_choice == '2':
            player['health'] = player['health'] + player['heal']

            player['health'] = player['health'] - calculate_zombie_attack()
            if player['health'] <= 0:
                zombie_won = True

        elif player_choice == '3':
            new_round = False
            game_running = False
        
        
        
        else:
            print('Invalid Input')

        if player_won == False and zombie_won == False:
            print(player['player_name'] + ' has ' + str(player['health']) + ' left ')
            print(zombie['name'] + ' has ' + str(zombie['health']) + ' left ')

        elif player_won:
            print(player['player_name'] + ' Won! ')
            new_round = False

        elif zombie_won:
            print('The Zombie Got You!!!')
            new_round = False
            
            
 