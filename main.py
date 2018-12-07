import json
import election
import generator

import keras.backend as K

from keras.models import Sequential
from keras.layers import Dense, Activation

x = open("information/people.json", "r")
pop = json.load(x)
x.close()

x = generator.policyGen(count=100)
y = generator.publicOpinion(pop, x)
x = generator.policyGen(count=100, data=True, translator=True, previous=x)

model = Sequential()
model.add(Dense(10, input_shape=13))
model.add(Activation("relu"))
model.add(Dense(6, input_shape=10))
model.add(Activation("relu"))
model.add(Dense(1, input_shape=6))
model.add(Activation("softmax"))

model.compile(optimizer="rmsprop", loss="mse")

model.fit(x[:80], y[:80])

print(model.evaluate(x[80:], y[80:]))

