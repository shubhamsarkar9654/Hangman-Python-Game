import string
from random import randint
from images import image
from words import random_word

def get_word(guess_word,secret_word):
	word=""
	for letter in range(len(secret_word)):

		if secret_word[letter] in guess_word:
			word+=secret_word[letter]
		else:
			word+='_ '
	return word	
def Hint(secret_word):
	length=len(secret_word)
	no=randint(0,length-1)
	word=secret_word[no]
	return word


def hangman(secret_word):
	
	print('Welcome to play a Hangaman Game:\n ')
	print(''' A Hangman game is word choice game. Here a secret code of 8 letters and you
	have to find a secret code. In this game you will get 8 chance to find the right letters. 
	If you couldn't find the letter so the man will go hang and you lost the game:\n''')

	level=input('Which level do you want to play:\na) Easy\n b) Medium\n c) Hard\t')
	if level=='b':
		image_level=[1,2,4,5,6]
		gave_chance=5
	elif level=='c':
		image_level=[2,4,5,6]
		gave_chance=4
	else:
		gave_chance=7
		image_level=[0,1,2,3,4,5,6]

	guess_word=[]
	counter=0
	guess_chance=0
	hint_chance=0
	while True:
		value=''
		guess_letter=input('Guess a Letter by user:\n ')
		if guess_letter=='hint'and hint_chance==0:
			print(Hint(secret_word))
			hint_chance=1
			continue
		else:
			print('You have already used Hint ')
			
		guess_word.append(guess_letter)
		if guess_letter in secret_word:
			value=get_word(guess_word,secret_word)
			print('Good guess: ',value)

		else:
			guess_chance+=1
			show_image=image_level[counter]
			counter+=1
			print(image[show_image])
		if value==secret_word:
			print('You won the game!\n Thank you for playing! ')
			break
		elif (gave_chance-guess_chance)==0:
			print('You lost the game! secret code is=',secret_word)
			break

secret_word=random_word()
hangman(secret_word)






