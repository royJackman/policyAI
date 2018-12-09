import os
import json
import election
import generator

# import tensorflow as tf

import keras.backend as K

from keras.models import Sequential
from keras.layers import Dense, Activation

# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

x = open("information/people.json", "r")
pop = json.load(x)
x.close()

c = 100

x = generator.policyGen(count=c)
y = generator.publicOpinion(pop, x)
x = generator.policyGen(count=c, data=True, translator=True, previous=x)

model = Sequential()
model.add(Dense(8, input_shape=(13,)))
model.add(Activation("relu"))
model.add(Dense(4, input_shape=(8,)))
model.add(Activation("relu"))
model.add(Dense(1, input_shape=(4,)))
model.add(Activation("relu"))

model.compile(optimizer="rmsprop", loss="mse", metrics=['mae'])

scale = int(0.8*c)

model.fit(x[:scale], y[:scale], epochs=5, batch_size=4, verbose=1)

print(model.evaluate(x[scale:], y[scale:]))
