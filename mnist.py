#Adaptation of:
#   https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python
#   https://stackoverflow.com/questions/2872381/how-to-read-a-file-byte-by-byte-in-python-and-how-to-print-a-bytelist-as-a-binar
import gzip
import io

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
    
    

            
train_images = read_images_from_file('data/train-images-idx3-ubyte.gz')
test_images = read_images_from_file('data/t10k-images-idx3-ubyte.gz')

for row in train_images[4999]:
    for col in row:
        print('.' if col <= 127 else '#', end='')
    print()
        
import PIL.Image as pil
img = train_image[4999]
img = np.array(img)
img = pil.fromarray(img)
img = img.convert('RGB')
img.show()
img.save('2.png')
        
        
    
        
        
    

        

    

