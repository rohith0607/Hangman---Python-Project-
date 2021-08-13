from words import words
import random,string

def get_valid_word(words):
    word = ' '
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print(f"You have {lives} lives, You have used these letters: {' '.join(used_letters)}")
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ',' '.join(word_list))
        
        user_input = input('Guess a letter: ').upper()
        if user_input in alphabet - used_letters:
            used_letters.add(user_input)

            if user_input in word_letters:
                word_letters.remove(user_input)
            else:
                print('you lost a life')
                lives -= 1

        elif user_input in used_letters:
            print('You have already used that character. Please try again')

        else:
            print('You didnt type in correct character')

    if lives == 0:
        print(f'you lost, the word is {word}')
    else: print(f'you win, the word is {word}')


hangman()
