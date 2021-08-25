import random

logo = ''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/  '''

# ASCII art for stages of hangman
stages =  [
     '''
      _______
     |/      |
     |      (_)
     |      \|/
     |      / \\
     |
    _|___''',
    ''' _______
     |/      |
     |      (_)
     |      \|/
     |      / 
     |
    _|___''',
    ''' _______
     |/      |
     |      (_)
     |      \|/
     |      
     |
    _|___''',
    '''_______
     |/      |
     |      (_)
     |      \|
     |      
     |
    _|___''',
    ''' _______
     |/      |
     |      (_)
     |       |
     |       
     |
    _|___''',
    ''' _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
    _|___'''
]

# Few sample words
word_list = [
"ability",
"able",
"about",
"above",
"accept",
"according",
"account",
"across",
"act",
"action",
"activity",
"actually",
"add",
"address",
"administration",
"admit",
"adult",
"affect",
"after",
"again",
"against",
"age",
"agency",
"agent",
"ago",
"agree",
"agreement",
"ahead",
"air",
"all",
"allow",
"almost",
"alone",
"along",
"already",
"also",
"although",
"always"
]

#Get a random word
word_to_guess = random.choice(word_list)
word_length = len(word_to_guess)

#Add _ to the word
word_with_blanks = []
for _ in range(word_length):
    word_with_blanks += '_'

print(logo)
print("\n\nWord to guess: " + str(word_with_blanks) + "\n")

game_run = True
attempts = 5

while attempts >= 0:
    #clear()
    guess = input("\n\nGuess a word: ").lower()
    
    if guess in word_to_guess:
        if guess in word_with_blanks:
            print(f"Letter {guess} is already guessed..")
            print(stages[attempts])
        else:
            for position in range(word_length):
                if word_to_guess[position] == guess:
                    word_with_blanks[position] = guess
        print(word_with_blanks)
    else:
        print(f"Letter {guess} is not present, please continue..")
        print(stages[attempts])
        attempts -= 1

    if attempts == -1:
        print("\n\nYou Lose")
        print("Word is: ", word_to_guess)
    elif '_' not in word_with_blanks:
        attempts = -1 
        print("\n\nYou Win!")
              

