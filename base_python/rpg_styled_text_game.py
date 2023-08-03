import random


weapon = ['sword','knife','bow','cross-bow']
damage = [100,30,70,95]
speed = [60,150,70,40]
weapon_stats = {'weapon_type':weapon,
                'damage':damage,
                'speed':speed}


difficulty_level = ['easy','medium','hard']


weapon_stats

user_difficulty = input('Select difficulty (easy/medium/hard)').lower()

if user_difficulty == 'easy':
    max_health_bar = 10
    lost_health_bar_count = 0
    initial_gold = 50
    print(f'You start the game with {max_health_bar} health bars and {initial_gold} coins')
elif user_difficulty == 'medium':
    max_health_bar = 9
    lost_health_bar_count = 0
    initial_gold = 35
    print(f'You start the game with {max_health_bar} health bars and {initial_gold} coins')
else:
    max_health_bar = 8
    lost_health_bar_count = 0
    initial_gold = 30
    print(f'You start the game with {max_health_bar} health bars and {initial_gold} coins')


while lost_health_bar_count < max_health_bar:
    
    user_weapon = random.choice(list(weapon_stats['weapon_type']))
    print(f'Your will fight with a {user_weapon}!')
    user_answer1 = input('''You see a foreigner approaching you.You don't know his intentions.You can either talk to him or run away.Do you stay? (answer yes or no)''').lower()
    user_answer2 = ''
    if user_answer1 == 'yes':
        user_answer2 = input('''Dont' worry. The man is seeking company.\nHe says he used to be an adventurer just like you then he took an arrow to the knee.\nNevertheless, you might need his help.\nDo you want to recruite him? (answer yes/no)''').lower()
        if user_answer2 == 'yes':
            print('You have a companion!')
        else:
            print('You decided not to recruit him. Perhaps this mas was a thief or maybe even a murderer...')
    else:
        print('You decided to run away. Perhaps this man was a thief or maybe even a murderer...')
        
    print('''It's getting dark. You see a tavern. Perhaps you could use some sleep...''')
    user_answer3 = input('Do you enter the tavern? Overnight here costs 10 coins. (answer yes/no)').lower()

    if user_answer3 == 'yes' and user_answer1 == 'yes' and user_answer2 == 'yes':
        if initial_gold >=10:
            print('You pay 10 coins for the overnight.')
            initial_gold = initial_gold - 10
            print(f'You have {initial_gold} coins left. Use them responsibly!')
            print('The day has come to an end')
            print('''The day just dawns. It's time to venture forth with your companion!''')
            print('''You managed to survive so far upon 1 day. I'm wondering what awaits you...''')
            print(f'As the beginning of the second day, you have {initial_gold} coins left and {10 - lost_health_bar_count} health bar left')
        else:
            print('You wanted to spend the night in the tavern, but you have no enough coins.')
            print('You hear several footsteps. Drunk thugs decided to mug you and your friend')
            if user_weapon == 'sword' or user_weapon == 'knife':
                print(f'You managed to defend yourself with your {user_weapon}. Good job, you saved yourself and your friend!')
            else:
                initial_gold = initial_gold - 10
                lost_health_bar_count = lost_health_bar_count + 2
                if lost_health_bar_count >= max_health_bar:
                    print('You are dead. Good luck next time!')
                    break
                print('You and your friend are robbed and beaten. You lost 10 coins and 2 health bars.')
                print(f'You have {initial_gold} coins left. Use them responsibly!')
                print(f'You have {10 - lost_health_bar_count} health bar left')

    elif user_answer3 == 'yes' and user_answer1 == 'yes' and user_answer2 == 'no':
        if initial_gold >=10:
            print('You pay 10 coins for the overnight.')
            initial_gold = initial_gold - 10
            print(f'You have {initial_gold} coins left. Use them responsibly!')
            print('''The day just dawns. It's time to venture forth!''')
            print('''You managed to survive so far upon 1 day. I'm wondering what awaits you...''')
            print(f'As the beginning of the second day, you have {initial_gold} coins left and {10 - lost_health_bar_count} health bar left')
        else:
            print('You wanted to spend the night in the tavern, but you have no enough coins.')
            print('''It's getting dark and dangerous...''')
            print('You hear several footsteps. Drunk thugs decided to mug you')
            if user_weapon == 'sword' or user_weapon == 'knife':
                print(f'You managed to defend yourself with your {user_weapon}. Good job!')
            else:
                initial_gold = initial_gold - 10
                lost_health_bar_count = lost_health_bar_count + 2
                if lost_health_bar_count >= max_health_bar:
                    print('You are dead. Good luck next time!')
                    break
                print(f'Your {user_weapon} is useless for short range battles... You are robbed and beaten. You lost 10 coins and 2 health bars. ')
                print(f'You have {initial_gold} coins left. Use them responsibly!')
                print(f'You have {10 - lost_health_bar_count} health bar left')
    
    elif user_answer3 == 'yes' and user_answer1 == 'no' and user_answer2 == '':
        if initial_gold >=10:
            print('You pay 10 coins for the overnight.')
            initial_gold = initial_gold - 10
            print(f'You have {initial_gold} coins left. Use them responsibly!')
            print('''The day just dawns. It's time to venture forth!''')
            print('''You managed to survive so far upon 1 day. I'm wondering what awaits you...''')
            print(f'As the beginning of the second day, you have {initial_gold} coins left and {10 - lost_health_bar_count} health bar left')
        else:
            print('You wanted to spend the night in the tavern, but you have no enough coins.')

    elif user_answer3 == 'no':
        if user_answer2 == 'no' or user_answer2 == '':
            if user_answer1 == 'yes' or user_answer1 == 'no':
                print('''You start thinking that it wasn't a good idea. It's getting dark and dangerous...''')
                print('You hear several footsteps. Drunk thugs decided to mug you')
                if user_weapon == 'sword' or user_weapon == 'knife':
                    print(f'You managed to defend yourself with your {user_weapon}. Good job!')
                else:
                    initial_gold = initial_gold - 10
                    lost_health_bar_count = lost_health_bar_count + 2
                    if lost_health_bar_count >= max_health_bar:
                        print('You are dead. Good luck next time!')
                        break
                    print(f'Your {user_weapon} is useless for short range battles... You are robbed and beaten. You lost 10 coins and 2 health bars. ')
                    print(f'You have {initial_gold} coins left. Use them responsibly!')
                    print(f'You have {10 - lost_health_bar_count} health bar left')

    elif user_answer3 == 'no' and user_answer1 == 'yes' and user_answer2 == 'yes':
        print('''You start thinking that it wasn't a good idea. It's getting dark and dangerous...''')
        print('You hear several footsteps. Drunk thugs decided to mug you and your friend')
        if user_weapon == 'sword' or user_weapon == 'knife':
            print(f'You managed to defend yourself with your {user_weapon}. Good job, you saved yourself and your friend!')
        else:
            initial_gold = initial_gold - 10
            lost_health_bar_count = lost_health_bar_count + 2
            if lost_health_bar_count >= max_health_bar:
                    print('You are dead. Good luck next time!')
                    break
            print('You and your friend are robbed and beaten. You lost 10 coins and 2 health bars.')
            print(f'You have {initial_gold} coins left. Use them responsibly!')
            print(f'You have {10 - lost_health_bar_count} health bar left')
        
    user_answer4 = input('You see an announcement on the noticeboard. The village administrator pays 10 coins for killing several monsters that scare villagers. Do you accept this task? (answer yes/no)').lower()
    
    if user_answer4 == 'yes': 
        if user_answer1 == 'yes':
            if user_answer2 == 'yes':
                user_answer5 = input('''You and your friend need to prepare for the fight. Do you want to buy several potions from a the village's magician for 5 coins? (answer yes/no)''').lower()
                if initial_gold >=5:
                    initial_gold = initial_gold - 5
                    print(f'You have {initial_gold} coins left. Use them responsibly!')
                    print('You and your friend venture into the woods')
                    if user_weapon == 'sword' or user_weapon == 'knife':
                        print(f'Since you have a {user_weapon}, it will be a short-distance battle.')
                        print('You drink the potions to increase your stamina')
                        print('The battle begins. You quickly kill the monsters, although one of them managed to scratch you')
                        print('''Your friend was a great help, if it hadn't been for him, you likely would have been dead now...''')
                        print('''If you had a bow or a cross-bow, you probably wouldn't get hurt, but who knows...''')
                        print('Nevertheless, you earned 10 coins. Unfortunately, you also lost 2 health bars.')
                        initial_gold = initial_gold + 10
                        lost_health_bar_count = lost_health_bar_count + 2
                        if lost_health_bar_count >= max_health_bar:
                            print('You are dead. Good luck next time!')
                            break
                        print(f'You have {initial_gold} coins left. Use them responsibly!')
                        print(f'You have {10 - lost_health_bar_count} health bars left. Better be cautious...')
                        print('''You spend the rest of the day in the village's tavern.''')
                    else:
                        print(f'Since you have a {user_weapon}, it would be better to take a good position to shoot from a long distance.')
                        print('You and your friend climb on a tree as it would be a great spot to shot down the monsters')
                        print('You drink the potions to increase your stamina')
                        print('''Everything goes as expected. You kill the monsters and return to the village's administrator''')
                        print('You earned 10 coins. Good job!')
                        initial_gold = initial_gold + 10
                        print(f'You have {initial_gold} coins left. Use them responsibly!')
                        print('''You spend the rest of the day in the village's tavern.''')
                else:
                    print('You wanted to buy the potions, but you have no coins left.')
                    if user_weapon == 'sword' or user_weapon == 'knife':
                        print(f'Since you have a {user_weapon}, it will be a short-distance battle.')
                        print('The battle begins. You quickly kill the monsters, although one of them managed to scratch you')
                        print('''Your friend was a great help, if it hadn't been for him, you likely would have been dead now...''')
                        print('''If you had a bow or a cross-bow, you probably wouldn't get hurt, but who knows...''')
                        print('Nevertheless, you earned 10 coins. Unfortunately, you also lost 4 health bars. You wish you could have afforded these potions back in there...')
                        initial_gold = initial_gold + 10
                        lost_health_bar_count = lost_health_bar_count + 4
                        if lost_health_bar_count >= max_health_bar:
                            print('You are dead. Good luck next time!')
                            break
                        print(f'You have {initial_gold} coins left. Use them responsibly!')
                        print(f'You have {10 - lost_health_bar_count} health bars left. Better be cautious...')
                        print('''You spend the rest of the day in the village's tavern.''')
                    else:
                        print(f'Since you have a {user_weapon}, it would be better to take a good position to shoot from a long distance.')
                        print('You and your friend climb on a tree as it would be a great spot to shot down the monsters')
                        print('''You kill the monsters but also get injured. You earn 10 coins, but also lose 2 health bars. You wish you could have afforded these potions back in there...''')
                        initial_gold = initial_gold + 10
                        lost_health_bar_count = lost_health_bar_count + 2
                        print(f'You have {initial_gold} coins left. Use them responsibly!')
                        print(f'You have {10 - lost_health_bar_count} health bars left. Better be cautious...')
                        if lost_health_bar_count >= max_health_bar:
                            print('You are dead. Good luck next time!')
                            break
                        print('''You spend the rest of the day in the village's tavern.''')
            else:
                user_answer5 = input('''You need to prepare for the fight. Do you want to buy several potions from a the village's magician for 5 coins? (answer yes/no)''').lower()
                if initial_gold >=5:
                    initial_gold = initial_gold - 5
                    print(f'You have {initial_gold} coins left. Use them responsibly!')
                    print('You venture into the woods')
                    if user_weapon == 'sword' or user_weapon == 'knife':
                        print(f'Since you have a {user_weapon}, it will be a short-distance battle.')
                        print('You drink the potions to increase your stamina')
                        print('The battle begins. You quickly kill the monsters, although one of them managed to scratch you')
                        print('''If you had a bow or a cross-bow, you probably wouldn't get hurt, but who knows...''')
                        print('You also could have used some company...')
                        print('Nevertheless, you earned 10 coins. Unfortunately, you also lost 2 health bars.')
                        initial_gold = initial_gold + 10
                        lost_health_bar_count = lost_health_bar_count + 4
                        if lost_health_bar_count >= max_health_bar:
                            print('You are dead. Good luck next time!')
                            break
                        print(f'You have {initial_gold} coins left. Use them responsibly!')
                        print(f'You have {10 - lost_health_bar_count} health bars left. Better be cautious...')
                        print('''You spend the rest of the day in the village's tavern.''')
                    else:
                        print(f'Since you have a {user_weapon}, it would be better to take a good position to shoot from a long distance.')
                        print('You climb on a tree as it would be a great spot to shot down the monsters')
                        print('You drink the potions to increase your stamina')
                        print('''You kill the monsters but also get injured''')
                        print('Perhaps you could have used some company...')
                        print('You earned 10 coins and lost 2 health bars.')
                        initial_gold = initial_gold + 10
                        lost_health_bar_count = lost_health_bar_count + 2
                        if lost_health_bar_count >= max_health_bar:
                            print('You are dead. Good luck next time!')
                            break
                        print(f'You have {initial_gold} coins left. Use them responsibly!')
                        print('''You spend the rest of the day in the village's tavern.''')
                else:
                    print('You wanted to buy the potions, but you have no coins left.')
                    if user_weapon == 'sword' or user_weapon == 'knife':
                        print(f'Since you have a {user_weapon}, it will be a short-distance battle.')
                        print('The battle begins. You quickly kill the monsters, although one of them managed to scratch you')
                        print('''If you had a bow or a cross-bow, you probably wouldn't get hurt, but who knows...''')
                        print('Perhaps you could have used some company...')
                        print('You earned 10 coins and lost 6 health bars. You wish you could have afforded these potions back in there...')
                        initial_gold = initial_gold + 10
                        lost_health_bar_count = lost_health_bar_count + 6
                        print(f'You have {initial_gold} coins left. Use them responsibly!')
                        print(f'You have {10 - lost_health_bar_count} health bars left. Better be cautious...')
                        if lost_health_bar_count >= max_health_bar:
                            print('You are dead. Good luck next time!')
                            break
                        print('''You spend the rest of the day in the village's tavern.''')
                    else:
                        print(f'Since you have a {user_weapon}, it would be better to take a good position to shoot from a long distance.')
                        print('You climb on a tree as it would be a great spot to shot down the monsters')
                        print('''You kill the monsters but also get injured. You earn 10 coins, but also lose 4 health bars. You wish you could have afforded these potions back in there...''')
                        print('Perhaps you could have used some company...')
                        initial_gold = initial_gold + 10
                        lost_health_bar_count = lost_health_bar_count + 4
                        print(f'You have {initial_gold} coins left. Use them responsibly!')
                        print(f'You have {10 - lost_health_bar_count} health bars left. Better be cautious...')
                        if lost_health_bar_count >= max_health_bar:
                            print('You are dead. Good luck next time!')
                            break
                        print('''You spend the rest of the day in the village's tavern.''')


        else:
            user_answer5 = input('''You need to prepare for the fight. Do you want to buy several potions from a the village's magician for 5 coins? (answer yes/no)''').lower()
            if initial_gold >=5:
                    initial_gold = initial_gold - 5
                    print(f'You have {initial_gold} coins left. Use them responsibly!')
                    print('You venture into the woods')
                    if user_weapon == 'sword' or user_weapon == 'knife':
                        print(f'Since you have a {user_weapon}, it will be a short-distance battle.')
                        print('You drink the potions to increase your stamina')
                        print('The battle begins. You quickly kill the monsters, although one of them managed to scratch you')
                        print('''If you had a bow or a cross-bow, you probably wouldn't get hurt, but who knows...''')
                        print('You also could have used some company...')
                        print('You earned 10 coins. Unfortunately, you also lost 4 health bars.')
                        initial_gold = initial_gold + 10
                        lost_health_bar_count = lost_health_bar_count + 4
                        print(f'You have {initial_gold} coins left. Use them responsibly!')
                        print(f'You have {10 - lost_health_bar_count} health bars left. Better be cautious...')
                        if lost_health_bar_count >= max_health_bar:
                            print('You are dead. Good luck next time!')
                            break
                        print('''You spend the rest of the day in the village's tavern.''')
                    else:
                        print(f'Since you have a {user_weapon}, it would be better to take a good position to shoot from a long distance.')
                        print('You climb on a tree as it would be a great spot to shot down the monsters')
                        print('You drink the potions to increase your stamina')
                        print('''You kill the monsters but also get hurt. You problaby could have used some company...''')
                        print('You earned 10 coins, but also lost 2 health bars')
                        initial_gold = initial_gold + 10
                        lost_health_bar_count = lost_health_bar_count + 2
                        print(f'You have {initial_gold} coins left. Use them responsibly!')
                        print(f'You have {10 - lost_health_bar_count} health bars left. Better be cautious...')
                        if lost_health_bar_count >= max_health_bar:
                            print('You are dead. Good luck next time!')
                            break
                        print('''You spend the rest of the day in the village's tavern.''')
            else:
                print('You wanted to buy the potions, but you have no coins left.')
                if user_weapon == 'sword' or user_weapon == 'knife':
                    print(f'Since you have a {user_weapon}, it will be a short-distance battle.')
                    print('The battle begins. You quickly kill the monsters, although one of them managed to scratch you')
                    print('''If you had a bow or a cross-bow, you probably wouldn't get hurt, but who knows...''')
                    print('You also could have used some company...')
                    print('Nevertheless, you earned 10 coins. Unfortunately, you also lost 4 health bars. You wish you could have afforded these potions back in there...')
                    initial_gold = initial_gold + 10
                    lost_health_bar_count = lost_health_bar_count + 6
                    if lost_health_bar_count >= max_health_bar:
                        print('You are dead. Good luck next time!')
                        break
                    print(f'You have {initial_gold} coins left. Use them responsibly!')
                    print(f'You have {10 - lost_health_bar_count} health bars left. Better be cautious...')
                    print('''You spend the rest of the day in the village's tavern.''')
                else:
                    print(f'Since you have a {user_weapon}, it would be better to take a good position to shoot from a long distance.')
                    print('You climb on a tree as it would be a great spot to shot down the monsters')
                    print('''You kill the monsters but also get injured. You earn 10 coins, but also lose 4 health bars. You wish you could have afforded these potions back in there...''')
                    print('You also could have used some company...')
                    initial_gold = initial_gold + 10
                    lost_health_bar_count = lost_health_bar_count + 4
                    if lost_health_bar_count >= max_health_bar:
                        print('You are dead. Good luck next time!')
                        break
                    print(f'You have {initial_gold} coins left. Use them responsibly!')
                    print(f'You have {10 - lost_health_bar_count} health bars left. Better be cautious...')
                    print('''You spend the rest of the day in the village's tavern.''')

        
    
    else:
        print('You decided not to accept the task. Who knows if it was a good choice?...')
        print('''You spend the rest of the day in the village's tavern.''')


    
    user_answer5 = ''
    if user_answer4 == 'yes' and user_answer1 == 'yes' and user_answer2 =='yes':
        print('You and your friend drank a lot of beers. You see several crooks approaching you. They are trying to rob you!')
        user_answer5 = input('You can either let them rob you or fight. Do you wish to fight? (answer yes/no)').lower()
        if user_answer5 == 'yes':
            print('''This wasn't a good idea. Not only you got robbed of 10 coins, but you also lost 2 health bars. Your friend tried to defend you, but you were outnumbered.''') 
            initial_gold = initial_gold - 10
            if initial_gold <=0:
                print('You have no coins left...')
            else:
                print(f'You have {initial_gold} coins left')
            lost_health_bar_count = lost_health_bar_count + 2
            if lost_health_bar_count >= max_health_bar:
                    print('You are dead. Good luck next time!')
                    break
            print(f'You have {10 - lost_health_bar_count} health bars left. Better be cautious!')
        else:
            print('You got robbed of 10 coins. But you are not hurt.')
            initial_gold = initial_gold - 10
            if initial_gold <=0:
                print('You have no coins left...')
            else:
                print(f'You have {initial_gold} coins left')
            
    elif user_answer4 == 'yes' and user_answer1 == 'yes' or user_answer1 == 'no' and user_answer2 == 'no' or user_answer2 == '':
        print('You drank a lot of beers. You see several crooks approaching you. They are trying to rob you!')
        user_answer5 = input('You can either let them rob or fight. Do you wish to fight? (answer yes/no)').lower()
        if user_answer5 == 'yes':
            print('''This wasn't a good idea. Not only you got robbed of 10 coins, but you also lost 2 health bars.''') 
            initial_gold = initial_gold - 10
            if initial_gold <=0:
                print('You have no coins left')
            else:
                print(f'You have {initial_gold} coins left')
            lost_health_bar_count = lost_health_bar_count + 2
            if lost_health_bar_count >= max_health_bar:
                    print('You are dead. Good luck next time!')
                    break
            print(f'You have {10 - lost_health_bar_count} health bars left. Better be cautious!')
        else:
            print('''You got robbed of 10 coins. But you are not hurt. That's something''')
            initial_gold = initial_gold - 10
    else:
        print('You drank a lot of beers. You see several crooks approaching you. They are trying to rob you!')
        user_answer5 = input('You can either let them rob or fight. Do you wish to fight? (answer yes/no)').lower()
        if user_answer5 == 'yes':
            print('''This wasn't a good idea. Not only you got robbed of 10 coins, but you also lost 2 health bars.''') 
            initial_gold = initial_gold - 10
            if initial_gold <=0:
                print('You have no coins left')
            else:
                print(f'You have {initial_gold} coins left')
            lost_health_bar_count = lost_health_bar_count + 2
            if lost_health_bar_count >= max_health_bar:
                    print('You are dead. Good luck next time!')
                    break
            print(f'You have {10 - lost_health_bar_count} health bars left. Better be cautious!')
        else:
            print('''You got robbed of 10 coins. But you are not hurt. That's something''')
            initial_gold = initial_gold - 10
            if initial_gold <=0:
                print('You have no coins left')
            else:
                print(f'You have {initial_gold} coins left')

    print(f'''The day has come to an end. You managed to survive so far upon 2 days. As the beginning of the second day, you have {initial_gold} coins left and {10 - lost_health_bar_count} health bar left''')
    print('''I'm wondering what awaits you...''')

    user_answer6 = input('''You see a blacksmith. He offers to repair your weapon for 20 coins. Do you accept his offer? (answer yes/no)''').lower()
    if user_answer6 == 'yes':
        if initial_gold >= 20:
            initial_gold = initial_gold - 20
            print(f'You have {initial_gold} coins left. Use them responsibly!')
            if user_answer4 == 'yes' and user_answer1 == 'yes' and user_answer2 =='yes':
                print('''You and your friend venture onto the woods. Suddenly, you hear wolves howling. There's not time left to run away. You have to fight!''')
                print('''You got just a little hurt. If it hadn't been for the blacksmith, you sword would have probably brittled...''')
                print('You lose 1 health bar')
                lost_health_bar_count = lost_health_bar_count + 1
                if lost_health_bar_count >= max_health_bar:
                    print('You are dead. Good luck next time!')
                    break
                print(f'You have {10 - lost_health_bar_count} health bars left. Better be cautious!')
            elif user_answer4 == 'yes' or user_answer4 == 'no' and user_answer1 == 'yes' or user_answer1 == 'no' and user_answer2 == 'no' or user_answer2 == '':
                print('''You venture onto the woods. Suddenly, you hear wolves howling. There's not time left to run away. You have to fight!''')
                print('You lose 2 health bars')
                lost_health_bar_count = lost_health_bar_count + 2
                if lost_health_bar_count >= max_health_bar:
                    print('You are dead. Good luck next time!')
                    break
        else:
            print('''You wanted to reapair your weapons, but you can't afford it.''')
            if user_answer4 == 'yes' and user_answer1 == 'yes' and user_answer2 =='yes':
                print('''You and your friend venture onto the woods. Suddenly, you hear wolves howling. There's not time left to run away. You have to fight!''')
                print('You lose 2 health bar')
                lost_health_bar_count = lost_health_bar_count + 2
                if lost_health_bar_count >= max_health_bar:
                    print('You are dead. Good luck next time!')
                    break
                print(f'You have {10 - lost_health_bar_count} health bars left. Better be cautious!')
            elif user_answer4 == 'yes' or user_answer4 == 'no' and user_answer1 == 'yes' or user_answer1 == 'no' and user_answer2 == 'no' or user_answer2 == '':
                print('''You venture onto the woods. Suddenly, you hear wolves howling. There's not time left to run away. You have to fight!''')    
                print('You lose 2 health bar')
                lost_health_bar_count = lost_health_bar_count + 2
                if lost_health_bar_count >= max_health_bar:
                    print('You are dead. Good luck next time!')
                    break 
                print(f'You have {10 - lost_health_bar_count} health bars left. Better be cautious!')
    else:
        print('''You venture onto the woods. Suddenly, you hear wolves howling. There's not time left to run away. You have to fight!''')
        print('''You got hurt. You probably should have repaired your sword back in there...''')
        print('You lose 4 health bars.')
        lost_health_bar_count = lost_health_bar_count + 4
        if lost_health_bar_count >= max_health_bar:
            print('You are dead. Good luck next time!')
            break 
    
    print(f'You completed the game with {10 - lost_health_bar_count} health bars and {initial_gold} coins. Good job!')

    break

else:
    print('You are dead. Good luck next time!')

