"""  1. Reading & Understanding Images
        * Read an image using OpenCV.
        * Display the image.
        * Print its:
            # Height
            # Width
            # Number of channels
        * Save the image with a different filename. """


import cv2 as cv

img = cv.imread('Photos/Pippo.jpeg')

if img is None:
    print("No image found!!!")

else:

    cv.imshow('Pippo',img)

    height,width,no_channels=img.shape
    print("Height: ",height)
    print("Width: ",width)
    print("Number of channels: ",no_channels)

    cv.imwrite("Judo.jpeg",img)

    cv.waitKey(0)
    cv.destroyAllWindows()
    








































