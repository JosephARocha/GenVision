from keras.layers import Conv2D,MaxPooling2D
from keras.layers import Activation,Dropout,Flatten,Dense
from keras.models import Sequential
from PIL import Image, ImageOps
from keras.preprocessing.image import img_to_array
from keras import optimizers
import numpy as np
import os
from numpy import array
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import sys

model = Sequential()

img_width,img_height = 150,150
input_shape = (img_width, img_height, 3)

model = Sequential()

model.add(Conv2D(64,(3,3), input_shape=input_shape))
model.add(Activation('relu'))
model.add(Conv2D(64, (3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(3, 3)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(3,3)))

model.add(Conv2D(16, (3, 3)))
model.add(Activation('relu'))
model.add(Conv2D(16, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(3,3))) 

model.add(Flatten()) 
model.add(Dense(16))
model.add(Activation('relu'))

model.add(Dense(1))
model.add(Activation('sigmoid'))

model.load_weights('GenVision.h5')
myoptimizer= optimizers.RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.000066)
model.compile(loss='binary_crossentropy',optimizer=myoptimizer,metrics =['accuracy'])

things_to_classify = []

data = sys.argv[1]
print(data)
img = Image.open(data)
img = ImageOps.fit(img, (150, 150), Image.ANTIALIAS, 0, (0.5, 0.5))
things_to_classify.append(np.asarray(img, dtype=np.uint8))

arr = array(things_to_classify)

classes = model.predict_classes(arr,batch_size=32,verbose=0)
for cl in classes:
    if cl[0] == 0:
        print('FEMALE')
    else:
        print('male')
