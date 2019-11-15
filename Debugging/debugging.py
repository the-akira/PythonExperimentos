import pdb

first = 'First'
second = 'Second'
pdb.set_trace()
result = first + second 
third = 'Third'
result += third 
print(result)

# import pdb
# pdb.set_trace 

# Também utilizado como:
# import pdb; pdb.set_trace

# Comandos comuns do pdb:
## l (list)
## p (print)
## n (next line)
## c (continue - finishes debugging)