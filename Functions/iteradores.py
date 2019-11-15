# Classe Iteradora
class Sentence:

	def __init__(self, sentence):
		self.sentence = sentence
		self.index = 0
		self.words = self.sentence.split()

	def __iter__(self):
		return self

	def __next__(self):
		if self.index >= len(self.words):
			raise StopIteration
		index = self.index 
		self.index += 1
		return self.words[index]

sentenca = Sentence('isso é um teste muito interessante sobre iteradores')

for s in sentenca:
	print(s)

# print(next(sentenca))
# print(next(sentenca))
# print(next(sentenca))
# print(next(sentenca))
# print(next(sentenca))
# print(next(sentenca))

# Funcao Geradora
# def sentenca(sentence):
# 	for word in sentence.split():
# 		yield word

# sentenca_2 = sentenca('testando essa aqui')

# print(next(sentenca_2))
# print(next(sentenca_2))
