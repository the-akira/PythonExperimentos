import unittest

def sum_digits(n):
	return sum(int(x) for x in str(n))

def digits_sum(n):
    results = 0
    while n > 0:
        remainder = n % 10
        results += remainder
        n = (n-remainder)/10
    return int(results)

def digitos(n):
	if n < 0:
		return "Número deve ser positivo"
	num = list(str(n))
	while len(num) != 1:
		n = [int(x) for x in num]
		num = sum(n)
		num = list(str(num))
	return int(num[0])

class Test(unittest.TestCase):
	def test_digitos(self):
		self.assertEqual(digitos(38), 2)
		self.assertEqual(digitos(255), 3)
		self.assertEqual(digitos(-33), "Número deve ser positivo")

#print(sum_digits(38))
#print(digits_sum(38))
#print(digitos(38))
#print(digitos(-33))

if __name__ == '__main__':
    unittest.main()