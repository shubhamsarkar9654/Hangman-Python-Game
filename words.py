
import random
import string

def random_word():
	word_list=['Navgurukul','heartfull','kind']
	secret_word=random.choice(word_list)
	secret_word=secret_word.lower()
	return secret_word