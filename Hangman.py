import random 
word = ["APPLE","CSK","BMW","DOG","NVIDIA"]
secret_word = random.choice(word)

guessed_letters = []
lives = 6
while lives >0:
    hidden_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            hidden_word += letter
        else:
            hidden_word += "_ "
            
    print(hidden_word)
    guess = input("Enter the letter :").upper()
   
    if guess in secret_word:
        guessed_letters.append(guess)
        print(guessed_letters)
        print("Correct")
    else :
        lives = lives-1 
        print("Wrong")
        print(guessed_letters)
        print("Remaning lives:",lives)

    # WIN condition
    if all(letter in guessed_letters for letter in secret_word):
        print("You Win The Game")
        print(secret_word)
        break

if lives == 0:
        print("You lose the game ")
        print(secret_word)