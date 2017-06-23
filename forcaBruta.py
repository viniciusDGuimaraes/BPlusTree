#! /usr/bin/python

import struct
from time import time

ti = time()
estrutura = '2s30s14s50s6s2s'
s = struct.Struct(estrutura)
f1 = open('BolsaFamiliaJan.dat', 'rb')
f2 = open('BolsaFamiliaFev.dat', 'rb')
linha1 = f1.read(s.size)
existem = 0
naoExistem = 0

#Roda ate o fim do arquivo de janeiro
while linha1 != b'':
	dados1 = s.unpack(linha1)
	linha2 = f2.read(s.size)
	
	#Roda ate o fim do arquivo de fevereiro
	while linha2 != b'':
		dados2 = s.unpack(linha2)
		
		#Adiciona mais um no contador, caso o NIS seja igual, volta para o comeco do arquivo e para o loop
		if dados1[2] == dados2[2]:
			existem += 1
			f2.seek(0)
			break
		#Le a proxima linha, caso o NIS nao for igual, e caso seja o final do arquivo, adiciona mais um ao contador
		else:
			linha2 = f2.read(s.size)
			if linha2 == b'':
				naoExistem += 1
				f2.seek(0)
				break

	linha1 = f1.read(s.size)

print("Quantidade de pessoas que existem nas duas tabelas: " + str(existem))
print("Quantidade de pessoas que existem na tabela de janeiro mas nao na de fevereiro: " + str(naoExistem))
print(time()-ti)
