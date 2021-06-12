# -*- coding: utf-8 -*-

# Codigo para hacer el modelo de tensorflow.

import numpy as np
import tensorflow as tf
import pandas as pd
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib as mtp

pathDatos = "C:/Users/pc/Downloads/diositoesgrande.csv"

datos = pd.read_csv(pathDatos, error_bad_lines=False)

#datos.info()
print(datos.describe())


#Codigo de la red neuronal.
def build_model():
    model = keras.Sequential([
         layers.Dense(70, activation = 'relu', input_shape=[]),
         layers.Dense(70,activation = 'relu'),
         layers.Dense(1)
         ])
    optimizer = tf.keras.optimizers.RMSprop(learning_rate=0.001)

    model.compile(loss='mse',
              optimizer = optimizer,
              metrics = ['mae','mse'])   
    return model

model = build_model()

# Display training progress by printing a single dot for each completed epoch
class PrintDot(keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs):
    if epoch % 100 == 0: print('')
    print('.', end='')

EPOCHS = 1000

#history = model.fit(
  #normed_train_data, train_labels,
  #epochs=EPOCHS, validation_split = 0.2, verbose=0,
  #callbacks=[PrintDot()])