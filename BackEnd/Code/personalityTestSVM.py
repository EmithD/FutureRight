import datasetClass

from sklearn import svm
from sklearn.metrics import accuracy_score

modelSVMclf = svm.SVC(kernel='linear')

modelSVMclf.fit(datasetClass.trainingX, datasetClass.trainingy)

SVMPrediction = modelSVMclf.predict(datasetClass.testingX)

score = accuracy_score(datasetClass.testingy, SVMPrediction)
print("SVM = ", score)