import datasetClass

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

modelLogReg = LogisticRegression(max_iter=1000)
modelLogReg.fit(datasetClass.main_train_array_X, datasetClass.main_train_y)

predictionsLogReg = modelLogReg.predict(datasetClass.main_test_X)

score = accuracy_score(datasetClass.test_y, predictionsLogReg)
print("Logistic Regression = ", score)