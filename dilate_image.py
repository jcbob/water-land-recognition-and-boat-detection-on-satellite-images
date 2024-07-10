import numpy as np
import cv2

def dilate_image(binary_image, kernel_size=3, iterations=1):

    # Create a structuring element (kernel)
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    
    # Apply dilation
    dilated_image = cv2.dilate(binary_image, kernel, iterations=iterations)
    
    return dilated_image