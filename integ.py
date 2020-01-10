# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 15:23:16 2019
    
@author: vaishnov
"""
def proces_data():
    import numpy as np
    import pandas as pd
    import cv2
    from wand.image import Image,Color
    import pytesseract
    from PIL import Image as im
    import glob
    import os
      
    pytesseract.pytesseract.tesseract_cmd =r"C:\Users\rgvaish\AppData\Local\Tesseract-OCR\tesseract.exe"
    simple_list = []
    #os.chdir('E:/ML/elction roll/')
    #input_file="test.pdf"
    #UPLOAD_FOLDER = os.path.join('C:/','Documents and Settings',os.getlogin(),'Desktop')
    UPLOAD_FOLDER = 'D:/vaishnov/practise/takehome/Electoral-roll-extraction-using-opencv-master'
    os.chdir(UPLOAD_FOLDER)
    list_of_files = glob.glob(UPLOAD_FOLDER + '/*.pdf') # * means all if need specific format then *.pdf
    latest_file = max(list_of_files, key=os.path.getctime)
    '''
    with Image(filename=latest_file, resolution=300) as img:
        img.background_color = Color("white")
        img.alpha_channel = 'remove'
        img.save(filename='image.png')
    '''
    l = len(glob.glob(UPLOAD_FOLDER+'\\'+'*.png'))    
    for i in range(0,l):
        inp = 'image-'+str(l-l+i)+'.png'
        print('-----',inp)
        img = cv2.imread(inp)
        text = pytesseract.image_to_string(img)
        if ('Section No and Name' in text):
            print(i)
    
        #img = cv2.imread('image-2.png')
            if inp == 'image-2.png':            
                for i in range(1,31):
                    print('i - ',i)
                    if 1<=i<=3:
                        if i == 1:
                            y = 209
                            y_h = 500
                            x = 99
                            x_h =853
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                            kernel = np.ones((2,2), np.uint8) 
                            img1 = cv2.erode(img1, kernel, iterations=1)
                             
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                            # cv2.imshow("resized", img1)
                            # cv2.waitKey(0)
                            # cv2.destroyAllWindows()
                                    
                            
                            text = pytesseract.image_to_string(img1,config = '--psm 6')
                            print(text)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])     
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])     
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------')            
                            else:
                                pass
                        else:
                            print('Enter else-----------')
                            y = y
                            y_h = y_h
                            x = x_h
                            x_h =x+752
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                            kernel = np.ones((2,2), np.uint8) 
                            img1 = cv2.erode(img1, kernel, iterations=1)                     
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                            # cv2.imshow("resized", img1)
                            # cv2.waitKey(0)
                            # cv2.destroyAllWindows()
                            
                    
                            text = pytesseract.image_to_string(img1,config = '--psm 6')
                            print(text)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])     
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                 
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])     
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------') 
                            else:
                                pass
                    
                    elif 4<=i<=6:
                        if i == 4:
                            y = 500
                            y_h = 791
                            x = 99
                            x_h =853
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                            kernel = np.ones((2,2), np.uint8) 
                            img1 = cv2.erode(img1, kernel, iterations=1)                             
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                            # cv2.imshow("resized", img1)
                            # cv2.waitKey(0)
                            # cv2.destroyAllWindows()
                                    
                            
                            text = pytesseract.image_to_string(img1,config = '--psm 6')
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])     
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                  
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])     
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------')               
                            else:
                                pass
                        else:
                            print('Enter else-----------')
                            y = y
                            y_h = y_h
                            x = x_h
                            x_h =x+750
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                            kernel = np.ones((2,2), np.uint8) 
                            img1 = cv2.erode(img1, kernel, iterations=1)                     
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                            # cv2.imshow("resized", img1)
                            # cv2.waitKey(0)
                            # cv2.destroyAllWindows()
                            
                    
                            text = pytesseract.image_to_string(img1,config = '--psm 6')
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])     
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                               
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])     
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------') 
                            else:
                              pass
                        
                    elif 7<=i<=9:
                        if i == 7:
                            y = 791
                            y_h = 1085
                            x = 99
                            x_h =853
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                             
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                            # cv2.imshow("resized", img1)
                            # cv2.waitKey(0)
                            # cv2.destroyAllWindows()
                                    
                            
                            text = pytesseract.image_to_string(img1)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])     
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                 
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])     
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------')          
                            else:
                                pass
                        else:
                            print('Enter else-----------')
                            y = y
                            y_h = y_h
                            x = x_h
                            x_h =x+750
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                     
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                            # cv2.imshow("resized", img1)
                            # cv2.waitKey(0)
                            # cv2.destroyAllWindows()
                            
                    
                            text = pytesseract.image_to_string(img1)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])     
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                 
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])     
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------') 
                            else:
                                pass
                    elif 10<=i<=12:
                        if i == 10:
                            y = 1085
                            y_h = 1379
                            x = 99
                            x_h =853
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                             
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                            # cv2.imshow("resized", img1)
                            # cv2.waitKey(0)
                            # cv2.destroyAllWindows()
                                    
                            
                            text = pytesseract.image_to_string(img1)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])      
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                 
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])     
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------')          
                            else:
                                pass
                        else:
                            print('Enter else-----------')
                            y = y
                            y_h = y_h
                            x = x_h
                            x_h =x+750
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                     
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                            # cv2.imshow("resized", img1)
                            # cv2.waitKey(0)
                            # cv2.destroyAllWindows()
                            
                    
                            text = pytesseract.image_to_string(img1)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])     
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                 
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])    
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------')          
                            else:
                                pass
                    elif 13<=i<=15:
                        if i == 13:
                            y = 1385
                            y_h = 1675
                            x = 99
                            x_h =853
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                             
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                            # cv2.imshow("resized", img1)
                            # cv2.waitKey(0)
                            # cv2.destroyAllWindows()
                                    
                            
                            text = pytesseract.image_to_string(img1)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])     
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                             
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])    
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------')       
                            else:
                                pass
                        else:
                            print('Enter else-----------')
                            y = y
                            y_h = y_h
                            x = x_h
                            x_h =x+750
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                     
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                            # cv2.imshow("resized", img1)
                            # cv2.waitKey(0)
                            # cv2.destroyAllWindows()
                            
                    
                            text = pytesseract.image_to_string(img1)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])     
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                              
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])    
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------') 
                            else:
                                pass
                    elif 16<=i<=18:
                        if i == 16:
                            y = 1675
                            y_h = 1967
                            x = 99
                            x_h =853
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                             
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                            # cv2.imshow("resized", img1)
                            # cv2.waitKey(0)
                            # cv2.destroyAllWindows()
                                    
                            
                            text = pytesseract.image_to_string(img1)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])     
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                               
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])    
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------')    
                            else:
                                pass
                        else:
                            print('Enter else-----------')
                            y = y
                            y_h = y_h
                            x = x_h
                            x_h =x+750
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                     
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                            # cv2.imshow("resized", img1)
                            # cv2.waitKey(0)
                            # cv2.destroyAllWindows()
                            
                    
                            text = pytesseract.image_to_string(img1)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])     
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                             
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])    
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------') 
                            else:
                                pass
                    elif 19<=i<=21:
                        if i == 19:
                            y = 1965
                            y_h = 2257
                            x = 99
                            x_h =853
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                             
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                            # cv2.imshow("resized", img1)
                            # cv2.waitKey(0)
                            # cv2.destroyAllWindows()
                                    
                            
                            text = pytesseract.image_to_string(img1)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])     
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                               
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])    
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------')             
                            else:
                                pass
                        else:
                            print('Enter else-----------')
                            y = y
                            y_h = y_h
                            x = x_h
                            x_h =x+750
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                     
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                            # cv2.imshow("resized", img1)
                            # cv2.waitKey(0)
                            # cv2.destroyAllWindows()
                            
                    
                            text = pytesseract.image_to_string(img1)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])     
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                               
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])    
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------')  
                            else:
                                pass                        
                    elif 22<=i<=24:
                        if i == 22:
                            y = 2257
                            y_h = 2547
                            x = 99
                            x_h =853
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                             
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                            # cv2.imshow("resized", img1)
                            # cv2.waitKey(0)
                            # cv2.destroyAllWindows()
                                    
                            
                            text = pytesseract.image_to_string(img1)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])     
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])    
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------')          
                            else:
                                pass
                        else:
                            print('Enter else-----------')
                            y = y
                            y_h = y_h
                            x = x_h
                            x_h =x+750
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                     
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                            # cv2.imshow("resized", img1)
                            # cv2.waitKey(0)
                            # cv2.destroyAllWindows()
                            
                    
                            text = pytesseract.image_to_string(img1)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])      
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                 
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])    
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------') 
                            else:
                                pass
                    elif 25<=i<=27:
                        if i == 25:
                            y = 2551
                            y_h = 2845
                            x = 99
                            x_h =853
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                             
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                            # cv2.imshow("resized", img1)
                            # cv2.waitKey(0)
                            # cv2.destroyAllWindows()
                                    
                            
                            text = pytesseract.image_to_string(img1)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])     
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                 
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])    
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------')          
                            else:
                                pass
                        else:
                            print('Enter else-----------')
                            y = y
                            y_h = y_h
                            x = x_h
                            x_h =x+750
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                     
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                            # cv2.imshow("resized", img1)
                            # cv2.waitKey(0)
                            # cv2.destroyAllWindows()
                            
                    
                            text = pytesseract.image_to_string(img1)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])     
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                              
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])    
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------')   
                            else:   
                                pass
                    elif 28<=i<=30:
                        if i == 28:
                            y = 2847
                            y_h = 3133
                            x = 99
                            x_h =853
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                             
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                            # cv2.imshow("resized", img1)
                            # cv2.waitKey(0)
                            # cv2.destroyAllWindows()
                                    
                            
                            text = pytesseract.image_to_string(img1)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])     
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                 
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])    
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------')              
                            else:
                                pass
                        else:
                            print('Enter else-----------')
                            y = y
                            y_h = y_h
                            x = x_h
                            x_h =x+750
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                     
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                            # cv2.imshow("resized", img1)
                            # cv2.waitKey(0)
                            # cv2.destroyAllWindows()
                            
                    
                            text = pytesseract.image_to_string(img1)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])     
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                 
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])    
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------')  
                            else:
                                pass
            else:            
                for i in range(1,31):
                    print('i - ',i)
                    if 1<=i<=3:
                        if i == 1:
                            y = 175
                            y_h = 460
                            x = 99
                            x_h =853
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                             
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
#                            cv2.imshow("resized", img1)
#                            cv2.waitKey(0)
#                            cv2.destroyAllWindows()
                                    
                            
                            text = pytesseract.image_to_string(img1)
                            print(text)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])     
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])    
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------')            
                            else:
                                pass
                        else:
                            print('Enter else-----------')
                            y = y
                            y_h = y_h
                            x = x_h
                            x_h =x+752
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                     
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                            # cv2.imshow("resized", img1)
                            # cv2.waitKey(0)
                            # cv2.destroyAllWindows()
                            
                    
                            text = pytesseract.image_to_string(img1)
                            print(text)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])     
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])    
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------') 
                            else:
                                pass
                    
                    elif 4<=i<=6:
                        if i == 4:
                            y = 460
                            y_h = 755
                            x = 99
                            x_h =853
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                             
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                            # cv2.imshow("resized", img1)
                            # cv2.waitKey(0)
                            # cv2.destroyAllWindows()
                                    
                            
                            text = pytesseract.image_to_string(img1)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])     
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])    
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------')               
                            else:
                                pass
                        else:
                            print('Enter else-----------')
                            y = y
                            y_h = y_h
                            x = x_h
                            x_h =x+750
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                     
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                            # cv2.imshow("resized", img1)
                            # cv2.waitKey(0)
                            # cv2.destroyAllWindows()
                            
                    
                            text = pytesseract.image_to_string(img1)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])     
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])    
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------') 
                            else:
                              pass
                        
                    elif 7<=i<=9:
                        if i == 7:
                            y = 755
                            y_h = 1049
                            x = 99
                            x_h =853
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                             
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                            # cv2.imshow("resized", img1)
                            # cv2.waitKey(0)
                            # cv2.destroyAllWindows()
                                    
                            
                            text = pytesseract.image_to_string(img1)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])     
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                               
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])    
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------')          
                            else:
                                pass
                        else:
                            print('Enter else-----------')
                            y = y
                            y_h = y_h
                            x = x_h
                            x_h =x+750
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                     
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                            # cv2.imshow("resized", img1)
                            # cv2.waitKey(0)
                            # cv2.destroyAllWindows()
                            
                    
                            text = pytesseract.image_to_string(img1)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])      
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                              
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])    
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------') 
                            else:
                                pass
                    elif 10<=i<=12:
                        if i == 10:
                            y = 1049
                            y_h = 1339
                            x = 99
                            x_h =853
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                             
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                            # cv2.imshow("resized", img1)
                            # cv2.waitKey(0)
                            # cv2.destroyAllWindows()
                                    
                            
                            text = pytesseract.image_to_string(img1)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])     
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])    
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------')          
                            else:
                                pass
                        else:
                            print('Enter else-----------')
                            y = y
                            y_h = y_h
                            x = x_h
                            x_h =x+750
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                     
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                            # cv2.imshow("resized", img1)
                            # cv2.waitKey(0)
                            # cv2.destroyAllWindows()
                            
                    
                            text = pytesseract.image_to_string(img1)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])     
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                 
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])    
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------')          
                            else:
                                pass
                    elif 13<=i<=15:
                        if i == 13:
                            y = 1339
                            y_h = 1633
                            x = 99
                            x_h =853
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                             
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                            # cv2.imshow("resized", img1)
                            # cv2.waitKey(0)
                            # cv2.destroyAllWindows()
                                    
                            
                            text = pytesseract.image_to_string(img1)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])     
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                 
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])    
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------')       
                            else:
                                pass
                        else:
                            print('Enter else-----------')
                            y = y
                            y_h = y_h
                            x = x_h
                            x_h =x+750
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                     
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                            # cv2.imshow("resized", img1)
                            # cv2.waitKey(0)
                            # cv2.destroyAllWindows()
                            
                    
                            text = pytesseract.image_to_string(img1)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])     
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                               
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])    
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------') 
                            else:
                                pass
                    elif 16<=i<=18:
                        if i == 16:
                            y = 1633
                            y_h = 1929
                            x = 99
                            x_h =853
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                             
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                            # cv2.imshow("resized", img1)
                            # cv2.waitKey(0)
                            # cv2.destroyAllWindows()
                                    
                            
                            text = pytesseract.image_to_string(img1)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])      
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                               
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])    
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------')    
                            else:
                                pass
                        else:
                            print('Enter else-----------')
                            y = y
                            y_h = y_h
                            x = x_h
                            x_h =x+750
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                     
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                            # cv2.imshow("resized", img1)
                            # cv2.waitKey(0)
                            # cv2.destroyAllWindows()
                            
                    
                            text = pytesseract.image_to_string(img1)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])     
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                 
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])    
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------') 
                            else:
                                pass
                    elif 19<=i<=21:
                        if i == 19:
                            y = 1929
                            y_h = 2221
                            x = 99
                            x_h =853
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                             
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                            # cv2.imshow("resized", img1)
                            # cv2.waitKey(0)
                            # cv2.destroyAllWindows()
                                    
                            
                            text = pytesseract.image_to_string(img1)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])     
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                               
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])    
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------')             
                            else:
                                pass
                        else:
                            print('Enter else-----------')
                            y = y
                            y_h = y_h
                            x = x_h
                            x_h =x+750
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                     
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                            # cv2.imshow("resized", img1)
                            # cv2.waitKey(0)
                            # cv2.destroyAllWindows()
                            
                    
                            text = pytesseract.image_to_string(img1)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])     
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])    
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------')  
                            else:
                                pass                        
                    elif 22<=i<=24:
                        if i == 22:
                            y = 2221
                            y_h = 2511
                            x = 99
                            x_h =853
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                             
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                            # cv2.imshow("resized", img1)
                            # cv2.waitKey(0)
                            # cv2.destroyAllWindows()
                                    
                            
                            text = pytesseract.image_to_string(img1)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])     
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                              
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])    
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------')          
                            else:
                                pass
                        else:
                            print('Enter else-----------')
                            y = y
                            y_h = y_h
                            x = x_h
                            x_h =x+750
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                     
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                            # cv2.imshow("resized", img1)
                            # cv2.waitKey(0)
                            # cv2.destroyAllWindows()
                            
                    
                            text = pytesseract.image_to_string(img1)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])     
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                 
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])    
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------') 
                            else:
                                pass
                    elif 25<=i<=27:
                        if i == 25:
                            y = 2511
                            y_h = 2805
                            x = 99
                            x_h =853
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                             
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
                            # cv2.imshow("resized", img1)
                            # cv2.waitKey(0)
                            # cv2.destroyAllWindows()
                                    
                            
                            text = pytesseract.image_to_string(img1)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])      
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])    
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------')          
                            else:
                                pass
                        else:
                            print('Enter else-----------')
                            y = y
                            y_h = y_h
                            x = x_h
                            x_h =x+750
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                     
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
#                            cv2.imshow("resized", img1)
#                            cv2.waitKey(0)
#                            cv2.destroyAllWindows()
                            
                    
                            text = pytesseract.image_to_string(img1)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])     
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                 
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])    
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------')   
                            else:   
                                pass
                    elif 28<=i<=30:
                        if i == 28:
                            y = 2805
                            y_h = 3097
                            x = 99
                            x_h =853
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                             
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
#                            cv2.imshow("resized", img1)
#                            cv2.waitKey(0)
#                            cv2.destroyAllWindows()
                                    
                            
                            text = pytesseract.image_to_string(img1)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])     
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                 
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])    
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------')              
                            else:
                                pass
                        else:
                            print('Enter else-----------')
                            y = y
                            y_h = y_h
                            x = x_h
                            x_h =x+750
                            print(x,y,x_h,y_h)
                            img1 = img[y:y_h, x:x_h]
                            r = 600.0 / img1.shape[1]
                            dim = (600, int(img1.shape[0] * r))
                     
                            # perform the actual resizing of the image and show it
                            #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
#                            cv2.imshow("resized", img1)
#                            cv2.waitKey(0)
#                            cv2.destroyAllWindows()
                            
                    
                            text = pytesseract.image_to_string(img1)
                            if 'Age' in text:
                                new1 = text.split('\n')
                                print(new1)        
                                First_name = []
                                Middle_name = []
                                last_name = []
                                Father = []
                                Husband = []
                                House = []
                                Age = []
                                Gender = []
                                Wife = []
                                Mother = []
                                Epic = []
                                
                                for i in range(0,len(new1)):
                                    print(new1[i])
                                    if ('Name' in new1[i]) and (str(new1[i]).split(':')[0].strip() == 'Name'):
                                        #print(name)
                                        if len(str(new1[i]).split(':')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split(':')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split(':')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[3]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 2:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 3:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[1])
                                            last_name.append(str(new1[i]).split(':')[1].strip().split(' ')[2]) 
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 1:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                        elif len(str(new1[i]).split('>')[1].strip().split(' ')) == 4:
                                            First_name.append(str(new1[i]).split('>')[1].strip().split(' ')[0])
                                            Middle_name.append(str(new1[i]).split('>')[1].strip().split(' ')[2])
                                            last_name.append(str(new1[i]).split('>')[1].strip().split(' ')[3])     
                                    elif 'WPK' in new1[i] or 'ZDR' in new1[i] or 'KYJ' in new1[i] or 'ZUC' in new1[i] or 'YOJ' in new1[i] or 'STC' in new1[i] or 'AP' in new1[i] or 'DMR' in new1[i] or 'TC' in new1[i]:                                   
                                        Epic.append(new1[i])                                       
                                    elif 'Father' in new1[i]:
                                        if 's Name >' in new1[i]:
                                            Father.append(str(new1[i]).split('>')[1])
                                        elif 's Name :' in new1[i]:
                                            Father.append(str(new1[i]).split(':')[1])
                                        
                                    elif 'House' in new1[i]:
                                        if 'House Number:' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                                
                                        elif 'House Number :' in new1[i]:
                                            House.append(str(new1[i]).split(':')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number >' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1]) 
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')
                                        elif 'House Number>' in new1[i]:
                                            House.append(str(new1[i]).split('>')[1])
                                            if 'Photo' in House[0]:
                                                House = str(House[0]).replace('Photo is',' ')
                                            elif 'Available' in House[0]:
                                                House = str(House[0]).replace('Available',' ')                                 
                                    elif 'Wife' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Wife.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])
                                        elif 'Name:' in new1[i]:
                                            Wife.append(str(new1[i]).split(':')[1])      
                                    elif 'Husband' in new1[i]:
                                        if 'Name >' in new1[i]:
                                            Husband.append(str(new1[i]).split('>')[1])
                                        elif 'Name :' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])  
                                        elif 'Name:' in new1[i]:
                                            Husband.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Mother' in new1[i]:
                                        if 'Name :' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])
                                        elif 'Name >' in new1[i]:
                                            Mother.append(str(new1[i]).split('>')[1])   
                                        elif 'Name:' in new1[i]:
                                            Mother.append(str(new1[i]).split(':')[1])                                         
                                    elif 'Age' in new1[i]:  
                                        Age.append(str(new1[i]).split(' ')[1])
                                        Gender.append(str(new1[i]).split(' ')[3])
                                for i in (First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband): 
                                    if len(i) == 0:
                                        i.append('-')
                                simple_list.append([First_name,Middle_name,last_name,Age,Father,Gender,House,Mother,Wife,Husband,Epic])    
                                print('First name -',First_name)
                                print('Middle name -',Middle_name)
                                print('last name -',last_name)
                                print('Epic - ',Epic)
                                print('Father - ',Father)
                                print('Husband - ',Husband)
                                print('House - ',House)
                                print('Age - ',Age)
                                print('Gender - ',Gender)
                                print('Wife - ',Wife) 
                                print('Mother - ',Mother)
                                print('-----------------------------------')  
                            else:
                                pass                                            
    df=pd.DataFrame(simple_list,columns=['First name','Middle name','last name','Age','Father','Gender','House','Mother','Wife','Husband','Epic'])  
    df['First name']=df['First name'].str[0]
    df['Middle name']=df['Middle name'].str[0]
    df['last name']=df['last name'].str[0]
    df['Age']=df['Age'].str[0]
    df['Father']=df['Father'].str[0]
    df['Gender']=df['Gender'].str[0]
    df['House']=df['House'].str[0]
    df['Mother']=df['Mother'].str[0]
    df['Wife']=df['Wife'].str[0]
    df['Husband']=df['Husband'].str[0]
    df['Epic']=df['Epic'].str[0]
    df.index = np.arange(1, len(df) + 1)
    # df1=pd.DataFrame(simple_list,columns=['name','Age','Father','Gender','House','Mother','Wife','Husband'])          
    #dload = 'Voter.csv'
    return (df.to_csv('Roll.csv'))
    #return dload

#o = process_data('test.pdf')     
proces_data()    