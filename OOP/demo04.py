# Classe Pai
class A:
    def feature1(self):
        print('Feature 1 Working')
    def feature2(self):
        print('Feature 2 Working')

# Classe Filha
class B(A):
    def feature3(self):
        print('Feature 3 Working')
    def feature4(self):
        print('Feature 4 Working')

# Multipla Herança
class C(B):
    def feature5(self):
        print('Feature 5 Working')

# Cria uma instância de A
a = A()
a.feature1()

# Cria uma instância de B
b = B()
b.feature1()

# Cria uma instância de C
c = C()
c.feature1()