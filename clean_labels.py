from medpy.io import load
import os
import numpy as np
from string import *
from utils import reshape
import SimpleITK
from medpy.io import save
import sys


#this dictionary contains as key the labels to remove and as value the label that shpuld be there instead.
labels_to_clean={
    "2": "1", 
    "3": "1", 
    "4": "1", 
    "5": "1", 
    "6": "1", 
    "7": "1", 
    "8": "1", 
    "9": "1", 
    "10": "1", 
    "11": "1", 
    "12": "1", 
    "102": "101", 
    "103": "101", 
    "104": "101", 
    "105": "101", 
    "106": "101", 
    "107": "101", 
    "108": "101", 
    "109": "101", 
    "110": "101", 
    "111": "101", 
    "112": "101", 
}


def main():
    image_to_clean=sys.argv[1]
    if not os.path.exists(image_to_clean):
        print("the image doesn't exist in search path!\n")
        exit(1)
    folder_output=os.path.dirname(image_to_clean)
    y_shape=256
    z_shape=64
    
    image, image_header = load(image_to_clean)
    for x in np.nditer(image, op_flags = ['readwrite']):
        for label in labels_to_clean.keys():
            # if the value on the pixel is a label from the dictionary- change it.
            if x==atoi(label):
                x=atoi(labels_to_clean[label])
    image = reshape(image, append_value=0, new_shape=(image.shape[0], image.shape[1], image.shape[2]))
    save(image, os.path.join(folder_output,'clean.nii'), image_header)


if __name__=="__main__":
    if len(sys.argv)<2:
        print("please enter the path to the image that you want to clean!\n")
        exit(1)
    main()