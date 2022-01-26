def get_guess():
  while True:
    guess = input("Guess: ").lower()
    if len(guess) > 1:
      print('Only enter one character!')
      guess = input("Guess: ").lower()
    elif len(guess) < 1:
      print('Please enter a letter!')
      guess = input("Guess: ").lower()
    else:
      break
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