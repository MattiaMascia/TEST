#ESERCIZIO NUMERO 10
import os
import warnings

# Imposta il livello di log di TensorFlow per sopprimere i messaggi INFO e WARNING
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # 0 = Tutti i log, 1 = INFO, 2 = WARNING, 3 = ERROR

# Disabilita specifici avvisi di Keras
warnings.filterwarnings('ignore', category=UserWarning, module='keras.layers.core.dense')

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix, classification_report


(X_train, y_train), (X_test, y_test) = mnist.load_data()

#normalizzo i dati X 
X_train = X_train.astype('float32') / 255
X_test = X_test.astype('float32') / 255

#appiattisco i dati in un vettore dato che sono valori di pixel all'interno di immagini
X_train = X_train.reshape(-1, 28*28)
X_test = X_test.reshape(-1, 28*28)

#converto in categorie le y
y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)

#scelgo un modello sequenziale 
model = Sequential()
model.add(Dense(units=128, activation='relu', input_shape=(784,)))#784 cause 28x28
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=10, activation='softmax'))

#compilo il modello
model.compile(optimizer='adam',
              loss='categorical_crossentropy',#viene utilizzata per problemi di classificazione multi-classe
              metrics=['accuracy'])#misuro l'accuratezza durante la compilazione


# Addestramento del modello
history = model.fit(X_train, y_train,
                    epochs=1,#ho poco tempo
                    batch_size=32,#nuìmero di passaggi da fare per ogni epoca
                    validation_split=0.1)


# Valutazione del modello
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f'Perdita sul test set: {test_loss:.4f}')
print(f'Accuratezza sul test set: {test_accuracy:.4f}')

# Predizioni
predictions = model.predict(X_test)
predicted_classes = np.argmax(predictions, axis=1)
true_classes = np.argmax(y_test, axis=1)


#matrice di confusione per valutare il modello
conf_matrix = confusion_matrix(true_classes, predicted_classes)
plt.figure(figsize=(10,8))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.title('Matrice di Confusione')
plt.xlabel('Classe Predetta')
plt.ylabel('Classe Vera')
plt.show()


