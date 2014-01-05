class VocabState():
	def __init__(self):
		pass;
	def handleInput():
		pass;
	def changeState():
		pass;

		
class IntroState(VocabState):

	def __init__(self):
		print('get rdy for vocab. \n 1: start quiz\n 2: exit\n');
	
	def handleInput(self, input):
		if input is '1':
			print('quiz selected. \n')
			return 1;
		elif input is '2':
			print('exiting');
			return 2;
		else:
			print('invalid input\n ')
			return 3;

from random import choice, randint

class QuizState(VocabState):

	def __init__(self, d):
		print('quiz time \n');
		self.dictionary = d;
		self.questionCounter = 0;
		self.questionsRight = 0;
		self.rightChoice = 0;
		self.questionWord = None;
		self.generateQuestion()
		
	def generateQuestion(self):
		self.questionCounter += 1;
		self.questionWord = choice(self.dictionary);
		self.questionWord.numQuizzed += 1;
		print(self.questionWord.word+'\n');
		
		#determine placement of correct option
		self.rightChoice = randint(1,5);
		
		#generate incorrect options
		wrongChoices = [];
		while len(wrongChoices) != 4:
			tempChoice = choice(self.dictionary);
			if tempChoice.definition is not questionWord.definition:
				wrongChoices.append(tempChoice);
		
		#format the choices
		for i in range(1,6):
			if i == self.rightChoice:
				print('\t {0}: {1}\n'.format(i,questionWord.definition))
			else:
				print('\t {0}: {1}\n'.format(i,wrongChoices.pop().definition))
		
		
	def handleInput(self, i):
		input = self.convertStr(i);
		print(self.rightChoice);
		if input == self.rightChoice:
			self.questionWord.numCorrect += 1;
			self.questionsRight = self.questionsRight + 1;
			print('correct \n');
		else:
			print('incorrect \n');
		
		#when max questions is reached, terminate the loop
		if self.questionCounter != 10:
			self.generateQuestion();
			return 1;
		else:
			print('quiz completed, you got {}/10 right \n'.format(self.questionsRight))
			return 2;
			
	#handles conversion of user input into processable data	
	def convertStr(self, s):
		while True:
			try:
				num = int(s)
				#if valid number but not a valid choice
				if num>5 or num<1:
					print("invalid input");
					s = input('choose again: ');
				else:
					return num;
			except ValueError:
				print("invalid input");
				s = input('choose again: ');
			
		
		
		
		
		
		
		
		
		
		
	
	