class Student:

	school = 'Gabriel'

	def __init__(self, m1, m2, m3):
		self.m1 = m1
		self.m2 = m2
		self.m3 = m3

	def avg(self):
		return (self.m1 + self.m2 + self.m3) / 3

	def get_m1(self):
		return self.m1

	def set_m1(self, value):
		self.m1 = value

	@classmethod
	def info(cls):
		return cls.school

	@staticmethod
	def escola():
		print(f'Escola que você estuda é Gabriel')

s1 = Student(6,3,10)
s2 = Student(3,10,7)
print(s1.avg())
print(s1.get_m1())
print(s2.avg())
print(Student.info())
print(s1.info())
Student.escola()