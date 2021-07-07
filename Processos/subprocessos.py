import subprocess

with open('resultado.txt', 'w') as f:
    p1 = subprocess.run(['ls','-la'], stdout=f, text=True)

print(p1.args) # Argumentos
print(p1.returncode) # 0 -> Nenhum erro
print(p1.stdout) # Saída Padrão