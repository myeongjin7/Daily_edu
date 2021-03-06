from keras.models import Sequential
from keras.layers import Dense, LSTM, Conv2D, Activation, Dropout, Flatten, MaxPooling2D
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
iris = load_iris()

x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=5)

model = Sequential()
model.add(Dense(40, input_shape=(4,), activation = 'relu'))
model.add(Dropout(0.2))
model.add(Dense(20, activation = 'relu'))
model.add(Dropout(0.2))
model.add(Dense(10, activation = 'relu'))
model.add(Dropout(0.2))
model.add(Dense(3, activation = 'softmax'))

model.summary()

model.compile(optimizer='adam', loss = 'sparse_categorical_crossentropy', metrics = ['acc'])
model.fit(x_train, y_train, batch_size = 4, epochs = 50, validation_split = 0.2)

loss, acc = model.evaluate(x_test,y_test,batch_size=5)
print(f'loss : {loss} ,      acc : {acc}')


y_predict = model.predict(x_test)

for i in range(len(x_test)):
  print(f'real y :   {y_test[i]},  y_predict :   {np.argmax(y_predict[i])}')