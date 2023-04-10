import random
import os

logo_treasure = '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[Binati]
*******************************************************************************
'''

def findTheTreasure():
    '''To find the treasure the player has to make three choices:

       - The first is to select a direction to go (left or right)
       - The second is to decide to swim or wait for a boat at a river
       - The third is to select one of three doors where the treasure is found

       To succeed your selected choice should match that selected by the computer
    '''
    play = True
    while play:
        print(f'{logo_treasure}\nWelcome to Treasure Island.\nYour mission is to find the treasure box...')
        move = random.choice(['right', 'left'])
        ans = input('Do you want to go left or right? l = left/r = right:\n').lower()
        if (ans == 'right' or ans == 'r') and move == 'left':
            print('Game Over! You fell into a pit \U0001F631 \U0001F628!')
        elif (ans == 'left' or ans == 'l') and move == 'right':
            print('Game Over! You fell into a ditch \U0001F631 \U0001F628!')
        else:
            move = random.choice(['swim', 'wait'])
            ans = input('You are at a lake... Do you want to swim or wait for a boat? s = swim/w = wait:\n').lower()
            if (ans == 'swim' or ans == 's') and move == 'wait':
                print('Game Over! You have been attacked by a shark \U0001F631 \U0001F628!')
            elif (ans == 'wait' or ans == 'w') and move == 'swim':
                print('Game Over! Your boat got attacked by pirates \U0001F631 \U0001F628!')
            else:
                door = random.choice(['blue', 'red', 'yellow'])
                ans = input('You have arrived at 3 doors... select a door? b = blue/r = red/y = yellow:\n').lower()
                if (ans == 'yellow' or ans == 'y') and door == 'yellow':
                    print('You win! You found the treasure box \U0001F44F \U0001F60A \U0001F60C!')
                elif (ans == 'red' or ans == 'r') and door == 'red':
                    print('Congratulations! You found the treasure box \U0001F44F \U0001F60A \U0001F60C!')
                elif (ans == 'blue' or ans == 'b') and door == 'blue':
                    print('Bravo!! You found the treasure box \U0001F44F \U0001F60A \U0001F60C!')
                else:
                    print('Game Over! You have been attacked by a lion \U0001F631 \U0001F628!')
                    
        ans = input('Do you want to play again? y = yes/n = no: ')
        if ans == 'no' or ans == 'n':
            print('Goodbye \U0001F44B!')
            play = False
        else:
            os.system('cls || clear')

################################################################################################

logo_number = '''
  ________                                 _____     _______               ___.                 
 /  _____/ __ __   ____   ______ ______   /  _  \    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/  /  /_\  \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \\
\    \_\  \  |  /\  ___/ \___ \ \___ \  /    |    \ /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  > \____|__  / \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/          \/          \/            \/    \/     \/    
'''

def guessANumber():
    '''In the Guess a Number game the computer choses a random number
       in a specified range and the player is requested to guess the number.
       The player is provided with two options - easy and hard.
       The easy option allows the player with a maximum of 10 trials while
       the hard option gives the player a maximum of 5 trials to guess the number.
    '''
    print(f'\nWelcome to Number Guessing Game\n{logo_number}')
    low = 1
    high = 100

    play = True
    while play:
        num = random.randint(low, high)
        level = input('Choose a difficulty level "e = easy / h = hard": ').lower()
        if level == 'e' or level == 'easy':
            max_trials = 10
            print(f'You are allowed {max_trials} attempts...')
        else:
            max_trials = 5
            print(f'You are allowed {max_trials} attempts...')
        guess = None
        while num != guess:
            guess = int(input(f'Enter your guess between {low} and {high}: '))
            if (guess < low) or (guess > high):
                print(f'Your guess must be between {low} and {high}...')
            elif num > guess:
                print(f'The number is higher than {guess}...\n')
                max_trials -= 1
                print(f'You have {max_trials} attempts remaining')

            elif num < guess:
                print(f'The number is lower than {guess}...\n')
                max_trials -= 1
                print(f'You have {max_trials} attempts remaining')

            else:
                print(f'You won \U0001F60A\U0001F60C!! Your guess is {guess} and the number is {num}!\n')
        
            if max_trials == 0:
                frown = ''
                print(f'You lost \U0001F61E! The number is {num}')
                break

        ans = input('Do you want to play again? y = yes/n = no: ').lower()
        if ans == 'no' or ans == 'n':
            play = False
        else:
            os.system('cls || clear')


####################################################################################################

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
logo_hangman = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/  
'''

stages = ['''
    +---+
    O   |
   /|\  |
   / \  |
        |
   ======
 ''', '''
    +---+
    O   |
   /|\  |
   /    |
        |
   ======
 ''', '''
    +---+
    O   |
   /|\  |
        |
  =======
 ''', '''
    +---+
    O   |
   /|   |
        |
        |
  =======
  ''', '''
    +---+
    O   |
    |   |
        |
        |
  =======
 ''', '''
    +---+
    O   |
        |
        |
        |
  =======
     ''']


def hangman():
    '''This is a hangman game where: 
    
       - The computer selects a word randomly from a list and indicates the number
       of letters in the word with hyphens "-". 
       - The player then tries to guess the letters in the word and the guessed letter is 
       used to replace the hyphens until the word is complete. 
       - For every missed guess the hangman figure will begin to form. 
       - After 6 missed guesses the hangman figure is complete and the player loses! 
       - Otherwise, the player wins!
    '''
    play = True
    while play:
        print(f'\nWelcome to Hangman game\n{logo_hangman}')
        chosen_word = random.choice(words)

        display = ['_'] * len(chosen_word)
        print(display)
        lives = 6
        guesses = []
        misses = []
        while lives > 0:
            guess = input('Guess a letter: ').lower()
            if guess in guesses:
                print(f'You already guessed "{guess}"...')
                guess = input('Guess a letter: ').lower()
            else:
                guesses.append(guess)
            for idx, char in enumerate(chosen_word):
                if guess == char:
                    display[idx] = guess
            if guess not in chosen_word:
                misses.append(guess)
                lives -= 1
                print(stages[lives])
                if lives == 0:
                    print('You lost \U0001F620!')
                    print(f'Chosen word is "{chosen_word}"')
                    break
            print(f"Wrong guesses: {''.join(misses)}\n")
            print(display)
            if chosen_word == ''.join(display):
                print('You won \U0001F44F \U0001F396 \U0001F3C6!') 	 
                break
        ans = input('Do you want to play again? y = yes/n = no: ').lower()
        if ans == 'no' or ans == 'n':
            print('Goodbye \U0001F44B!')
            play = False
        else:
            os.system('cls || clear')


##################################################################################################

logo_highlow = '''
  ___ ___ .__       .__                   .____                               
 /   |   \|__| ____ |  |__   ___________  |    |    ______  _  __ ___________ 
/    ~    \  |/ ___\|  |  \_/ __ \_  __ \ |    |   /  _ \ \/ \/ // __ \_  __ \\
\    Y    /  / /_/  >   Y  \  ___/|  | \/ |    |__(  <_> )     /\  ___/|  | \/
 \___|_  /|__\___  /|___|  /\___  >__|    |_______ \____/ \/\_/  \___  >__|   
       \/   /_____/      \/     \/                \/                 \/       

'''

vs = '''
____   ____     
\   \ /   /_____
 \   Y   /  ___/
  \     /\___ \ 
   \___//____  >
             \/ 
             
'''

data = [
    {
    'name': 'Instagram',
    'follower_count': 346,
    'description': 'social media platform',
    'country': 'United States'
    },
    {
    'name': 'Cristiano Ronaldo',
    'follower_count': 215,
    'description': 'Footballer',
    'country': 'Portogal'
    },
    {
    'name': 'Ariana Grande',
    'follower_count': 183,
    'description': 'Musician and Actress',
    'country': 'United States'
    },
    {
    'name': 'Dwayne Johnson',
    'follower_count': 181,
    'description': 'Actor and Professional wrestler',
    'country': 'United States'
    },
    {
    'name': 'Kim Kardashian',
    'follower_count': 167,
    'description': 'Reality TV Personality and Businesswoman',
    'country': 'United States'
    },
    {
    'name': 'Lionel Messi',
    'follower_count': 149,
    'description': 'Footballer',
    'country': 'Argentia'
    },
    {
    'name': 'Beyoncé',
    'follower_count': 145,
    'description': 'Musician',
    'country': 'United States'
    },
    {
    'name': 'Neymar',
    'follower_count': 138,
    'description': 'Footballer',
    'country': 'Brazil'
    },
    {
    'name': 'Kylie Jenner',
    'follower_count': 172,
    'description': 'Reality TV personality and businesswoman and self-made Billionaire',
    'country': 'United States'
    },
    {
    'name': 'Selena Gomez',
    'follower_count': 174,
    'description': 'Musician and Actress',
    'country': 'United States'
    },

]


def lowerHigher():
    '''This function provides two celebreties A and B and the 
       player is to say whether A has higher or lower followers than B
    '''
    global data
    data = data
    play = True

    while play:
        print(f'\nWelcome to Lower - Higher Game\n{logo_highlow}')
        score = 0
        random.shuffle(data)
        for i in range(len(data) - 1):

            print(f'Compare A: {data[i]["name"]}, a {data[i]["description"]}, from {data[i]["country"]}\n{vs}')
            print(f'Against B: {data[i+1]["name"]}, a {data[i+1]["description"]}, from {data[i+1]["country"]}\n')

            ans = input('Is A\'s number of followers "lower" or "higher"?: ').lower()
            if ans == 'lower' and (data[i]['follower_count'] < data[i+1]['follower_count']):
                score += 1
                print("\nThat's correct \U0001F60A...!")
                print(f'Your current score is = {score}')
            elif ans == 'higher' and (data[i]['follower_count'] > data[i+1]['follower_count']):
                score += 1
                print("\nThat's correct \U0001F60A...!")
                print(f'Your current score is = {score}')
            else:
                print("\nSorry! That's not correct \U0001F620...!")
                break

        print(f'Your final score is = {score}')
        ans = input('Do you want to play again? yes/no: ').lower()
        if ans == 'no' or ans == 'n':
            play = False
        else:
            os.system('cls || clear')

###############################################################################################


logo_rps = '''
                _                                         _                        
               | |                                       (_)                       
 _ __ ___   ___| | ___ __   __ _ _ __   ___ _ __ ___  ___ _ ___ ___  ___  _ __ ___ 
| '__/ _ \ / __| |/ / '_ \ / _` | '_ \ / _ \ '__/ __|/ __| / __/ __|/ _ \| '__/ __|
| | | (_) | (__|   <| |_) | (_| | |_) |  __/ |  \__ \ (__| \__ \__ \ (_) | |  \__ \\
|_|  \___/ \___|_|\_\ .__/ \__,_| .__/ \___|_|  |___/\___|_|___/___/\___/|_|  |___/
                    | |         | |                                                
                    |_|         |_|                                                
'''

def rockPaperScissors():
    '''This is a rock-paper-scissors game where
       the user plays against the computer.
    '''
    print(f'\nWelcome to Rock-Paper-Scissors Game\n{logo_rps}')
    choices = ['rock', 'paper', 'scissors']
    win_player = 0
    win_computer = 0
    tie = 0

    while True:
        computer = random.choice(choices)
        player = input(f'Enter your choice from {choices}: ').lower()
        if player not in choices:
            print('Your choices is not among the allowed options...')
            player = input(f'Enter your choice from {choices}: ').lower()
        if player == 'rock' and computer == 'scissors':
            print('You win \U0001F60A!\n')
            win_player += 1
        elif player == 'paper' and computer == 'rock':
            print('You win \U0001F60A!\n')
            win_player += 1
        elif player == 'scissors' and computer == 'paper':
            print('You win \U0001F60A!\n')
            win_player += 1
        elif player == computer:
            print('It\'s a tie\n')
            tie += 1
        else:
            print(f'You chose {player} and the computer chose {computer}')
            print('Computer wins \U0001F631!\n')
            win_computer += 1
        play = input('Do you wish to continue? y = yes/n = no: ').lower()
        if play == 'no' or play == 'n':
            os.system('cls || clear')
            break

    print('----------')
    print(f'You won {win_player} time(s)')
    print(f'Computer won {win_computer} time(s)')
    print(f'You tied {tie} time(s)')


########################################################################################################


logo_blkjack = '''
                  
            .------.                         
            |A_  _ |                      
            |( \/ )|-----.     
            | \  / | /\  |
            |  \/ A|/  \ |
            `-----+'\  / |                              
                   | \/ A|  
                   `-----'            
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                    _/ |                
                    |__/

'''

def blackJack21():
    '''This is a Black Jack 21 game where the player tries to beat the dealer.

       How to beat the dealer:
       - By drawing a hand value that is higher than the dealer's hand value
       - By the dealer drawing a hand value that goes over 21.
       - By drawing a hand value of 21 on your first two cards, when the dealer does not.
       - The dealer will keep drawing cards as along as his hand value is less than 17

       How the dealer beats you: 
       - Your hand value exceeds 21.
       - The dealers hand has a greater value than yours at the end of the round

       How to find a hand's total value:
       - 2 through 10 count at face value, i.e. a 2 counts as two, a 9 counts as nine.
       - Face cards (J, Q, K) count as 10.
       - Ace can count as a 1 or an 11 depending on which value helps the hand the most.
    '''
    print(f'\nWelcome to Black Jack 21\n{logo_blkjack}')
    win_player = 0
    win_dealer = 0
    tie = 0

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    resume = True
    max_rounds = 100
    while resume:
        dealer = random.choices(cards, k = 2)
        player = random.choices(cards, k = 2)

        print(f'Player: {player}, sum = {sum(player)}\n')
        if len(player) == 2 and sum(player) < 21:
            add_card = input('Do you want to add a card? y = yes/n = no: ').lower()
            if add_card == 'yes' or add_card == 'y':
                player += [random.choice(cards)]

        while sum(dealer) < 17:
            dealer += [random.choice(cards)]
        print(f'Player: {player}, sum = {sum(player)}')
        print(f'Dealer: {dealer}, sum = {sum(dealer)}')

        if (sum(player) == 21 and sum(dealer) != 21) or (sum(player) > sum(dealer) 
                                                        and sum(player) < 21) or (sum(player) < 21 and sum(dealer) > 21):
            print('You won \U0001F60A \U0001F3C6!')
            win_player += 1
        elif sum(player) == sum(dealer):
            print("It's a tie!")
            tie += 1
        else:
            print('You Burst \U0001F620!')
            win_dealer += 1
            
        play = input('Do you wish to continue? y = yes/n = no: ').lower()
        if play == 'no' or play == 'n':
            print('Goodbye \U0001F44B!')
            resume = False
        else:
            max_rounds -= 1
        if max_rounds == 0:
            resume = False

    print('\n----------------')
    print(f'You won {win_player} times')
    print(f'Dealer won {win_dealer} times')
    print(f'You and dealer tie {tie} times')


#################################################################################################
