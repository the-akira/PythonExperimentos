import subprocess

# Executa o comando cat recebendo como argumento o arquivo 'output.txt'
p1 = subprocess.run(['cat', 'output.txt'], capture_output=True, text=True)
print(p1.stdout)

# Executa o comando 'grep -n Júpiter' na saída de 'p1'
p2 = subprocess.run(['grep', '-n', 'Júpiter'], capture_output=True, text=True, input=p1.stdout)
print(p2.stdout)

# Executa o comando 'cat output.txt | grep -n Júpiter' 
p3 = subprocess.run('cat output.txt | grep -n Júpiter', capture_output=True, text=True, shell=True)
print(p3.stdout)