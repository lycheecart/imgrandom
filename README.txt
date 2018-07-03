script to get random pictures from https://imgur.com/

depends on the python requests http library
http://docs.python-requests.org/en/master/

usage:
remember to chmod +x imgur_random.py

./imgur_random.py 

to download 50 images

./imgur_random.py 50

this will make a folder "randomImgurs" in the directory you run the script from, then put images in it.

stuff you can get:
https://help.imgur.com/hc/en-us/articles/115000083326-What-files-can-I-upload-What-is-the-size-limit-
    JPEG
    PNG
    GIF
    APNG
    TIFF
    PDF
    MOV (desktop website only)
    MP4 (desktop website only)

The maximum file size for non-animated images (think JPG, PNG, etc) is 20MB
The maximum file size for animated images (like GIFs) and video is 200MB
