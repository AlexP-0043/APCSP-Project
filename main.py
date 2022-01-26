from functions import update_dashes
from functions import get_guess
import random as r
RED = "\u001b[31;1m"
GREEN = "\u001b[32;1m"
BOLD = "\033[1m"
wordlist = ['apple','banana','orange','yellow','word','tree','red','easy','medium','computer','science','mathematics','console','difficult']
hidden_word = r.choice(wordlist)
guessed = []
tries = len(hidden_word)
dashes = print('_' * len(hidden_word))
guess = get_guess()
dashes = update_dashes(hidden_word, dashes, guess)

if guess in hidden_word and guess not in guessed:
  print(f'Letter: {guess}, is in the word.')
  guessed.append(guess)
elif guess in guessed:
  print('You have already inputed this letter')
elif guess not in hidden_word and guess not in guessed:
  print(f'Letter: {guess}, is not in the word')
