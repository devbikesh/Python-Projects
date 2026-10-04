import random
words=["python","computer","security","network","hacker"]
while True:
   secret_word=random.choice(words)
   hidden_word=[]
   for character in secret_word:
       hidden_word.append("_")
       guessed_letters=[]
       attempts_left=6
       print("Welcome to Hangman!")
     
