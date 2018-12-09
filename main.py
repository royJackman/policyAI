import os
import json
import election
import generator

import tensorflow as tf

# import keras.backend as K

# from keras.models import Sequential
# from keras.layers import Dense, Activation

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

x = open("information/people.json", "r")
pop = json.load(x)
x.close()

c = 10000

x = generator.policyGen(count=c)
y = generator.publicOpinion(pop, x)
x = generator.policyGen(count=c, data=True, translator=True, previous=x)

# model = Sequential()
# model.add(Dense(8, input_shape=(13,)))
# model.add(Activation("relu"))
# model.add(Dense(4, input_shape=(8,)))
# model.add(Activation("relu"))
# model.add(Dense(1, input_shape=(4,)))
# model.add(Activation("softmax"))

# model.compile(optimizer="rmsprop", loss="mae", metrics=['mae','accuracy'])

# scale = int(0.8*c)

# model.fit(x[:scale], y[:scale], epochs=20, batch_size=400, verbose=2)

# print(model.evaluate(x[scale:], y[scale:]))

