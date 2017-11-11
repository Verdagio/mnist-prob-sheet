# mnist-prob-sheet

# Introduction
The following is an in class assignment of: Reading in the MNIST data sets byte by byte into a data structure to then output the image to console & save it as a .PNG file with a generated name.
This machine learning exercise is to be done using the python programming language, for module Emerging technologies. 

### What is the MNIST data set?

The MNIST database of handwritten digits, available from this page, has a training set of 60,000 examples, and a test set of 10,000 examples. It is a subset of a larger set available from NIST. The digits have been size-normalized and centered in a fixed-size image.
It is a good database for people who want to try learning techniques and pattern recognition methods on real-world data while spending minimal efforts on preprocessing and formatting.

For more info see : [MNIST](http://yann.lecun.com/exdb/mnist/)

## Getting started

To be able to run these scripts we have a bit of setup to do first. Firstly we will need to have python installed you can get it here:

[Python](https://www.python.org/downloads/)

Once the download & installation of Python is finished we are ready to go!

You might need to install some dependencies.

Open a CMD / Terminal window on your system and type in the following:

1. Pillow -> ```pip install pillow```
2. Numpy -> ```pip install numpy```
3. Gzip -> ```pip install gzip```

With that out of the way we can go to the directory of the project

```cd path/to/directory```

Once in the project directory we will use the following commands to run the scripts

First run:

```python setup.py```

That will create our images directory (the location where the images will be saved), now run:

```python mnist.py```

Note.. this will generate approximately 69,000 .png images in the image/ directory 

### Asignment specification

These problems relate to the famous MNIST data set. Save your work as a Python file, or a collection of Python files. Place them in a single repository on GitHub, complete with a README. The files are in a bespoke format, as described on the website.

1. Read the data files

Download the image and label files. Have Python decompress and read them byte by byte into appropriate data structures in memory.

2. Output an image to the console

Output the third image in the training set to the console. Do this by representing any pixel value less than 128 as a full stop and any other pixel value as a hash symbol.

3. Output the image files as PNGs

Use Python to output the image files as PNGs, saving them in a subfolder in your repository. Name the images in the format train-XXXXX-Y.png or test-XXXXX-Y.png where XXXXX is the image number (where it occurs in the data file) and Y is its label. For instance, the five-thousandth training image is labelled 2, so its file name should be train-04999-2.png. 