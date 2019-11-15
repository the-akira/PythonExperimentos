class A:
	def feature1(self):
		print('Feature 1 Working')
	def feature2(self):
		print('Feature 1 Working')

class B(A):
	def feature3(self):
		print('Feature 1 Working')
	def feature4(self):
		print('Feature 1 Working')

# Multipla Herança
class C(B):
	def feature5(self):
		print('Feature 1 Working')

a1 = A()

a1.feature1()

b1 = B()

b1.feature1()

c1 = C()

c1.feature1()