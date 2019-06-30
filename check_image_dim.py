from medpy.io import load
import os
import numpy as np
from string import *
from utils import reshape
import SimpleITK
from medpy.io import save
import sys
import nibabel as nib



#this functions checks if the dimensions of 2 .nii files (given as parameters to the script) are the same.
#throws error if not!

def main():
    image1=sys.argv[1]
    image2=sys.argv[2]
    if not os.path.exists(image1):
        print("the first image doesn't exist in search path!\n")
        exit(1)
    if not os.path.exists(image2):
        print("the second image doesn't exist in search path!\n")
        exit(1)
    image_1 = nib.load(image1)
    image_2 = nib.load(image2)
    header1=image_1.header
    header2=image_2.header
    if header1.get_data_shape() != header2.get_data_shape():
        print("Error!!!\nThe image: " +os.path.basename(image1)+" and it's segmnetation have different dimensions!\n")
        exit(1)


if __name__=="__main__":
    if len(sys.argv)<3:
        print("please enter the path to the images that you want to check their dimensions!\n")
        exit(1)
    main()