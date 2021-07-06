# Definindo uma classe iteradora
class Sentence:
    def __init__(self, sentença):
        self.sentença = sentença
        self.index = 0
        self.palavras = self.sentença.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.palavras):
            raise StopIteration
        index = self.index 
        self.index += 1
        return self.palavras[index]

sentença = Sentence('isso é um teste muito interessante sobre iteradores')
for s in sentença:
    print(s)

s = Sentence('esta é uma nova sentença')
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))

# Definindo uma função geradora
def sentence(sentence):
    for palavra in sentence.split():
        yield palavra

sent = sentence('testando uma nova sentença')
print(next(sent))
print(next(sent))
print(next(sent))
print(next(sent))