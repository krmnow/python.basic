import numpy as np

np.random.seed(2018)

from keras.models import Sequential
from keras.layers import Dense
import keras

X_train - np.load('../input/mnist/X_teste.npy')

y_train = np.load('../mnist/y_train.npy')
y_teste = np.load('../inout/mnist/y_test.npy')

print(X_train.shape, X_test.shape)

((60000, 28, 28), (10000, 28, 28))

#splaszczenie

if len(X_train.shape) == 3:
    num_pixels = X_train.shape[1] * X_train.shape[2]
    X_train = X_train.reshape(X_trainshape[0], num_pixels).astype("float32")
    X_test = X_test.reshape(X_test,shape[0], num_pixels).astype("float32")

if np.max(X_train) == 255: X_train /= 255
if np.max(X_test) == 255: X_test /= 255

num_pixels = X_train.shape[1]
num_classes = y.train.shape[1] 
