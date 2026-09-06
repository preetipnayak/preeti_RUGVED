""" 3. Grayscale, HSV & Edge Detection
        * Convert an image to grayscale and HSV.
        * Apply Canny edge detection to the grayscale image.
        * Display the original, grayscale, HSV, and edge-detected images. """

import cv2 as cv

img= cv.imread('Photos/Smile.jpg')

if img is None:
    print("No image found!!!")

else:
    print("""  
███████ ███    ███ ██ ██      ███████ 
██      ████  ████ ██ ██      ██      
███████ ██ ████ ██ ██ ██      █████   
     ██ ██  ██  ██ ██ ██      ██      
███████ ██      ██ ██ ███████ ███████ 
                                       """)

    cv.waitKey(1000)
    
    gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    cv.imshow('Original Image',img)
    cv.imshow('Grayscaled Image',gray_img)
    

    edges = cv.Canny(gray_img, 100, 200)
    cv.imshow('Canny Edges', edges)
    

    
    hsv_img=cv.cvtColor(img,cv.COLOR_BGR2HSV)
    cv.imshow('Original Image',img)
    cv.imshow('HSV Image',hsv_img)
    cv.waitKey(0)
    cv.destroyAllWindows()

cv.imwrite('grayscale_result.jpg', gray_img)
cv.imwrite('hsv_result.jpg', hsv_img)
cv.imwrite('edges_result.jpg', edges)



    






































































