import random
from words import words
from hangman_visual import lives_visual_dict
from emoticons import dancer
import string

def get_valid_word(words):
    word = random.choice(words) #Randomly chooses something from the list

    while "-" in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #What user have guessed

    lives = 6

    #Get user input
    while len(word_letters)> 0 and lives > 0:
        # letter used

        print(lives_visual_dict[lives-1])

        print('You have ',lives, 'lives left')
        print('You have used :',' '.join(used_letters))

        #What the current word is with cencored un-guessed letters
        word_list = [letter if letter in used_letters else "_" for letter in word]
        print('Current word: ',' '.join(word_list))

        used_letter = input('Guess a letter: ').upper()

        if used_letter in alphabet - used_letters:
            used_letters.add(used_letter)
            if used_letter in word_letters:
                word_letters.remove(used_letter)

            else:
                lives = lives - 1 #Take away a life if wrong
                print("Letter is not in word.")

        elif used_letter in used_letters:
            print('You have already used that character. Please try again')

        else:
            print("Invalid character. Please try again")


    if lives == 0:
        print("You have died :')")
        print('The word is',word)
    else:
        print(dancer)
        print('You have guessed the word',word, '!!')

hangman()