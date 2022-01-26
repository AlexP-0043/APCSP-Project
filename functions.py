def guessing():
  str=hidden_word
  letter = input('> ')
  if str.find(letter) == 'true':
    print(f'Letter: {GREEN}{BOLD}{letter} + , is found within the letter')

def get_guess():
  guess = input("Guess: ").lower()
  return(guess)

def update_dashes(word, dashes, guess):
	for i in range(len(word)):
		if word[i] == guess:
			dashes = dashes[:i] + guess + dashes[i+1:]
			
	return dashes