import cv2
import numpy as np

def threshold_impl(src, thresh, maxval):
    """
    Applies a binary threshold to an image.
    
    Parameters:
    src (numpy.ndarray): The source grayscale image.
    thresh (int): The threshold value.
    maxval (int): The value to set for pixels that pass the threshold.
    
    Returns:
    numpy.ndarray: The binary thresholded image.
    """
    width = src.shape[1]
    height = src.shape[0]
    dest = np.zeros_like(src)  # Create an empty array with the same shape as the source image
    
    # Iterate over each pixel in the source image
    for j in range(height):
        for i in range(width):
            if src[j, i] > thresh:
                dest[j, i] = maxval  # Set the pixel to maxval if it is above the threshold
            else:
                dest[j, i] = 0  # Set the pixel to 0 if it is below the threshold
    
    return dest

def main():
    """
    Main function to read an image, apply three different thresholding methods, 
    and display the results using OpenCV.
    """
    frame = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)  # Read the image in grayscale

    th = 128  # Threshold value
    
    # Apply custom threshold implementation
    thresh_my = threshold_impl(frame, th, 255)
    
    # Apply OpenCV threshold implementation
    ret, thresh_cv = cv2.threshold(frame, th, 255, cv2.THRESH_BINARY)
    
    # Apply NumPy threshold implementation
    thresh_np = np.where(frame > th, np.uint8(255), np.uint8(0))
    
    # Display the results
    cv2.imshow('Custom Threshold', thresh_my)
    cv2.imshow('OpenCV Threshold', thresh_cv)
    cv2.imshow('NumPy Threshold', thresh_np)

    cv2.waitKey(5000)  # Wait for 5 seconds
    cv2.destroyAllWindows()  # Close all OpenCV windows

if __name__ == '__main__':
    main()
