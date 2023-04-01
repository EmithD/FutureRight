import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

#data pre-processing
train_data = pd.read_csv("BackEnd\\Data\\SLALevelDataset\\Final_data_set\\Train.csv")
train_data_array = train_data.values
train_df = pd.DataFrame(train_data_array)
main_train_df = train_df[[0,1,2,3,4,5,6,7]]
main_train_array_X = main_train_df.values
main_train_y = train_df[8]

#converting into strings
for i in range (len(main_train_y)):
    main_train_y[i] = str(main_train_y[i])

#Test-train splitting Data
#X_train_split, X_test_split, y_train_split, y_test_split = train_test_split(main_train_y,main_train_df,test_size=0.2)
  
#Creating the model
academic_model = LogisticRegression(max_iter=5000)
#academic_model.fit(X_train_split,y_train_split)

#predictions = academic_model.predict(X_test_split)
#score = ac#curacy_score(y_test_split,predictions)
#print("Accuracy =", score )

test_data = pd.read_csv("BackEnd\\Data\\SLALevelDataset\\Final_data_set\\Test.csv")
test_data_values = test_data.values
test_df = pd.DataFrame(test_data_values)
test_X = test_df[[0,1,2,3,4,5,6,7]]
test_y = test_df[[8]]
main_test_X = test_X.values



academic_model.fit(main_train_array_X,main_train_y)
predictions = academic_model.predict(main_test_X)
score = accuracy_score(test_y,predictions)
print("Accuracy =", score )
# joblib.dump(academic_model, "BackEnd\\Models\\academicPerformance.joblib")
