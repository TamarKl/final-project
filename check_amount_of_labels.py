from medpy.io import load
import os
import numpy as np
from string import *
from utils import reshape
import SimpleITK
from medpy.io import save
import sys
import nibabel as nib



#This function checks the amount fo labels that there are in a .nii file that is given as input.
#if the amount is equal to the number of classes defined in the config file- the test Passes.


def main():
    image_to_check=sys.argv[1]
    if not os.path.exists(image_to_check):
        print("the image doesn't exist in search path!\n")
        exit(1)
    num_classes=sys.argv[2]
    image = nib.load(image_to_check)
    _image=image.get_fdata()

    labels_found=[]
    #iterate over the image and create a list of all the different labels.
    for x in range(len(_image)):
        for y in range(len(_image[0])):
            for z in range(len(_image[0][0])):
                if not str(_image[x,y,z].astype(np.int64)) in labels_found:
                    labels_found+=str(_image[x,y,z].astype(np.int64))
    if len(labels_found)!= atoi(num_classes):
        print("Error!\nThe number of labels in the segmented image is :"+str(len(labels_found))+" please change the config file accordingly!\n")
        exit(1)
    print("Number of labels is correct!!\n")


if __name__=="__main__":
    if len(sys.argv)<3:
        print("please enter the path to the image that you want to clean and the number of classes in the config files!\n")
        exit(1)
    main()