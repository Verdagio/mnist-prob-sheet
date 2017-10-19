#Adaptation of:
#   https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python
#   https://stackoverflow.com/questions/2872381/how-to-read-a-file-byte-by-byte-in-python-and-how-to-print-a-bytelist-as-a-binar
import gzip
import numpy as np
import PIL.Image as pil

def read_labels_from_file(filename) :
    with gzip.open(filename, 'rb') as f:
        magic = f.read(4)
        magic = int.from_bytes(magic, 'big')
        print("magic is: ", magic)
        
        nolab = f.read(4)
        nolab = int.from_bytes(nolab, 'big')
        print("number of labels: ", nolab)

        labels = [f.read(1) for i in range(nolab)]
        labels = [int.from_bytes(label, 'big') for label in labels]
        
        return labels


def read_images_from_file(file):
    with gzip.open(file, 'rb') as f:
        magic = f.read(4)
        magic = int.from_bytes(magic, 'big')
        print("magic is: ", magic)
        
        nolab = f.read(4)
        nolab = int.from_bytes(nolab, 'big')
        print("number of labels: ", nolab)

        norow = f.read(4)
        norow = int.from_bytes(norow, 'big')
        print("number of rows: ", norow)
        
        nocol = f.read(4)
        nocol = int.from_bytes(nocol, 'big')
        print("number of cols: ", nocol)    
        
        
        images = []
        
        for i in range(nolab):
            rows = []
            for r in range(norow):
                cols = []
                for c in range(nocol):
                    cols.append(int.from_bytes(f.read(1), 'big'))
                rows.append(cols)
            images.append(rows)
            
        return images

def save(image, name, id, label):
    location = "images/%s-%05d-%d.png"
    img = np.array(image)
    img = pil.fromarray(img)
    img = img.convert('RGB')
    img.save(location % (name, id, label))

train_labels = read_labels_from_file('data/train-labels-idx1-ubyte.gz')
test_labels = read_labels_from_file('data/t10k-labels-idx1-ubyte.gz')
            
train_images = read_images_from_file('data/train-images-idx3-ubyte.gz')
test_images = read_images_from_file('data/t10k-images-idx3-ubyte.gz')

#will print out an image 
for row in train_images[4999]:
    for col in row:
        print('.' if col <= 127 else '#', end='')
    print()
    
for i in range(len(train_images)):  #   Please note: this will create 60,000 png images
    save(train_images[i],'train', (i+1), train_labels[i])        

for i in range(len(test_images)):   #   Please note: this will create 10,000 png images
    save(test_images[i],'test', (i+1), test_labels[i])
    
        
    
        
        
    

        

    

