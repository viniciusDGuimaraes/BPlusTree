#! /usr/bin/python

import struct
import os
from time import time

ti = time()
estrutura = '2s30s14s50s6s2s'
s = struct.Struct(estrutura)
f1 = open('data/BolsaFamiliaJanOrdenado.dat', 'rb')
f2 = open('data/BolsaFamiliaFevOrdenado.dat', 'rb')
linha1 = f1.read(s.size)
existem = 0
naoExistem = 0
i = 1

while linha1 != b'':
	if i%10000 == 0:
		print(str(i//10000) + "%")
	
	inicio = 0
	fim = os.path.getsize('data/BolsaFamiliaFevOrdenado.dat') // s.size
	meio = (inicio + fim) // 2
	dados1 = s.unpack(linha1)
	
	while inicio <= fim:
		f2.seek(meio * s.size)
		linha2 = f2.read(s.size)
		dados2 = s.unpack(linha2)
		if int(dados1[2]) == int(dados2[2]):
			existem += 1
			break
		elif int(dados1[2]) < int(dados2[2]):
			fim = meio - 1
			meio = (inicio + fim) // 2
		else:
			inicio = meio + 1
			meio = (inicio + fim) // 2
	
	if inicio > fim:
		naoExistem += 1
	
	i += 1
	linha1 = f1.read(s.size)

print('Quantidade de registros que existem nas duas tabelas: ' + str(existem))
print('Quantidade de registros que so existem na tabela de janeiro: ' + str(naoExistem))
print(time() - ti)
