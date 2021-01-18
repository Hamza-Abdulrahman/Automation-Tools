#!/usr/bin/python3

##########################################################

#           Tool Developer Hamza-Abdulrahman

###########################################################
import os
import shutil


my_dir = os.path.dirname(os.path.realpath(__file__))

print("welcome in organiz.py script - happy clean folder")

for filename in os.listdir(my_dir):
    
    if filename.endswith((".jpg","png","gif")):
        if not os.exists("Images")
            os.mkdir("Images")

        shutil.copy(filename,"Images")
        os.remove(filename)
        print("DONE IMAGES Quoted")

    if filename.endswith((".py","css","html","bash","js","php","rb","sh")):
        if not os.exists("Codes")
            os.mkdir("Codes")

        shutil.copy(filename,"Codes")
        os.remove(filename)
        print("DONE CODES Quoted")

    if filename.endswith((".mp4","webm")):
        if not os.exists("Videos")    
            os.mkdir("Videos")

        shutil.copy(filename,"Videos")
        os.remove(filename)
        print("DONE VEDEOS Quoted")

    if filename.endswith((".txt")):
        if not os.exists("Text_Files")    
            os.mkdir("Text_Files")

        shutil.copy(filename,"Text_File")
        os.remove(filename)
        print("DONE TEXT FILES Quoted ")        
        
    if filename.endswith((".deb","exe")):
        if not os.exists("Programs")
            os.mkdir("Programs")

        shutil.copy(filename,"Programs")
        os.remove(filename)
        print("DONE PROGRAMS Quoted") 

    if filename.endswith((".der")):
        if not os.exists("Carteficates")
            os.mkdir("Carteficates")

        shutil.copy(filename,"Carteficates")
        os.remove(filename)
        print("DONE CARTEFICATES Quoted")  

    if filename.endswith((".rar","zip","tar")):
        if not os.exists("Compressed_File")    
            os.mkdir("Compressed_File")

        shutil.copy(filename,"Compressed_File")
        os.remove(filename)
        print("DONE COMPRESSED FILE Quoted")  

        print("EXIT ......... ^_^")