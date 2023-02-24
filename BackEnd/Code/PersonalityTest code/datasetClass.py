import pandas as pd
from sklearn.model_selection import train_test_split

#PREPROCESSING ATTEMPT 1

#Training datasets
trainingDf = pd.read_csv('BackEnd\\Data\\PersonalityTest\\train.csv')
# trainingDf['Gender'].replace({'Male':1, 'Female':0}, inplace=True)
trainingX = trainingDf.drop(columns=['Personality (Class label)', 'Gender', 'Age'])
trainingy = trainingDf["Personality (Class label)"]

#Testing datasets
testingDf = pd.read_csv('BackEnd\\Data\\PersonalityTest\\test.csv')
# testingDf['Gender'].replace({'Male':1, 'Female':0}, inplace=True)
testingX = testingDf.drop(columns=['Personality (class label)', 'Gender', 'Age'])
testingy = testingDf["Personality (class label)"]

#Test_Train splitting the Training dataset
X_train_split, X_test_split, y_train_split, y_test_split= train_test_split(trainingX, trainingy, test_size=0.2)

#####################################################################################################################################
#PREPROCESSING ATTEMPT 2
#Training datasets
train_data = pd.read_csv('BackEnd\\Data\\PersonalityTest\\train.csv')
train_data_array = train_data.values

for i in range(len(train_data_array)):
    if train_data_array[i][0] == 'Male':
        train_data_array[i][0] = 1
    else:
        train_data_array[i][0] = 0
        
train_df = pd.DataFrame(train_data_array)

main_train_df = train_df[[0,1,2,3,4,5,6]]
main_train_array_X = main_train_df.values

main_train_y = train_df[7]

for i in range(len(main_train_y)):
    main_train_y[i] = str(main_train_y[i])

#Testing Datasets
test_data = pd.read_csv('BackEnd\\Data\\PersonalityTest\\test.csv')
test_data_values = test_data.values

for i in range(len(test_data_values)):
    if test_data_values[i][0] == 'Male':
        test_data_values[i][0] = 1
    else:
        test_data_values[i][0] = 0

test_df = pd.DataFrame(test_data_values)

test_X = test_df[[0,1,2,3,4,5,6]]
test_y = test_df[[7]]
main_test_X = test_X.values
