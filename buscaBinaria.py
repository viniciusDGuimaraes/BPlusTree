#! /usr/bin/python

"""Acessa cada entradada da tabela de janeiro e usa o método de busca binária em
uma versão ordenada da tabela de fevereiro para checar se a mesma entrada existe
nesta tabela."""

import struct
import os
from math import ceil
from time import time

ti = time()
estrutura = '2s30s14s50s6s2s'
s = struct.Struct(estrutura)
f1 = open('data/BolsaFamiliaJan.dat', 'rb')
f2 = open('data/BolsaFamiliaFevOrdenado.dat', 'rb')
linha1 = f1.read(s.size)
existem = 0
naoExistem = 0
totalAcessos = 0

while linha1 != b'':
	inicio = 0
	fim = os.path.getsize('data/BolsaFamiliaFevOrdenado.dat') // s.size
	meio = int((inicio + fim) / 2)
	f2.seek(meio * s.size)
	linha2 = f2.read(s.size)
	dados1 = s.unpack(linha1)
	
	while inicio <= fim and linha2 != b'':
		dados2 = s.unpack(linha2)
		totalAcessos += 1

		if int(dados1[2]) == int(dados2[2]):
			existem += 1
			break
		elif int(dados1[2]) < int(dados2[2]):
			fim = meio - 1
			meio = ceil((inicio + fim) / 2)
		else:
			inicio = meio + 1
			meio = ceil((inicio + fim) / 2)

		f2.seek(int(meio * s.size))
		linha2 = f2.read(s.size)
	
	if inicio > fim or linha2 == b'':
		naoExistem += 1

	linha1 = f1.read(s.size)

print('Quantidade de registros que existem nas duas tabelas: ' + str(existem))
print('Quantidade de registros que so existem na tabela de janeiro: ' + str(naoExistem))
print('Media de acessos: ' + str(totalAcessos / 13601764))
print(time() - ti)
