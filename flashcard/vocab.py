#custom classes
from flashcard import *
from states import *

#standard python libraries
from string import *
from random import choice
import csv
import sys


diction = [];
problems = [];

with open('truevocab.txt', 'r') as raw:
	csvread = csv.reader(raw, delimiter='	');
	for row in csvread:
		temp = Flashcard(row[0], row[1], row[2], row[3], row[4]);
		diction.append(temp);
#swap to writer later to allow additional words

#main loop
#print('get rdy for vocab. type iamscrub to exit\n');

#closing loop

#main handles the states
def main():
	introProcess();

def introProcess():
	intro = IntroState();
	userChoice = 3;
	while userChoice == 3:
		userChoice = intro.handleInput(input());
		if userChoice == 1:
			quizProcess();
		elif userChoice == 2:
			exitProcess();
			sys.exit(0);

def quizProcess():
	quiz = QuizState(diction);
	userChoice = 1;
	while userChoice ==1:
		userChoice = quiz.handleInput(input());
		if userChoice ==2:
			introProcess();

def exitProcess():
	with open('truevocab2.txt', 'w', newline="") as csvfile:
		writa = csv.writer(csvfile, delimiter = '	')
		for i in diction:
			i.determineFrequentlyWrong();
			writa.writerow([i.word,i.definition,i.numQuizzed,i.numCorrect,i.frequentlyWrong]);
if __name__ =="__main__":
	main();












