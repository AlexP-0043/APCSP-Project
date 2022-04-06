import random as r
wordlist = ['apple','banana','orange','yellow','word','tree','red','easy','medium','computer','science','mathematics','console','difficult','word','kill','treehouse','computer','python','code','alphabet','default','skill','list','guess','progessive','english','spanish','college','school','university']
templist = ['hello', 'goodbye']
guessed = []
print('''
Welcome to the Guessing Game!

Instructions: Only enter one letter per guess, don't enter symbols or fancy letters, and don't cheat.
''')
def guessing_game(word):   
  tries = len(word) * 2
  hidden_word = "-" * len(word)
  print("This is the hidden word " + hidden_word)
  while(hidden_word != word):
    user_input = input("Guess a letter: ")
    if (tries < 0):
      print('\n')
      print('You have failed to guess the word')
      print(f'The word was "{word}".')
      break
    elif (user_input in guessed):
      print('\n')
      print(f'You have already guessed {user_input}.')
      print(f'Guessed letters: {guessed}.')
    if (user_input in word):
      occurences = find(word, user_input)
      for index in occurences:
        hidden_word = hidden_word[:index] + user_input + hidden_word[index + 1:]
        print('\n')
        print(f'Letter: {user_input}, is in the word.')
        guessed.append(user_input)
        print(hidden_word)
        print(f'Guessed letters: {guessed}.')

    else:
        if (user_input in guessed):
            print('') # prevents another wrong from previously guessed
        else:
          print('\n')
          print(f'Letter: {user_input}, is not in the word.')
          print(f'You have {tries} attempts to complete the word.')
          print(hidden_word)
          guessed.append(user_input)
          print(f'Guessed letters: {guessed}.')
          tries -= 1

    if (hidden_word == word):
      print('\n')
      print(f'You found the word! The word was "{hidden_word}".')
      print(f'With {tries} attempts to complete the word.')
def find(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

guessing_game(r.choice(wordlist))

