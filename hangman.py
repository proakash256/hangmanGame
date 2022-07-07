import hangmanArt
import wordList
import random

print(hangmanArt.logo)
chosen_word = random.choice(wordList.word_list)
print(f'\nPssst, the solution is {chosen_word}.')
lives = 7
l1 = []
for _ in range(len(chosen_word)):
    l1.append('_')
for i in l1:
    print(i, end=" ")
word_length = len(chosen_word)

while True:
    guess = input("\n\nGuess a letter: ").lower()

    if guess not in chosen_word:
        print(f"Sorry!! Wrong Answer, You have {lives} lives left.")
        print(hangmanArt.stages[lives - 1])
        lives -= 1
    if lives == 0:
        print("You Lose!!")
        break
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            l1[position] = letter
    for i in l1:
        print(i, end=" ")
    if "_" not in l1:
        print("\nYou win!!.")
        break
