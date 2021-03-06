import numpy as np 
from keras.models import Sequential
from keras.layers import Dense, Activation

#Generate dummy training dataset
np.random.seed(2018)
x_train = np.random.random((6000,10))
y_train = np.random.randint(2, size=(6000, 1))

#Generate dummy validation dataset
x_val = np.random.random((2000,10))
y_val = np.random.randint(2, size=(2000, 1))

#Generate dummy test dataset
x_test = np.random.random((2000, 10))
y_test = np.random.randint(2, size=(2000, 1))

#Define the model architecture
model = Sequential()
model.add(Dense(64, input_dim = 10, activation = "relu"))       #Layer1
model.add(Dense(32, activation = "relu"))                       #Layer2
model.add(Dense(16, activation = "relu"))                       #Layer3
model.add(Dense(8,  activation = "relu"))                       #Layer4
model.add(Dense(4, activation = "relu"))                        #Layer5
model.add(Dense(1,  activation = "relu"))                       #Outputlayer

#Configure the model
model.compile(optimizer='Adam', loss='binary_crossentropy', metrics=['accuracy'])

#Train the model
model.fit(x_train, y_train, batch_size=64, epochs=3, validation_data=(x_val, y_val))