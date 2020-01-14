# Word frequency counter
bob_speech = "I like Python and JavaScript since they can help you develop most projects. Python is one of the most popolar programming languages."

programming_languages = {}

#function to loop though the senstence and count how many times a word appears in a sentence

def word_frequency(bob_speech):
	programming_languages = {}
	for word in bob_speech.split():
		if word not in programming_languages:
			programming_languages[word] = 1
		else:
			programming_languages[word] = programming_languages[word] + 1
	return programming_languages
print(word_frequency(bob_speech))



	

	

