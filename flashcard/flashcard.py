class Flashcard(object):
	def __init__(self, w, d, q, c, p):
		self.word = w;
		self.definition = d;
		self.numQuizzed = q;
		self.numCorrect = c;
		self.frequentlyWrong = p;
	
	def printargs(self):
		print(self.word);
		print(self.definition);
		print(self.numQuizzed);
		print(self.numCorrect);
		print(self.frequentlyWrong);
	
	def determineFrequentlyWrong(self):
		try:
			if float(self.numCorrect) / float(self.numQuizzed) < 0.5:
				self.frequentlyWrong = True;
			else:
				self.frequentlyWrong = False;
		except ZeroDivisionError:
			self.frequentlyWrong = False;
	
	def testing(self):
		print('the test was succesful');