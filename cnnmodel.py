from keras.models import Model, Sequential
from keras.layers import InputLayer, Conv2D, MaxPooling2D, BatchNormalization, GlobalAveragePooling2D, ZeroPadding2D
from keras.layers import Activation, Dropout, Flatten, Dense
import keras

#####################################################################
def simpleCNN(input_shape, outclass, sigma='sigmoid'):
    
    model = None
    model = Sequential()
    model.add(InputLayer(input_shape=input_shape))
    
    for i in [64, 96, 128]:
        model.add(Conv2D(i, (3, 3), padding='valid', activation='relu'))
        model.add(Conv2D(i, (3, 3), padding='valid', activation='relu'))
        model.add(MaxPooling2D(pool_size=(3, 3), strides=(2,2)))

    model.add(Flatten())
    for i in range(2):
        model.add(Dense(1024, activation='relu'))

    model.add(Dense(outclass)) 
    model.add(Activation(sigma))
    
    return model

def vgg9CNN(input_shape, outclass, sigma='sigmoid'):
    
    model = None
    model = Sequential()
    model.add(InputLayer(input_shape=input_shape))
       
    for i in [64, 96, 128]:
        model.add(Conv2D(i, (3, 3), padding='valid'))
        model.add(BatchNormalization())
        model.add(Activation('relu'))
        model.add(Conv2D(i, (3, 3), padding='valid'))
        model.add(BatchNormalization())
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(3, 3), strides=(2,2)))

    model.add(Flatten())
    for i in range(2):
        model.add(Dense(1024, activation='relu'))
        model.add(Dropout(0.5))

    model.add(Dense(outclass)) 
    model.add(Activation(sigma))
    
    return model

def vgg16CNN(input_shape, outclass, sigma='sigmoid'):
    
    model = None
    model = Sequential()
    model.add(InputLayer(input_shape=input_shape))
    model.add(BatchNormalization(input_shape=input_shape))
    
    for i in [64, 128]:
        model.add(ZeroPadding2D((1, 1)))
        model.add(Conv2D(i, (3, 3), activation='relu'))
        model.add(ZeroPadding2D((1, 1)))
        model.add(Conv2D(i, (3, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2,2)))

    for i in [256, 512, 512]:
        model.add(ZeroPadding2D((1, 1)))
        model.add(Conv2D(i, (3, 3), activation='relu'))
        model.add(ZeroPadding2D((1, 1)))
        model.add(Conv2D(i, (3, 3), activation='relu'))
        model.add(ZeroPadding2D((1, 1)))
        model.add(Conv2D(i, (3, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2,2)))
        
    model.add(Flatten())
    for i in range(2):
        model.add(Dense(4096, activation='relu'))
        model.add(Dropout(0.5))

    model.add(Dense(outclass)) 
    model.add(Activation(sigma))
    
    return model

def vgg16CNNtl(input_shape, outclass, sigma='sigmoid'):
    
    base_model = None
    base_model = keras.applications.VGG16(weights='imagenet', include_top=False, input_shape=input_shape)
    top_model = Sequential()
    top_model.add(Flatten(input_shape=base_model.output_shape[1:]))
    for i in range(2):
        top_model.add(Dense(4096, activation='relu'))
        top_model.add(Dropout(0.5))
    top_model.add(Dense(outclass, activation=sigma))

    model = None
    model = Model(inputs=base_model.input, outputs=top_model(base_model.output))
    
    return model
 
def resnet50tl(input_shape, outclass, sigma='sigmoid'):
    
    base_model = None
    base_model = keras.applications.resnet50.ResNet50(weights='imagenet', include_top=False, input_shape=input_shape)
    top_model = Sequential()
    top_model.add(Flatten(input_shape=base_model.output_shape[1:]))
    for i in range(2):
        top_model.add(Dense(4096, activation='relu'))
        top_model.add(Dropout(0.5))
    top_model.add(Dense(outclass, activation=sigma))

    model = None
    model = Model(inputs=base_model.input, outputs=top_model(base_model.output))
    
    return model