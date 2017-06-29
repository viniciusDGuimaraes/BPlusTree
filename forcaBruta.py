#! /usr/bin/python

"""Compara uma versão reduzida da tabela de janeiro com a tabela de fevereiro
usando o método de força bruta"""

import struct
from time import time

ti = time()
estrutura = '2s30s14s50s6s2s'
s = struct.Struct(estrutura)
f1 = open('data/BolsaFamiliaJanReduzido.dat', 'rb')
f2 = open('data/BolsaFamiliaFev.dat', 'rb')
linha1 = f1.read(s.size)
existem = 0
naoExistem = 0
totalAcessos = 0
i = 0

#Roda ate o fim do arquivo de janeiro
while linha1 != b'':
	i += 1

	if i%1000 == 0:
		print(str(i//1000) + "%")
	dados1 = s.unpack(linha1)
	f2.seek(0)
	linha2 = f2.read(s.size)
	
	#Roda ate o fim do arquivo de fevereiro
	while linha2 != b'':
		totalAcessos += 1
		dados2 = s.unpack(linha2)
		
		#Adiciona mais um no contador, caso o NIS seja igual, para o loop
		if dados1[2] == dados2[2]:
			existem += 1
			break
		#Le a proxima linha, caso o NIS nao seja igual, e caso seja o final do arquivo, adiciona mais um ao contador
		else:
			linha2 = f2.read(s.size)
			if linha2 == b'':
				naoExistem += 1
				break

	linha1 = f1.read(s.size)

print("Quantidade de registros que existem nas duas tabelas: " + str(existem))
print("Quantidade de registros que so existem na tabela de janeiro: " + str(naoExistem))
print("Media de acessos: " + str(totalAcessos / 100000))
print(time()-ti)
