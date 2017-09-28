#Adaptation of:
#   https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python
#   https://stackoverflow.com/questions/2872381/how-to-read-a-file-byte-by-byte-in-python-and-how-to-print-a-bytelist-as-a-binar
import gzip

def read_labels_from_file(filename) :
    with gzip.open(filename, 'rb') as f:
        magic = f.read(4)
        magic = int.from_bytes(magic, 'big')
        print("magic is: ", magic)
        
        nolab = f.read(4)
        nolab = int.from_bytes(nolab, 'big')
        print("no of labels: ", nolab)

        labels = [f.read(1) for i in range(nolab)]
        labels = [int.from_bytes(label, 'big') for label in labels]
        
        return labels
    
train_labesl = read_labels_from_file('data/train-images-idx3-ubyte.gz')
test_labesl = read_labels_from_file('data/t10k-images-idx3-ubyte.gz')
        

    
    
    
f.close()
