class Flashcard(object):
	def __init__(self, w, d, m):
		self.word = w;
		self.definition = d;
		self.mark = m;
	
	def printargs(self):
		print(self.word);
		print(self.definition);
		print(self.mark);
	
	def testing(self):
		print('the test was succesful');