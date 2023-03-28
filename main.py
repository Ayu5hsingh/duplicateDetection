import imagehash 
import pandas 
import os 
import cv2
from PIL import Image 
import random

# class duplication:
def checkDuplication():
    images_hash={}
    for i in (os.listdir(path="C:/kaggler/Airbnb Data/Test Data/bathroom")):
        # img=cv2.imread(f"C:/kaggler/Airbnb Data/Test Data/bathroom/{i}")

        if i.endswith(".jpg"):
            file_path=os.path.join("C:/kaggler/Airbnb Data/Test Data/bathroom",i)
            img_hash=str(imagehash.average_hash(Image.open(file_path)))
            if img_hash in images_hash:
                print(f"There is duplication present for {i} image")
                
            else:
                images_hash[img_hash]=file_path

def createDuplicates():
    for i,filename in enumerate(os.listdir("C:/kaggler/Airbnb Data/Test Data/bathroom"),1):
        img_path=os.path.join("C:/kaggler/Airbnb Data/Test Data/bathroom",filename)
        if filename.endswith(".jpg"):
            no_of_copies=random.randint(0,4)
            image=Image.open(img_path)
            image_copy=image.copy()
            new_name=f"{filename}{i}.jpg"
            image_copy.save(f"C:/kaggler/Airbnb Data/Test Data/bathroom/{new_name}")
        

checkDuplication()
createDuplicates()


    
      
      
      
      
      
