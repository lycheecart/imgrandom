#!/usr/bin/env python
# -'''- coding: utf-8 -'''-

import requests
import re
import os
import sys
import random

class ImageGetter():
    def __init__(self):
        self.characterSpace = [
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9" 
        ]
        self.imagesDir = "randomImgurs"
        if not os.path.exists(self.imagesDir):
            os.mkdir(self.imagesDir)

        self.num404s = 0

    def isInt(self, num):
        try:
            int(num)
            return True
        except ValueError:
            return False

    def alreadyHave(self, title):
        for fileName in os.listdir(self.imagesDir):
            if fileName.startswith(title + "."):
                print(fileName + "already in " + self.imagesDir)
                return True
        return False

    def grabRandom(self, attempts):
        if attempts == 0:
            print "404s: " + str(self.num404s)
            return
        nameLength = random.choice([5, 7])
        imageTitle = ""
        for i in range(nameLength):
            imageTitle = imageTitle + random.choice(self.characterSpace)

        # one in a million billion chance but idc
        if self.alreadyHave(imageTitle):
            grabRandom(attempts)

        response = requests.get("https://imgur.com/" + imageTitle)
        if str(response.status_code) != "404":
            pattern = imageTitle + "\.(jpg|jpeg|png|gif|apng|tiff|pdf|mov|mp4)"
            prog = re.compile(pattern, re.IGNORECASE)
            nameMatch = prog.search(response.text)
            if nameMatch is not None:
                imageName = nameMatch.group(0)
                print imageName
                aMegabyte = 1024*1024
                imgResponse = requests.get("https://i.imgur.com/" + imageName, stream=True)
                with open(self.imagesDir + "/" + imageName, "wb")  as fd:
                    for chunk in imgResponse.iter_content(chunk_size=aMegabyte):
                        fd.write(chunk)
                self.grabRandom(attempts - 1)
            else:
                print "oops"
                print "(" + imageTitle + ")"
        else:
            self.num404s = self.num404s + 1
            self.grabRandom(attempts)
        
if __name__ == "__main__":
    ig = ImageGetter()
    if len(sys.argv) == 1:
        ig.grabRandom(attempts = 1)
    elif ig.isInt(sys.argv[1]):
        ig.grabRandom(attempts = int(sys.argv[1]))
    else:
        print "odd arg"
