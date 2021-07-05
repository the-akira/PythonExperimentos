import argparse

"""
Exemplos de uso:
python fib_args.py --num 6 -v
python fib_args.py -n 8
python fib_args.py -n 10 --quiet -o
"""

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")
    parser.add_argument("-n", "--num", help="O número fibonacci que você deseja calcular", type=int)
    parser.add_argument("-o", "--output", help="Imprima o resultado em um arquivo", action="store_true")
    args = parser.parse_args()
    result = fib(args.num)

    if args.verbose:
        print(f"O {str(args.num)}º número fibonnaci é {str(result)}")
    elif args.quiet:
        print(result)
    else: 
        print(f'fib({str(args.num)}) = {str(result)}')
    if args.output:
        f = open("fibonacci.txt", "a")
        f.write(str(result)+"\n")
        f.close()

if __name__ == '__main__':
    main()