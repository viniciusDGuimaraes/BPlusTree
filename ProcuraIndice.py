import struct
import hashlib
import os
from time import time

ti = time()
hashSize = 1000003
fileName = "data/BolsaFamiliaFev.dat"
indexName = "data/BolsaFamiliaJan-hash.dat"
dataFormat = "2s30s14s50s6s2s"
indexFormat = "14sLL"
keyColumnIndex = 2
existem = 0
naoExistem = 0
totalAcessos = 0
i = 0

dataStruct = struct.Struct(dataFormat)
indexStruct = struct.Struct(indexFormat)

def h(key):
    return int(hashlib.sha1(key).hexdigest(),16)%hashSize

f = open(fileName,"rb")

line = f.read(dataStruct.size)

while line != b'':
    i += 1
    if i%10000 == 0:
        print str(i / 10000) + "%"
    data = dataStruct.unpack(line)
    fi = open(indexName,"rb")
    p = h(data[2])
    offset = p*indexStruct.size
    while True:
        totalAcessos += 1
        fi.seek(offset,os.SEEK_SET)
        indexRecord = indexStruct.unpack(fi.read(indexStruct.size))
        if indexRecord[0] == data[2]:
            existem += 1
            break
        else:
            offset = indexRecord[2]
            if offset == 0:
                naoExistem += 1
                break
    line = f.read(dataStruct.size)
    fi.close()

print "Media de acessos: ", totalAcessos / float(1000000)
print "Quantidade de registros que existem nas duas tabelas: ", existem
print "Quantidade de registros que so existem na tabela de fevereiro: ", naoExistem
tf = time()
tt = tf - ti
print tt
