"""
Um quine é um programa de computador que não recebe nenhuma entrada 
e produz uma cópia de seu próprio código-fonte como sua única saída. 

Os termos padrão para esses programas na teoria da computabilidade 
e na literatura da ciência da computação são "programas autorreplicantes"
"""

print((lambda s:s%s)('print((lambda s:s%%s)(%r))'))