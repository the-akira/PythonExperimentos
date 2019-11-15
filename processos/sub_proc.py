import subprocess

p1 = subprocess.run(['cat', 'output.txt'], capture_output=True, text=True)

#print(p1.stdout)

p2 = subprocess.run(['grep', '-n', 'Jupiter'], capture_output=True, text=True, input=p1.stdout)

#print(p2.stdout)

p3 = subprocess.run('cat output.txt | grep -n Jupiter', capture_output=True, text=True, shell=True)

print(p3.stdout)