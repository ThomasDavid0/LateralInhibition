import numpy as np
import plotly.express as px
from PIL import Image


def latinhib(arr):

    def checkind(r,c,arr):
        res = arr[r,c]
        for i in range(2):
            for j in range(2):
                res += arr[r+i-1,c+j-1] 
        return res


    for _ in range(3):
        arr2 = []
        for i in range(1, arr.shape[0]):
            arr3 = []
            for j in range(1, arr.shape[1]):
                arr3.append(checkind(i,j,arr))
            
            arr2.append(arr3)
        arr = np.array(arr2)

    return arr

def image_array(path):
    pass




if __name__ == '__main__':

    
    # Open the image form working directory
    image = Image.open('Capture.jpg').convert('L')
    # summarize some details about the image
    print(image.format)
    print(image.size)
    print(image.mode)
    # show the image


    arr = np.asarray(image) # np.full((11,11),255)
    
    px.imshow(arr).show()
    arr3  = latinhib(arr)
    px.imshow(arr3).show()