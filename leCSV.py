#! /usr/bin/python3

import struct
import csv
from time import time

ti = time()

#Define o formato da estrutura
estrutura = '2s30s14s50s6s2s'

#Cria a estrutura
s = struct.Struct(estrutura)

#Abre a planilha de Janeiro
print('Abrindo a planilha de janeiro')
f = open('201701_BolsaFamiliaFolhaPagamento.csv', encoding = 'cp1252')

#Escreve o dat da planilha de janeiro
print('Criando o arquivo dat de janeiro')
t = open('BolsaFamiliaJan.dat', 'wb')
print('Lendo a planilha')
r = csv.reader(f)

i = 1

for linha in r:
	if i == 1:
		i += 1
		continue
	
#	if i > 11:
#		break

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

#Abre a planilha de Fevereiro
print('Abrindo a planilha de fevereiro')
f = open('201702_BolsaFamiliaFolhaPagamento.csv', encoding = 'cp1252')

#Escreve o dat da planilha de fevereiro
print('Criando o arquivo dat de fevereiro')
t = open('BolsaFamiliaFev.dat', 'wb')
print('Lendo a planilha')
r = csv.reader(f)

i = 1

for linha in r:
	if i == 1:
		i += 1
		continue

#	if i > 11:
#		break

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
	info = linha[0].split('\t')
	t.write(s.pack(bytearray(info[0], encoding = 'cp1252'),
                   bytearray(info[2], encoding = 'cp1252'),
                   bytearray(info[7], encoding = 'cp1252'),
                   bytearray(info[8], encoding = 'cp1252'),
                   bytearray(info[10], encoding = 'cp1252'),
                   bytearray('\n', encoding = 'cp1252')))

t.close()

print(time()-ti)
