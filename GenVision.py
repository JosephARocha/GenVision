#from __future__ import print_function
from keras.layers import Conv2D,MaxPooling2D
from keras.layers import Activation,Dropout,Flatten,Dense
from keras.models import Sequential
from PIL import Image
from keras.preprocessing.image import img_to_array
from keras import optimizers
import numpy as np
import os
from numpy import array
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import sys
model = Sequential()
#dire = ''
#folder = os.listdir(dire)


img_width,img_height = 150,150
input_shape = (img_width, img_height, 3)

model.add(Conv2D(32, (3, 3), input_shape=input_shape))
model.add(Activation('relu'))
model.add(Conv2D(32,(3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(128, (3, 3)))
model.add(Activation('relu'))
model.add(Conv2D(128, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten()) 
model.add(Dense(128))
model.add(Activation('relu'))

model.add(Dense(1))
model.add(Activation('sigmoid'))
model.load_weights('gender_try.h5')
optimizer= optimizers.RMSprop(lr=0.0001, rho=0.9, epsilon=1e-08, decay=0.0)
model.compile(loss='binary_crossentropy',optimizer='rmsprop',metrics =['accuracy'])

things_to_classify = []

data = sys.argv[1]
print(data)
img = Image.open(data)
img = img.resize((150, 150))
things_to_classify.append(np.asarray(img, dtype=np.uint8))

arr = array(things_to_classify)

classes = model.predict_classes(arr,batch_size=32,verbose=0)
for cl in classes:
    if cl[0] == 0:
        print('FEMALE')
    else:
        print('male')
