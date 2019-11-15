import subprocess

# subprocess.run('ls -la', shell=True)
# p1 = subprocess.run(['ls','-la'], capture_output=True, text=True)
with open('output.txt', 'w') as f:
	p1 = subprocess.run(['ls','-la'], stdout=f, text=True)

print(p1.args) # Argumentos
print(p1.returncode) # 0 -> Nenhum erro
print(p1.stdout) # Saída Padrão