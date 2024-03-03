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