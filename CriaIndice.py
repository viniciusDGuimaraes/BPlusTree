import struct
import hashlib
import os
from time import time


ti = time()
hashSize = 15000001
fileName = "data/BolsaFamiliaJan.dat"
indexName = "data/BolsaFamiliaJan-hash.dat"
dataFormat = "2s30s14s50s6s2s"
indexFormat = "14sLL"
keyColumnIndex = 2

dataStruct = struct.Struct(dataFormat)
indexStruct = struct.Struct(indexFormat)

def h(key):
    global hashSize
    return int(hashlib.sha1(key).hexdigest(),16)%hashSize

fi = open(indexName,"wb")
emptyIndexRecord = indexStruct.pack("",0,0)
for i in range(0,hashSize):
    fi.write(emptyIndexRecord)
fi.close()

f = open(fileName,"rb")
fi = open(indexName,"r+b")

fi.seek(0,os.SEEK_END)
fileIndexSize = fi.tell()
print "IndexFileSize", fileIndexSize
#fi.seek(0,os.SEEK_END)

recordNumber = 0
while True:
    line = f.read(dataStruct.size)
    if line == "": # EOF
        break

    if recordNumber%1000000 == 0:
        print recordNumber
    record = dataStruct.unpack(line)
    p = h(record[keyColumnIndex])
    fi.seek(p*indexStruct.size,os.SEEK_SET)
    indexRecord = indexStruct.unpack(fi.read(indexStruct.size))
    fi.seek(p*indexStruct.size,os.SEEK_SET)
    if indexRecord[0][0] == "\0":
        fi.write(indexStruct.pack(record[keyColumnIndex],recordNumber,0))
    else:
        nextPointer = indexRecord[2]
        fi.write(indexStruct.pack(indexRecord[0],indexRecord[1],fileIndexSize))
        fi.seek(0,os.SEEK_END)
        fi.write(indexStruct.pack(record[keyColumnIndex],recordNumber,nextPointer))
        fileIndexSize = fi.tell()
    recordNumber += 1
f.close()
fi.close()

print(time()-ti)
