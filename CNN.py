import tensorflow
import keras
import numpy as np
np.random.seed(1337)

from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense,Activation,Conv2D,MaxPooling2D
from keras.optimizers import RMSprop

Vector_len = 10
Vector_wid = 10
#NewDataset = np.reshape(Original_dat, (len(Original_dat),3,10,10))

model = Sequential()

model.add(Conv2D(filters=32,kernel_size=(5,5),strides=(1,1),padding='same',data_format='channels_first',input_shape=(3,10,10)))

model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2),strides=(2,2),padding='same'))

