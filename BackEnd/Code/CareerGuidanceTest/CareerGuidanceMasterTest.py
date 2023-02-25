import pandas as pd 
from sklearn.model_selection import train_test_split

data = pd.read_csv('BackEnd\\Data\\TestSet\\career_pred.csv')
data.drop(columns=['certifications', 'workshops', 'interested subjects', 'interested career area', 'Type of company want to settle in?', 'Interested Type of Books'])
data_array = data.values

# for i in range(len(data_array)):
#     if data_array[i][14] == 'yes':
#         data_array[i][14] = 1
#     else:
#         data_array[i][14] = 0
        
#     if data_array[i][15] == 'yes':
#         data_array[i][15] = 1
#     else:
#         data_array[i][15] = 0
        