import datasetClass

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

modelKNN = KNeighborsClassifier()
modelKNN.fit(datasetClass.main_train_array_X, datasetClass.main_train_y)

predictionKNN = modelKNN.predict(datasetClass.main_test_X)

score = accuracy_score(datasetClass.test_y, predictionKNN)
print("KNN = ", score)