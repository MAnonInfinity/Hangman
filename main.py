import random
import hangman_words
import hangman_art
import replit

print(hangman_art.logo)

stages = hangman_art.stages

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#print(f"The word is : {chosen_word}.")

display = ['_' for i in range(word_length)]
#print(display)
print(f"\n\n{' '.join(display)}\n\n")

lives = 6
print(stages[len(stages)-1])

while '_' in display:
    if lives == 0: #Lost
        print("You Died! Game Over!")
        break

    guess = input("Guess a letter: ").lower() 
    if guess in display: #Check Repetition
        print(f"You've already guessed {guess}")
      
    replit.clear() #Clear Screen

    for i in range(word_length): #Set the correct guess
        if chosen_word[i] == guess:
            display[i] = guess
            
    if guess not in chosen_word: #Punish
        print(f"{guess} is not in the word. Wrong Guess")
        lives -= 1

    print(f"\n{' '.join(display)}")
    print(f"\nLives = {lives}\n")
    print(stages[lives])


print(f"\nThe word was : {chosen_word}")

if '_' not in display and lives > 0: #Won
    print("You Win!")
