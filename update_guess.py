def update_dashes(hidden_word, dashes, guess):
	for i in range(len(hidden_word)):
		if hidden_word[i] == guess:
			dashes = dashes[:i] + guess + dashes[i+1:]
			
	return dashes