# Hangman Challenge Program

import random

print("Welcome to the Hangman Challenge!")

word_list = ['Udoy', 'Dipty', 'Ashma', 'Hamim']
display_word = []

for letter in word_list:
    display_word += '-'
    print(display_word)

random_word = random.choice(word_list)
print(random_word)

print('You get 5 guesses')

num = 0
game_over = False

while not game_over:
    guess = input("Guess the letter? ").lower()

    for position in range(len(random_word)):
        letter = random_word[position]
        if letter == guess:
            display_word[position] = letter
            print('Right!')
        else:
            print('Wrong!')
    
    if guess not in random_word:
        num += 1
        guesses_left = 5 - num
        print(guesses_left)

        if num >= 5:
            print('You loser')
            game_over = True

    print(display_word)

    if '-' not in display_word:
        print('You win')
        game_over = True