from keras.models import Sequential
from keras.layers import Conv2D,MaxPooling2D
from keras.layers import Activation,Dropout,Flatten,Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.layers.normalization import BatchNormalization
from keras.regularizers import l2
from keras import optimizers
from keras.callbacks import ModelCheckpoint
import numpy

img_width,img_height = 150,150
train_data_dir = 'Data/training'
validation_data_dir = 'Data/validation'
nb_train_samples = 100000
nb_validation_samples = 800
epochs = 15
batch_size = 32
input_shape = (img_width, img_height,3)


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

myoptimizer= optimizers.RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.000066)
model.compile(loss='binary_crossentropy',optimizer=myoptimizer,metrics =['accuracy'])

train_datagen =ImageDataGenerator(rescale=1. /255,
                                  rotation_range=40,
                                  shear_range = 0.2,
                                  zoom_range=0.2,
                                  horizontal_flip=True,
                                  fill_mode = 'nearest'
                                  )

test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(train_data_dir,
                                                    target_size=(img_width, img_height),
                                                    batch_size=batch_size,
                                                    class_mode='binary')

validation_generator = test_datagen.flow_from_directory(validation_data_dir,
                                                        target_size=(img_width, img_height),
                                                        batch_size=batch_size,
                                                 class_mode='binary')

checkpointer = ModelCheckpoint(filepath='TheVision.hdf5', verbose=1, save_best_only=True)
callbacks_list = [checkpointer]
model.fit_generator(train_generator,
                    steps_per_epoch=nb_train_samples // batch_size,
                    epochs=epochs,
                    validation_data=validation_generator,
                    validation_steps=nb_validation_samples // batch_size,
                    callbacks = callbacks_list
                    )

model.save_weights('GenVisionWide.h5')