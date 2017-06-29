#! /usr/bin/python3

import struct
import os
from operator import itemgetter
from time import time

"""Faz o merge externo da tabela de fevereiro"""

ti = time()
estrutura = '2s30s14s50s6s2s'
s = struct.Struct(estrutura)
f = open('data/BolsaFamiliaFev.dat', 'rb')
n = 0
linha = f.read(s.size)
tamanho = 100000
printed = False

#Roda até o EOF
while linha != b'':
	k = 0

	#Zera a lista
	listaDeEntradas = []

	#Adiciona até 100000 arquivos na lista
	while k < tamanho and linha != b'':
		k += 1
		dados = s.unpack(linha)
		listaDeEntradas.append(dados)
		linha = f.read(s.size)

	#Organiza a lista pelo cep
	listaDeEntradas.sort(key=itemgetter(2))
	
	#Adiciona mais um ao contador
	n += 1

	#Usa o contador para criar um arquivo com nome único
	nF = open('BolsaFamiliaFev' + str(n) + '.dat', 'ab')

	#Escreve uma mensagem caso ela não tenha sido escrita antes
	if printed == False:
		print('Escrevendo arquivos')
		printed = True

	#Itera a lista e escreve cada entrada no novo arquivo criado
	for i in range(k):
		nF.write(s.pack(listaDeEntradas[i][0],
                        listaDeEntradas[i][1],
                        listaDeEntradas[i][2],
                        listaDeEntradas[i][3],
                        listaDeEntradas[i][4],
                        listaDeEntradas[i][5]))
	nF.close()

n = 1

#Roda o loop até que o contador aponte para o arquivo 1 e não exista um arquivo vizinho
while n != 1 or os.path.isfile('BolsaFamiliaFev' + str(n + 1) + '.dat'):
	#Confere se existe um par de arquivos
	if os.path.isfile('BolsaFamiliaFev' + str(n) + '.dat') and os.path.isfile('BolsaFamiliaFev' + str(n + 1) + '.dat'):
		#print('Unindo'BolsaFamiliaFev' + str(n) + '.dat e'BolsaFamiliaFev' + str(n + 1) + '.dat')

		#Abre o arquivo impar
		f1 = open('BolsaFamiliaFev' + str(n) + '.dat', 'rb')
		linha1 = f1.read(s.size)

		#Abre o arquivo par
		f2 = open('BolsaFamiliaFev' + str(n + 1) + '.dat', 'rb')
		linha2 = f2.read(s.size)

		#Cria um arquivo para armazenar o merge dos dois arquivos abertos
		f3 = open('placeholder.dat', 'ab')

		#Roda até chegar no EOF de um desses arquivos
		while linha1 != b'' and linha2 != b'':
			dados1 = s.unpack(linha1)
			dados2 = s.unpack(linha2)

			#Escreve a entrada com menor cep no placeholder.dat
			if dados1[2] < dados2[2]:
				f3.write(s.pack(dados1[0],
                                dados1[1],
                                dados1[2],
                                dados1[3],
                                dados1[4],
                                dados1[5]))
				linha1 = f1.read(s.size)
			else:
				f3.write(s.pack(dados2[0],
                                dados2[1],
                                dados2[2],
                                dados2[3],
                                dados2[4],
                                dados2[5]))
				linha2 = f2.read(s.size)

		#Se o arquivo impar não chegou ao fim, escreve o resto de suas entradas
		while linha1 != b'':
			dados1 = s.unpack(linha1)
			f3.write(s.pack(dados1[0],
                            dados1[1],
                            dados1[2],
                            dados1[3],
                            dados1[4],
                            dados1[5]))
			linha1 = f1.read(s.size)

		#Se o arquivo par não chegou ao fim, escreve o resto de suas entradas
		while linha2 != b'':
			dados2 = s.unpack(linha2)
			f3.write(s.pack(dados2[0],
                            dados2[1],
                            dados2[2],
                            dados2[3],
                            dados2[4],
                            dados2[5]))
			linha2 = f2.read(s.size)

		#Fecha o placeholder
		f3.close()

		#Remove o arquivo impar
		os.remove('BolsaFamiliaFev' + str(n) + '.dat')

		#Remove o arquivo par
		os.remove('BolsaFamiliaFev' + str(n + 1) + '.dat')

		#Renomeia o placeholder
		os.rename('placeholder.dat', 'BolsaFamiliaFev' + str((n + 1) // 2) + '.dat')

		#Adiciona mais 2 ao contador para pegar o próximo arquivo impar
		n += 2
	else:
		#Confere se esse arquivo impar existe
		if os.path.isfile('BolsaFamiliaFev' + str(n) + '.dat') and n != 1:
			#Renomeia esse arquivo
			os.rename('BolsaFamiliaFev' + str(n) + '.dat', 'BolsaFamiliaFev' + str((n + 1) // 2) + '.dat')
		#print('Renomeando'BolsaFamiliaFev' + str(n) + '.dat para'BolsaFamiliaFev' + str((n + 1) // 2) + '.dat')

		#Reseta o contador para apontar para o primeiro arquivo
		n = 1

print(time() - ti)
