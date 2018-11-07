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

