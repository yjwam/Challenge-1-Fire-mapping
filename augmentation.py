import numpy as np
from matplotlib import pyplot as plt
from skimage.transform import AffineTransform, warp
from skimage import io, img_as_ubyte
import random
import os
from scipy.ndimage import rotate
import cv2

import albumentations as A

def image_generate(n,x,y):
    SIZE_X = x #Resize images (height  = SIZE_Y, width = SIZE_X)
    SIZE_Y = y
    images_to_generate=n
    images_path="data/train_images/" #path to original images
    masks_path = "data/train_masks/"
    
    images=[] # to store paths of images from folder
    masks=[]
    
    for im in os.listdir(images_path):  # read image name from folder and append its path into "images" array     
        images.append(os.path.join(images_path,im))

    for msk in os.listdir(masks_path):  # read image name from folder and append its path into "images" array     
        masks.append(os.path.join(masks_path,msk))


    aug = A.Compose([
        A.VerticalFlip(p=0.5),              
        A.RandomRotate90(p=0.5),
        A.HorizontalFlip(p=1),
        A.Transpose(p=1)])
    aug_images = []
    aug_masks = []
    i = 1
    while i<=images_to_generate: 
        number = random.randint(0, len(images)-1)  #Pick a number to select an image & mask
        image = images[number]
        mask = masks[number]
        
        original_image = cv2.imread(image,cv2.IMREAD_COLOR)
        original_mask = cv2.imread(mask)

        original_image = cv2.resize(original_image, (SIZE_Y, SIZE_X))
        original_mask = cv2.resize(original_mask, (SIZE_Y, SIZE_X))
        
        
        augmented = aug(image=original_image, mask=original_mask)
        transformed_image = augmented['image']
        transformed_mask = augmented['mask']
        
        transformed_mask = np.sum(transformed_mask,axis = 2)/3
        transformed_mask = np.expand_dims(transformed_mask, axis=2)
        
        aug_images.append(transformed_image.astype('int8'))
        aug_masks.append(transformed_mask.astype('int8'))
        i =i+1
        
    return aug_images,aug_masks
