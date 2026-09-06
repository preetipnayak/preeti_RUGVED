""" 2. Basic Image Manipulation
        * Resize an image.
        * Crop a specific region.
        * Flip the image horizontally.
        * Display and save the results. """

import cv2 as cv

img_1= cv.imread('Photos/Resize_Me.jpg')

if img_1 is None:
    print("No image found!!!")

else:
    resize_img = cv.resize(img_1,(500,800))
    cv.imshow('Original Image',img_1)
    cv.imshow('Resized Image',resize_img)

    cv.waitKey(0)
    cv.destroyAllWindows()

img_2=cv.imread('Photos/Teddy.jpg')

if img_2 is None:
    print("No image found!!!")

else:
    crop_img=img_2[500:1308,36:736]
    cv.imshow('Original Image',img_2)
    cv.imshow('Cropped Image',crop_img)

    cv.waitKey(0)
    cv.destroyAllWindows()

img_3=cv.imread('Photos/Hello.jpg')

if img_3 is None:
    print("No image found!!!")

else:
    flip_img=cv.flip(img_3,1)
    cv.imshow('Original Image',img_3)
    cv.imshow('Flipped Image',flip_img)

    cv.waitKey(0)
    cv.destroyAllWindows()

cv.imwrite('Resize_result.jpg', resize_img)
cv.imwrite('Crop_result.jpg', crop_img)
cv.imwrite('Flip_result.jpg', flip_img)














