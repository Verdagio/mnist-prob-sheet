#Adaptation of:
#   https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python
#   https://stackoverflow.com/questions/2872381/how-to-read-a-file-byte-by-byte-in-python-and-how-to-print-a-bytelist-as-a-binar
import gzip
import numpy as np
import PIL.Image as pil                                       # import 3 modules required 

def read_labels_from_file(filename) :                         # create a function that will read the labels from a .gz file 
    with gzip.open(filename, 'rb') as f:                      # using gzip decompress the file, read it and save it as f - https://docs.python.org/2/library/gzip.html
        magic = f.read(4)                                     # the magic number is the 4th element - http://yann.lecun.com/exdb/mnist/
        magic = int.from_bytes(magic, 'big')                  # convert to an int from bytes using the magic number & byteorder set to big If byteorder is "big", the most significant byte is at the beginning of the byte array.
        print("magic is: ", magic)
        
        nolab = f.read(4)                                     # number of labels is the next piece of data to take in
        nolab = int.from_bytes(nolab, 'big')
        print("number of labels: ", nolab)

        labels = [f.read(1) for i in range(nolab)]            # create an array of labels based off the size
        labels = [int.from_bytes(label, 'big') for label in labels]     # and insert a label into each
        
        return labels


def read_images_from_file(file):                              # again we do much the same as before except this time we will get the magic number, labels, number of rows & columns
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

        for i in range(nolab):                              # in this nested loop we will populate the rows & columns with data 
            rows = []                                         
            for r in range(norow):
                cols = []
                for c in range(nocol):
                    cols.append(int.from_bytes(f.read(1), 'big'))   # columns store the data
                rows.append(cols)                                   # rows store the column data
            images.append(rows)                                     # and images store the rows (all of data essentially)
            
        return images

def save(image, name, id, label):                                   # this function will save our  image as a .png file 
    location = "images/%s-%05d-%d.png"
    img = np.array(image)
    img = pil.fromarray(img)                                        # Creates an image memory from an object exporting the array interface (using the buffer protocol). - http://pillow.readthedocs.io/en/3.1.x/reference/Image.html
    img = img.convert('RGB')                                        # Returns a converted copy of this image. 
    img.save(location % (name, id, label))                          # saves to the destination specified

train_labels = read_labels_from_file('data/train-labels-idx1-ubyte.gz') # call the methods to extract the data from them and store said data
test_labels = read_labels_from_file('data/t10k-labels-idx1-ubyte.gz')
            
train_images = read_images_from_file('data/train-images-idx3-ubyte.gz')
test_images = read_images_from_file('data/t10k-images-idx3-ubyte.gz')

#will print out an image 
for row in train_images[4999]:
    for col in row:
        print('.' if col <= 127 else '#', end='')                       # to print, we'll represent the vaule stored with either a . or # to show in console
    print()
    
for i in range(len(train_images)):  #   Please note: this will create 60,000 png images
    save(train_images[i],'train', (i+1), train_labels[i])        

for i in range(len(test_images)):   #   Please note: this will create 10,000 png images
    save(test_images[i],'test', (i+1), test_labels[i])
    
        
    
        
        
    

        

    

