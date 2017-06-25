import struct
import hashlib

hashSize = 1000003
fileName = "data/BolsaFamiliaJan.dat"
fileFormat = "2s30s14s50s6s2s"
keyColumnIndex = 2
recordSize = struct.calcsize(fileFormat)
counts = [0] * hashSize

def h2(key):
    global hashSize
    return int(key)%hashSize

def h(key):
    global hashSize
    return int(hashlib.sha1(key).hexdigest(),16)%hashSize


colisoes = 0
tamanhoMaiorLista = 0
recordCount = 0
f = open(fileName,"rb")
while True:
    line = f.read(recordSize)
    if line == "": # EOF
        break
    record = struct.unpack(fileFormat, line)
    p = h(record[keyColumnIndex])
    counts[p] += 1
    if counts[p] > 1:
        colisoes += 1
    if counts[p] > tamanhoMaiorLista:
        tamanhoMaiorLista = counts[p]
    recordCount += 1
f.close()

print "Numero Colisoes:", colisoes
print "Tamanho Maior Lista:", tamanhoMaiorLista

countOfCounts = [0] * (tamanhoMaiorLista+1)

for i in counts:
    countOfCounts[i] += 1

print countOfCounts

c = 0
media = 0
for j in countOfCounts:
    probabilidade = c*(float(j)/recordCount)
    print "Lista de tamanho", c, "probabilidade", probabilidade
    media += c*probabilidade
    c += 1

print "Media acesso", media

print ""

fileName = "data/BolsaFamiliaFev.dat"

colisoes = 0
tamanhoMaiorLista = 0
recordCount = 0
f = open(fileName,"rb")
while True:
    line = f.read(recordSize)
    if line == "": # EOF
        break
    record = struct.unpack(fileFormat, line)
    p = h(record[keyColumnIndex])
    counts[p] += 1
    if counts[p] > 1:
        colisoes += 1
    if counts[p] > tamanhoMaiorLista:
        tamanhoMaiorLista = counts[p]
    recordCount += 1
f.close()

print "Numero Colisoes:", colisoes
print "Tamanho Maior Lista:", tamanhoMaiorLista

countOfCounts = [0] * (tamanhoMaiorLista+1)

for i in counts:
    countOfCounts[i] += 1

print countOfCounts

c = 0
media = 0
for j in countOfCounts:
    probabilidade = c*(float(j)/recordCount)
    print "Lista de tamanho", c, "probabilidade", probabilidade
    media += c*probabilidade
    c += 1

print "Media acesso", media
