import pandas as pd 

train_data = pd.read_csv('BackEnd\\Data\\CareerPredictions\\TestTrain\\Train.csv')
train_data_array = train_data.values

train_df = pd.DataFrame(train_data_array)

main_train_df = train_df[[0, 1, 2]]
main_train_array_X = main_train_df.values

main_train_y = train_df[3]

for i in range(len(main_train_y)):
    main_train_y[i] = str(main_train_y)
    
test_data = pd.read_csv('BackEnd\\Data\\CareerPredictions\\TestTrain\\Test.csv')
test_data_values = test_data.values

test_df = pd.DataFrame(test_data_values)

test_X = test_df[[0,1,2]]
test_y = test_df[[3]]
main_test_X = test_X.values


#Model creation
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

careerPredModel = LogisticRegression(max_iter=1000)
careerPredModel.fit(main_train_array_X, main_train_y)

predictions = careerPredModel.predict([[0, 0, 3]])
print(predictions)
# score = accuracy_score(test_y, predictions)
# print("Accuracy = ", score)