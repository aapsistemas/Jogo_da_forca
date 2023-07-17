from replit import clear
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

lives = 6
from hangman_words import word_list
print(logo)
chosen_word = random.choice(word_list)

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += '_'
print(display)

end_of_game = False
while not end_of_game:

    guess = input('insira uma letra').lower()
    clear()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
          display[position] = letter

    if guess not in chosen_word:
        lives-= 1
        if lives == 0:
            end_of_game = True
            print('voce perdeu')
    print(display)

    if '_' not in display:
        end_of_game = True
        print('voce venceu')

    print(stages[lives])