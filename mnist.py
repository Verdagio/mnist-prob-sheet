#Adaptation of:
#   https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python
#   https://stackoverflow.com/questions/2872381/how-to-read-a-file-byte-by-byte-in-python-and-how-to-print-a-bytelist-as-a-binar
import gzip


f = gzip.open('data/train-images-idx3-ubyte.gz', 'rb')

i = f.read(4)
print(i)

print(int.from_bytes(i, byteorder='big'))

f.close()
