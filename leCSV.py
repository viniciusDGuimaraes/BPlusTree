#! /usr/bin/python3

import struct
import csv
from time import time
import cProfile

"""Converte os arquivos CSV em arquivos dat"""

ti = time()
#Define o formato da estrutura
estrutura = '2s30s14s50s6s2s'

#Cria a estrutura
s = struct.Struct(estrutura)

#Abre a planilha de Janeiro
f = open('201701_BolsaFamiliaFolhaPagamento.csv', encoding = 'cp1252')

#Escreve o dat da planilha de janeiro
t = open('BolsaFamiliaJan.dat', 'wb')
r = csv.reader(f)

i = 1

for linha in r:
	if i == 1:
		i += 1
		continue

	if i%1000000 == 0:
		print(i)

	i += 1

	info = linha[0].split('\t')

	if len(info[2]) < 30:
		info[2] = info[2] + ' ' * (30 - len(info[2]))

	if len(info[8]) < 50:
		info[8] = info[8] + ' ' * (50 - len(info[8]))

	if len(info[10]) < 6:
		info[10] = info[10] + ' ' * (6 - len(info[10]))

	t.write(s.pack(bytearray(info[0], encoding = 'cp1252'),
			         bytearray(info[2], encoding = 'cp1252'),
			         bytearray(info[7], encoding = 'cp1252'),
			         bytearray(info[8], encoding = 'cp1252'),
			         bytearray(info[10], encoding = 'cp1252'),
			         bytearray('\n', encoding = 'cp1252')))
t.close()

f = open('201702_BolsaFamiliaFolhaPagamento.csv', encoding = 'cp1252')

t = open('BolsaFamiliaFev.dat', 'wb')
r = csv.reader(f)

i = 1

for linha in r:
	if i == 1:
		i += 1
		continue

	if i%1000000 == 0:
		print(i)

	i += 1

	info = linha[0].split('\t')

	if len(info[2]) < 30:
		info[2] = info[2] + ' ' * (30 - len(info[2]))

	if len(info[8]) < 50:
		info[8] = info[8] + ' ' * (50 - len(info[8]))

	if len(info[10]) < 6:
		info[10] = info[10] + ' ' * (6 - len(info[10]))

	t.write(s.pack(bytearray(info[0], encoding = 'cp1252'),
			         bytearray(info[2], encoding = 'cp1252'),
			         bytearray(info[7], encoding = 'cp1252'),
			         bytearray(info[8], encoding = 'cp1252'),
			         bytearray(info[10], encoding = 'cp1252'),
			         bytearray('\n', encoding = 'cp1252')))
t.close()

print(time() - ti)
