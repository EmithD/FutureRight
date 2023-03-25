import pandas as pd 

data=pd.read_csv("BackEnd\\Data\\CareerPredictions\\TrainSet.csv")
# make a copy of the original dataframe
edited2 = data.copy()
# replacing values in 'stream' column
edited2['Stream'].replace(['arts','commerce ', 'physical science', 'biological science', 'engineering technology',
                          'biosystems technology'], [0, 1, 2, 3, 4, 5], inplace=True)

#replacing values in the 'personality' column
edited2['Personality'].replace(['dependable ','serious','lively','responsible','extraverted'],
                                [0,1,2,3,4], inplace=True )

#replacing values in the 'Academic Performance' column
edited2['Academic Performance'].replace(['Excellent','Good','Average','Below Average'],
                                [0,1,2,3], inplace=True )

# saving the edited dataframe
edited2.to_csv("BackEnd\\Data\\CareerPredictions\\CareersEdited.csv")
