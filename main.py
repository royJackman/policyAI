import os
import sys
import json
import election
import generator

# import tensorflow as tf
import numpy as np
import keras.backend as K
import matplotlib.pyplot as plt

from IPython.display import SVG
from keras.utils import plot_model
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, GaussianNoise
from keras.utils.vis_utils import model_to_dot

# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

x = open("information/people.json", "r")
pop = json.load(x)
x.close()

c = 1000
e = 5
b = 40
v = 0.2

x = generator.policyGen(count=c)
y1 = generator.publicOpinion(pop, x)

elect = election.elect(pop,districts=[[7,2,1], [1,2,1], [9,2,1], [4,2,1], [53,2,1], [7,2,1], [5,2,1], [1,2,1], [27,2,1], [14,2,1], [2,2,1], [2,2,1], [18,2,1], [9,2,1], [4,2,1], [4,2,1], [6,2,1], [6,2,1], [2,2,1], [8,2,1], [9,2,1], [14,2,1], [8,2,1], [4,2,1], [8,2,1], [1,2,1], [3,2,1], [4,2,1], [2,2,1], [12,2,1], [3,2,1], [27,2,1], [13,2,1], [1,2,1], [16,2,1], [5,2,1], [5,2,1], [18,2,1], [2,2,1], [7,2,1], [1,2,1], [9,2,1], [36,2,1], [4,2,1], [1,2,1], [11,2,1], [10,2,1], [3,2,1], [8,2,1], [1,2,1]])

for i in pop.keys():
    pop[i]["politician"] = False

for i in elect.keys():
    winner = elect[i]["winner"]
    pop[winner["name"]]["politician"] = True

# print(pop[elect['d20_h1_r0']["winner"]["name"]])
house = {}
senate = {}

houseReps = [elect[race]["winner"]["name"] for race in list(filter(lambda l: "_h0_" in l, elect.keys()))]
senateReps = [elect[race]["winner"]["name"] for race in list(filter(lambda l: "_h1_" in l, elect.keys()))]

for rep in houseReps:
    house[rep] = pop[rep]

for rep in senateReps:
    senate[rep] = pop[rep]

# house = [pop[name] for name in [elect[race]["winner"]["name"] for race in list(filter(lambda l: "_h0_" in l, elect.keys()))]]
# senate = [pop[name] for name in [elect[race]["winner"]["name"] for race in list(filter(lambda l: "_h1_" in l, elect.keys()))]]

y2 = generator.publicOpinion(house, x)
y3 = generator.publicOpinion(senate, x)
x = generator.policyGen(count=c, data=True, translator=True, previous=x)

y1 = np.array(y1)
y2 = np.array(y2)
y3 = np.array(y3)

print(y1.shape,y2.shape,y3.shape)
y = np.vstack((y1.reshape(1,-1),y2.reshape(1,-1),y3.reshape(1,-1))).T
print(y.shape)

model1 = Sequential()
model2 = Sequential()
model3 = Sequential()

model1.add(Dense(10, input_shape=(13,)))
model1.add(Activation("relu"))
model1.add(GaussianNoise(stddev=1.0))
model1.add(Dense(5, input_shape=(10,)))
model1.add(Activation("relu"))
model1.add(Dense(3, input_shape=(5,)))
model1.add(Activation("relu"))

model2.add(Dense(100, input_shape=(13,)))
model2.add(Activation("relu"))
model2.add(Dense(3, input_shape=(100,)))
model2.add(Activation("relu"))

model3.add(Dense(50,input_shape=(13,)))
model3.add(Activation("sigmoid"))
model3.add(GaussianNoise(stddev=1.0))
model3.add(Dense(24,input_shape=(50,)))
model3.add(Activation("sigmoid"))
model3.add(Dropout(24))
model3.add(Dense(12,input_shape=(24,)))
model3.add(Activation("sigmoid"))
model3.add(Dense(3,input_shape=(12,)))

model1.compile(optimizer="rmsprop", loss="mse")
model2.compile(optimizer="adam", loss="mae")
model3.compile(optimizer="adagrad", loss="mse")

scale = int(0.8*c)

history1 = model1.fit(x, y, epochs=e, batch_size=b, validation_split=v, verbose=1)
history2 = model2.fit(x, y, epochs=e, batch_size=b, validation_split=v, verbose=1)
history3 = model3.fit(x, y, epochs=e, batch_size=b, validation_split=v, verbose=1)

acc1 = model1.evaluate(x[scale:,:], y[scale:,:])
acc2 = model2.evaluate(x[scale:,:], y[scale:,:])
acc3 = model3.evaluate(x[scale:,:], y[scale:,:])
print(acc1,acc2,acc3)

# plot_model(model, to_file='model.png')
# SVG(model_to_dot(model).create(prog='dot', format='svg'))

plt.plot(history1.history['loss'])
plt.plot(history2.history['loss'])
plt.plot(history3.history['loss'])
plt.plot(history1.history['val_loss'])
plt.plot(history2.history['val_loss'])
plt.plot(history3.history['val_loss'])
# plt.plot(acc.history['loss'])
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Average','Perceptron','StatesLayer','avgVal','pctVal','stlVal'], loc='upper right')
plt.show()
