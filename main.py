import random as r
from subprocess import call
from os import name
#Imports
RED = "\u001b[31;1m"
GREEN = "\u001b[32;1m"
BOLD = "\033[1m"
NORMAL = "\u001b[0m"
#text stuff
wordlist = ['apple','banana','orange','yellow','word','tree','red','easy','medium','computer','science','mathematics','console','difficult','word','kill','treehouse','computer','python','code','alphabet','default','skill','list','guess','progessive','english','spanish','college','school','university']
#lists
guessed = []
#variables
def clear():
  call("clear" if name == "posix" else "cls", shell=True)
def guessing_game(word):   
  tries = len(word)
  hidden_word = "-" * len(word)
  print("This is the hidden word " + hidden_word)
  while(hidden_word != word):
    user_input = input("Guess a letter: ")
    if user_input in word and not guessed:
      occurences = find(word, user_input)
      for index in occurences:
        hidden_word = hidden_word[:index] + user_input + hidden_word[index + 1:]
        clear()
        print(f'Letter: {user_input}, is {GREEN}in{NORMAL} the word.')
        guessed.append(user_input)
        print(hidden_word)
    elif (tries == 0):
      clear()
      print('You have failed to guess the word')
      print(f'The word was "{word}".')
      break
    elif user_input in guessed:
      clear()
      print(f'You have already entered {user_input}')
      print(f'You have {tries} attempts to complete the word.')
      print(hidden_word)
    else:
      if user_input in guessed:
        clear()
        print(f'You have already entered {user_input}')
        print(f'You have {tries} attempts to complete the word.')
        print(hidden_word)
      else:
        clear()
        print(f'Letter: {user_input}, is {RED}not{NORMAL} in the word.')
        print(f'You have {tries} attempts to complete the word.')
        print(hidden_word)
        tries -= 1
    if hidden_word == word or user_input == word:
      clear()
      print(f'You found the word! The word was "{word}".')
      print(f'With {tries} attempts to complete the word.')
def find(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

guessing_game(r.choice(wordlist))

