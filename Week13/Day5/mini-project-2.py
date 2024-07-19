import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist) 

guessed = []
body_parts = ['head', 'body', 'right arm', 'left arm', 'right leg', 'left leg']
incorrect = -1
gallows = []

word_to_guess = "*" * len(word)

# print(list(word))
# for c in enumerate(word):
#     print(c)

def get_guess():
    while True:
        guess = input("Guess a letter: ")

        if guess in guessed:
            print("letter already guessed. enter another")
        else:
            return guess


while word != word_to_guess and gallows != body_parts:
   print("Word to guess: ", word_to_guess)
   print("Gallows: ",  gallows)

   guess = get_guess()

   if guess in word:
        for pos, char in enumerate(word):
            if char == guess:
                word_to_guess = word_to_guess[:pos] + char + word_to_guess[pos+1:]
   else:
        print("Letter not in word")
        incorrect +=1
        gallows.append(body_parts[incorrect])

if word_to_guess == word:
    print("You won!")
else:
    print("Gallows: ",  gallows)
    print("Too many guesses. You lost")
    
