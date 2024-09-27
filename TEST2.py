#ESERCIZIO NUMERO 7
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import pandas as pd


iris = load_iris()
X = iris.data 
y = iris.target  


df_iris = pd.DataFrame(X, columns=iris.feature_names)
df_iris['target'] = y
print(df_iris.head())  


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)


knn = KNeighborsClassifier(n_neighbors=3)  
knn.fit(X_train, y_train)


y_pred = knn.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)


print(f"Accuratezza: {accuracy:.2f}")



cm = confusion_matrix(y_test, y_pred)


ConfusionMatrixDisplay(cm, display_labels=iris.target_names).plot(cmap="Blues")
plt.title("Matrice di confusione")
plt.show()
