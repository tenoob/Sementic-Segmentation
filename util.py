import numpy as np
from constant import PATCH_SIZE,MODEL_LOCATION,BUILDING,LAND,ROAD,VEGETATION,WATER,UNLABLED
import tensorflow as tf
import cv2
from patchify import patchify,unpatchify
from PIL import Image
from sklearn.preprocessing import MinMaxScaler

def to_cv2(image):
    image_rgb = image.convert("RGB")
    image_cv2 = np.array(image_rgb)[:,:,::-1].copy()
    return image_cv2

def to_rgb(img):
    Building = BUILDING.lstrip('#')
    Building = np.array(tuple(int(Building[i:i+2], 16) for i in (0, 2, 4))) 
    
    Land = LAND.lstrip('#')
    Land = np.array(tuple(int(Land[i:i+2], 16) for i in (0, 2, 4))) 
    
    Road = ROAD.lstrip('#') 
    Road = np.array(tuple(int(Road[i:i+2], 16) for i in (0, 2, 4)))
    
    Vegetation = VEGETATION.lstrip('#') 
    Vegetation = np.array(tuple(int(Vegetation[i:i+2], 16) for i in (0, 2, 4))) 
    
    Water = WATER.lstrip('#') 
    Water = np.array(tuple(int(Water[i:i+2], 16) for i in (0, 2, 4))) 
    
    Unlabeled = UNLABLED.lstrip('#') 
    Unlabeled = np.array(tuple(int(Unlabeled[i:i+2], 16) for i in (0, 2, 4))) 
    
    segmented_img = np.empty((img.shape[0], img.shape[1], 3))
    
    segmented_img[(img == 0)] = Building
    segmented_img[(img == 1)] = Land
    segmented_img[(img == 2)] = Road
    segmented_img[(img == 3)] = Vegetation
    segmented_img[(img == 4)] = Water
    segmented_img[(img == 5)] = Unlabeled
    
    segmented_img = segmented_img.astype(np.uint8)
    return(segmented_img)

def get_prediction(img):
    """
    Makes segmentation prediction on the image given
    """
    scaler = MinMaxScaler()
    model = tf.keras.models.load_model(MODEL_LOCATION, compile=False)

    pil_image = Image.open(img)
    img = to_cv2(pil_image)
    SIZE_X = (img.shape[1]//PATCH_SIZE)*PATCH_SIZE 
    SIZE_Y = (img.shape[0]//PATCH_SIZE)*PATCH_SIZE 
    large_img = Image.fromarray(img)    
    large_img = large_img.crop((0 ,0, SIZE_X, SIZE_Y))  
    large_img = np.array(large_img)  
    patches_img = patchify(large_img, (PATCH_SIZE, PATCH_SIZE, 3), step=PATCH_SIZE)  
    patches_img = patches_img[:,:,0,:,:,:]
    patched_prediction = []
    for i in range(patches_img.shape[0]):
        for j in range(patches_img.shape[1]):
            
            single_patch_img = patches_img[i,j,:,:,:]
            
            single_patch_img = scaler.fit_transform(single_patch_img.reshape(-1, single_patch_img.shape[-1])).reshape(single_patch_img.shape)
            single_patch_img = np.expand_dims(single_patch_img, axis=0)
            pred = model.predict(single_patch_img)
            pred = np.argmax(pred, axis=3)
            pred = pred[0, :,:]
                                    
            patched_prediction.append(pred)

    patched_prediction = np.array(patched_prediction)
    patched_prediction = np.reshape(patched_prediction, [patches_img.shape[0], patches_img.shape[1], 
                                            patches_img.shape[2], patches_img.shape[3]])

    unpatched_prediction = unpatchify(patched_prediction, (large_img.shape[0], large_img.shape[1]))

    display_img = to_rgb(unpatched_prediction)
    
    return display_img

