                                              ###encode_msg2Img###

import numpy as np
from PIL import Image

#Coverting user message to ASIIC binary codes of the individual characters 
def encode_msg(User_msg):
# USE list() TO SPLIT A MESSAGE INTO A LIST OF CHARACTERS,
# Call list(iterable) with a string as iterable to split it into a list of characters.  
    list_User_msg=list(User_msg)       
    number_msg=list()
    binary_msg=list()
    for i in range(len(list_User_msg)):    
        number_msg.append(ord(list_User_msg[i]))
        binary_msg.append("{:08b}".format(number_msg[i]))  # "{:08b}" This specifies leading 0, 8 digits, binary.
 # using list comprehension
        listToStr = ' '.join(map(str, binary_msg))
 #Removing White spaces between the binary unicode codes of the characters
        encoded_msg="".join(listToStr.split())
    return encoded_msg 


#Reshaping the 2D array of shape (int(len(imgArr)),3) to (int(len(imgArr)/3),9) 
def Img2Arr(img):
    imgArr = np.array(img.getdata())
     #print(len(imgArr))
    imgArr = imgArr.reshape(int(len(imgArr)/3),9)
     #print(len(imgArr))
    return imgArr

#encoding the user's message to the image 
def encode_msg_image(img,encoded_msg):   
    Img_Arr=Img2Arr(img)
    bin_msg=(list(encoded_msg))       #binary message
#Removing White spaces between the binary unicode codes of the characters
 #   bin_msg="".join(bin_msg.split())    
    for z in range(len(bin_msg)):
        bin_msg[z]=int(bin_msg[z])
        
    for j in range(int(len(bin_msg)/8)):
        for i in range(8) :
            if bin_msg[i+8*j]==1 :
                if Img_Arr[j][i]%2==0 :
                    Img_Arr[j][i]=Img_Arr[j][i]+1
                else :
                    Img_Arr[j][i]=Img_Arr[j][i]
            else :
                if Img_Arr[j][i]%2==0 :
                    Img_Arr[j][i]=Img_Arr[j][i]
                else :
                    Img_Arr[j][i]=Img_Arr[j][i]+1     
                    
        if j==(len(bin_msg)/8)-1:
            if Img_Arr[j][8]%2==0 :
                    Img_Arr[j][8]=Img_Arr[j][8]+1
            else :
                    Img_Arr[j][8]=Img_Arr[j][8]
        else :
            if Img_Arr[j][8]%2==0 :
                    Img_Arr[j][8]=Img_Arr[j][8]
            else :
                 Img_Arr[j][8]=Img_Arr[j][8]+1 
    return Img_Arr      


def Arr2Img(img_Arr,img):
    #Arr_Img = img_Arr.reshape(int((len(img_Arr))*3),3)  
    width, height = img.size
    Arr_Img = img_Arr.reshape(height,width,3)
    # creating image object of above array
    # saving the final output  as a PNG file
    img_en = Image.fromarray(np.uint8(Arr_Img))
    print("Enter the name for the encoded image to save(with .png extension at the end)")
    Save_image_name=str(input())
    img_en.save(Save_image_name)
    #Image.show(img_en)
    return img_en



                                            ###decode_Img2msg###
import numpy as np
from PIL import Image
 
def Img2Arr(img):
    imgArr = np.array(img.getdata())
     #print(len(imgArr))
    imgArr = imgArr.reshape(int(len(imgArr)/3),9)
     #print(len(imgArr))
    return imgArr    
    
def decode_msg_image(img):    
    Img_Arr=Img2Arr(img)
    for j in range(int(len(Img_Arr))):
        if Img_Arr[j][8]%2!=0 :
                    a=j
                    break
                    
    bin_msg= [0] * (a+1)*8                                
    for j in range(a+1):
        for i in range(8) :
            if Img_Arr[j][i]%2==0 :
                bin_msg[i+8*j]=0
            else :
                bin_msg[i+8*j]=1                
    return bin_msg

def decode_msg(User_msg):
    for j in range(int((len(User_msg))/8)):
        User_msg[j:j+1] = [''.join(map(str, User_msg[8*j :(8*j+8)]))]
    del  User_msg[int((len(User_msg))/8):int((len(User_msg)))]   
   # print(User_msg)
    msg=list()   
    final_msg=list()
    for i in range(int(len(User_msg))):
        msg.append(int(str(User_msg[i]), 2))
     #   print(msg)
        final_msg.append(chr(msg[i]))
    final_msg[0 : int((len(User_msg)))] =[''.join(map(str, final_msg[0 : int((len(User_msg)))]))] 
     
    return final_msg     

                                              ###MAIN Function###
    
print("USER : Enter the message")
User_msg=str(input())
print("Enter the name of the image ")
img=Image.open(str(input()))  #the image should in the same directory:to avoid errors there is testinput_1 with the code in the directory
bin_encoded_msg=encode_msg(User_msg)
encode_msg_image_1=encode_msg_image(img,bin_encoded_msg)
final_image=Arr2Img(encode_msg_image_1,img)
decode=decode_msg_image(final_image)
print("The User message is :")
user_msg=decode_msg(decode)
print(user_msg)
      
