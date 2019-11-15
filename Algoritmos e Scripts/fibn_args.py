import argparse

def fib(n):
	a, b = 0, 1
	for i in range(n):
		a, b = b, a+b
	return a

def Main():
	parser = argparse.ArgumentParser()
	group = parser.add_mutually_exclusive_group()
	group.add_argument("-v", "--verbose", action="store_true")
	group.add_argument("-q", "--quiet", action="store_true")
	parser.add_argument("num", help="O número fibonacci que você deseja calcular", type=int)
	parser.add_argument("-o", "--output", help="Imprima o resultado em um arquivo", action="store_true")
	args = parser.parse_args()
	result = fib(args.num)

	if args.verbose:
		print("O "+str(args.num)+" número fibonacci é: "+str(result))
	elif args.quiet:
		print(result)
	else: 
		print("Fib("+str(args.num)+") = "+str(result))

	if args.output:
		f = open("fibonacci.txt", "a")
		f.write(str(result)+"\n")
		f.close()

if __name__ == '__main__':
	Main()