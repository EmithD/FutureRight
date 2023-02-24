import datasetClass

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

modelLogReg = LogisticRegression(max_iter=1000)
modelLogReg.fit(datasetClass.main_train_array_X, datasetClass.main_train_y)

joblib.dump(modelLogReg, 'Backend\\Models\\PersonalityTestLogisticRegression.joblib')

predictionsLogReg = modelLogReg.predict(datasetClass.main_test_X)

# Code for custom values
# predictionTest = modelLogReg.predict([[1, 18, 8, 7, 6, 9, 7]])
# print(predictionTest)

score = accuracy_score(datasetClass.test_y, predictionsLogReg)
print("Logistic Regression = ", score)