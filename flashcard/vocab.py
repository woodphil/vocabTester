#custom classes
from flashcard import *
from states import *

#standard python libraries
from string import *
from random import choice
import csv


diction = [];
problems = [];

with open('truevocab.txt', 'r') as raw:
	csvread = csv.reader(raw, delimiter='	');
	for row in csvread:
		temp = Flashcard(row[0], row[1], False);
		diction.append(temp);
#swap to writer later to allow additional words

#main loop
#print('get rdy for vocab. type iamscrub to exit\n');

#closing loop

def main():
	intro = IntroState();
	c = 1;

	while True:
		rando = choice(diction);
		ans = input(rando.word+'\n');
		print(rando.definition+'\n');
		
		if ans == 'iamscrub':
			break;
		
		next = input('got it right? y/n\n');
		
		if next is 'n':
			problems.append(rando);
		
		c = c+1;
		
		if c == 10:
			break;


if __name__ =="__main__":
	main();












