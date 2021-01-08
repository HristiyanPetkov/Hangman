word = input("Enter a word to guess: ")
word = list(word)
guess_word = ['_']*len(word)
lenght = len(word) - 2
lives = 8

guess_word[0] = word[0]
guess_word[len(guess_word) - 1] = word[len(word) - 1]

def print_word():
    for i in guess_word:
        print(i, end='')
    
while lives > 0:

    guess = input("Your guess: ")
    correct = 0
    print(lenght)
    
    for i in range(1, len(word) - 1):
        if guess == word[i]:
            lenght -= 1
            correct = 1
            guess_word[i] = word[i]

    if correct == 0:
        lives -= 1
        
    print_word()
    print()
    
    if lenght == 0:
        print("You guessed the word!")
        break
        
    print("Lives left: ", lives)
    