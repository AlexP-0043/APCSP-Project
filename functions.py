def get_guess():
  guess = input("Guess: ").lower()
  return(guess)

def update_dashes(word, dashes, guess):
	for i in range(len(word)):
		if word[i] == guess:
			dashes = dashes[:i] + guess + dashes[i+1:]
			
	return dashes

def update_dashes(hidden_word, dashes, guess):
	for i in range(len(hidden_word)):
		if hidden_word[i] == guess:
			dashes = dashes[:i] + guess + dashes[i+1:]
	return dashes