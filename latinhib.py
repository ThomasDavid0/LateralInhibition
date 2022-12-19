import numpy as np
import plotly.express as px
from PIL import Image


def latinhib(arr, ncycles=1):


    def checkind(r,c,arr):
        """Return the sum of signs of differences between requested number and those surrounding it """
        res = 0

        for i in [-1,1]:
            for j in [-1,1]:

                res += np.sign(arr[r,c] - arr[r+i,c+j]) 

        if res > 255:
            return 255
        if res < 0:
            return 0
        return res

    #run checkind for the whole array then add to the original, repeat for the requested number of cycles.    
    for _ in range(ncycles):
        arr2 = []
        for i in range(1, arr.shape[0]-1):
            arr3 = []
            for j in range(1, arr.shape[1]-1):
                arr3.append(checkind(i,j,arr))
            
            arr2.append(arr3)

        arr[1:-1,1:-1] = arr[1:-1,1:-1] + np.array(arr2)
        
    return arr


if __name__ == '__main__':    
    # Open the image and convert to grayscale
    image = Image.open('Capture.jpg').convert('L')

    #convert image to numpy array
    arr = np.array(image) 
    
    #display the original image
    fig = px.imshow(arr)
    fig.update_layout(coloraxis_showscale=False).show()

    #run lateral inhibition
    arr3  = latinhib(arr, 100)

    #display the new image
    fig = px.imshow(arr3)
    fig.update_layout(coloraxis_showscale=False).show()