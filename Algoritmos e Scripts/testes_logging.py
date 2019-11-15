import logging

'''
Propósito: Registrar progresso e problemas 
Níveis: Debug, Info, Warning, Error, Critical

Nível    | Valor Numérico
NOTSET   | 0
DEBUG    | 10
INFO     | 20
WARNING  | 30
ERROR    | 40 
CRITICAL | 50
'''

# Criando e configurando um logger
FORMATO_LOG = "%(levelname)s %(asctime)s - %(message)s"

# filemode = 'w' altera o modo padrão de append para write
logging.basicConfig(filename = "/home/talantyr/Documentos/Projetos/Python/Algoritmos/teste.Log", level = logging.DEBUG, format = FORMATO_LOG)
logger = logging.getLogger()

# Testando o Logger
logger.info("Nossa primeira mensagem")

print(logger.level)