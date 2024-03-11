import cv2
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as pt
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

print("X_train" , X_train.shape)

fig, axs = pt.subplots(3, 3)

cnt = 0

for i in range(3):
  for j in range(3):
   axs [i, j].imshow(X_train[cnt])
   cnt += cnt
   
X_train = tf.keras.utils.normalize(X_train, axis = 1)
X_test = tf.keras.utils.normalize(X_test, axis = 1)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape = (28, 28)))

model.add(tf.keras.layers.Dense(units = 128, activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(units = 128, activation = tf.nn.relu))

model.add(tf.keras.layers.Dense(units = 10, activation = tf.nn.softmax))
model.summary()