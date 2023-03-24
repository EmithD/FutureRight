import pandas as pd
import numpy

# # replace() syntax
# DataFrame.replace(to_replace=None, value=None, inplace=False, limit=None, regex=False, method='pad')

data = pd.read_csv("BackEnd\\Data\\SLALevelDataset\\al_results_2020.csv")

# make a copy of the original dataframe
edited = data.copy()

# replacing values in 'stream' column
edited['stream'].replace(['ARTS', 'COMMERCE', 'PHYSICAL SCIENCE', 'BIOLOGICAL SCIENCE', 'ENGINEERING TECHNOLOGY',
                          'BIOSYSTEMS TECHNOLOGY', 'NON', '-'], [0, 1, 2, 3, 4, 5, 6, 7], inplace=True)

# replacing values in 'sub1' column
edited['sub1'].replace(['POLITICAL SCIENCE','ECONOMICS','ISLAM','HISTORY OF SRI LANKA & EUROPE','COMMUNICATION & MEDIA STUDIES','GEOGRAPHY',
'HOME ECONOMICS','INFORMATION & COMMUNICATION TECHNOLOGY','PHYSICS','LOGIC & SCIENTIFIC METHOD','HISTORY OF SRI LANKA & INDIA','CHEMISTRY','ART',
'AGRICULTURAL SCIENCE','BUSINESS STUDIES','CHRISTIANITY','MATHEMATICS','ISLAMIC CIVILIZATION','HINDU CIVILIZATION','BIO SYSTEMS TECHNOLOGY','BUSINESS STATISTICS',
'BUDDHIST CIVILIZATION','CHRISTIAN CIVILIZATION','GREEK & ROMAN CIVILIZATION','HISTORY OF SRI LANKA & MODERN WORLD','DRAMA AND THEATRE (SINHALA)','BUDDHISM',
'ACCOUNTING','DANCING(INDIGENOUS)','FOOD TECHNOLOGY','ELECTRICAL,ELECTRONIC AND IT','COMBINED MATHEMATICS','ORIENTAL MUSIC','ENGLISH','BIOLOGY','CIVIL TECHNOLOGY',
'AGRO TECHNOLOGY','SINHALA','ENGINEERING TECHNOLOGY','HINDUISM','WESTERN MUSIC','MECHANICAL TECHNOLOGY','TAMIL','PALI','BIO-RESOURCE TECHNOLOGY',
'CARNATIC MUSIC','DANCING(BHARATHA)'],
                       [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46], inplace=True)

#replacing values in 'sub1_r' column
edited['sub1_r'].replace(['A', 'B', 'C', 'S', 'F', 'Absent', 'Withheld'], [0, 1, 2, 3, 4, 5, 6], inplace=True)

# replacing values in 'sub2' column
edited['sub2'].replace(['DANCING(BHARATHA)','CARNATIC MUSIC','BUSINESS STUDIES','HINDU CIVILIZATION','CHRISTIANITY','ART','ISLAM',
'POLITICAL SCIENCE','COMMUNICATION & MEDIA STUDIES','HISTORY OF SRI LANKA & EUROPE','LOGIC & SCIENTIFIC METHOD',
'HOME ECONOMICS','GEOGRAPHY','ECONOMICS','CHEMISTRY','COMBINED MATHEMATICS','DRAMA AND THEATRE (SINHALA)','ENGLISH',
'BUSINESS STATISTICS','HISTORY OF SRI LANKA & INDIA','DANCING(INDIGENOUS)','AGRICULTURAL SCIENCE','ENGINEERING TECHNOLOGY',
'BIO SYSTEMS TECHNOLOGY','BUDDHIST CIVILIZATION','CHRISTIAN CIVILIZATION','CIVIL TECHNOLOGY','DRAMA AND THEATRE (TAMIL)',
'ACCOUNTING','ISLAMIC CIVILIZATION','TAMIL','SCIENCE FOR TECHNOLOGY','SINHALA','INFORMATION & COMMUNICATION TECHNOLOGY',
'FRENCH','CHINESE','GREEK & ROMAN CIVILIZATION','HISTORY OF SRI LANKA & MODERN WORLD','ORIENTAL MUSIC','PALI','BUDDHISM',
'AGRO TECHNOLOGY','GERMAN','WESTERN MUSIC','BIOLOGY','HINDI','MATHEMATICS','SANSKRIT','FOOD TECHNOLOGY','BIO-RESOURCE TECHNOLOGY',
'ELECTRICAL,ELECTRONIC AND IT','DRAMA AND THEATRE (ENGLISH)','HINDUISM','MECHANICAL TECHNOLOGY','RUSSIAN','ARABIC','HIGHER MATHEMATICS'],
[46,45,14,18,15,12,2,0,4,3,9,6,5,1,11,31,25,33,20,10,28,13,38,19,21,22,35,47,27,17,42,48,37,7,49,50,23,24,32,43,26,36,51,40,34,52,16,
53,29,44,30,54,39,41,55,56,57], inplace=True)

#replacing values in 'sub2_r' column
edited['sub2_r'].replace(['A', 'B', 'C', 'S', 'F', 'Absent', 'Withheld'], [0, 1, 2, 3, 4, 5, 6], inplace=True)

# replacing values in 'sub3' column
edited['sub3'].replace(['TAMIL','ACCOUNTING','ISLAM','ART','CHRISTIANITY','COMMUNICATION & MEDIA STUDIES','SINHALA','HOME ECONOMICS','COMBINED MATHEMATICS',
'INFORMATION & COMMUNICATION TECHNOLOGY','BIOLOGY','HISTORY OF SRI LANKA & EUROPE','BUSINESS STUDIES','FRENCH','DRAMA AND THEATRE (SINHALA)','ENGLISH','SCIENCE FOR TECHNOLOGY',
'DRAMA AND THEATRE (TAMIL)','ARABIC','ISLAMIC CIVILIZATION','BUDDHIST CIVILIZATION','CHRISTIAN CIVILIZATION','BUSINESS STATISTICS','ORIENTAL MUSIC','CHINESE','GERMAN','JAPANESE',
'GEOGRAPHY','LOGIC & SCIENTIFIC METHOD','DANCING(INDIGENOUS)','POLITICAL SCIENCE','GREEK & ROMAN CIVILIZATION','HISTORY OF SRI LANKA & MODERN WORLD','HISTORY OF SRI LANKA & INDIA',
'HINDI','WESTERN MUSIC','SANSKRIT','PALI','HINDUISM','MATHEMATICS','FOOD TECHNOLOGY','PHYSICS','ECONOMICS','HINDU CIVILIZATION','BUDDHISM','RUSSIAN','ENGINEERING TECHNOLOGY',
'BIO SYSTEMS TECHNOLOGY','CARNATIC MUSIC','CHEMISTRY','AGRO TECHNOLOGY','HIGHER MATHEMATICS','BIO-RESOURCE TECHNOLOGY','MECHANICAL TECHNOLOGY','DANCING(BHARATHA)','AGRICULTURAL SCIENCE',
'CIVIL TECHNOLOGY'],[42,27,2,12,15,4,37,6,31,7,34,3,14,49,25,33,48,47,56,17,21,22,20,32,50,51,58,5,9,28,0,23,24,10,52,40,
53,43,39,16,29,8,1,18,26,55,38,19,45,11,36,57,44,41,46,13,35],inplace=True)

#replacing values in 'sub2_r' column
edited['sub3_r'].replace(['A', 'B', 'C', 'S', 'F', 'Absent', 'Withheld'], [0, 1, 2, 3, 4, 5, 6], inplace=True)

#replacing values in 'sub2_r' column
edited['general_english_r'].replace(['A', 'B', 'C', 'S', 'F', 'Absent','Withheld'], [0, 1, 2, 3, 4, 5,6], inplace=True)

# Define a function to calculate the final result based on the subject results
def calculate_final_result(row):
    subjects = ['sub1_r', 'sub2_r', 'sub3_r', 'general_english_r']
    grades = [row[subject] for subject in subjects]
    if all(grade == 0 for grade in grades):
        return 'Excellent'
    elif all(grade <= 2 for grade in grades):
        return 'Good'
    elif all(grade <= 3 for grade in grades):
        return 'Average'
    else:
        return 'Below Average'

# Apply the function to each row in the dataframe and store the result in a new column
edited['final_result'] = edited.apply(calculate_final_result, axis=1)


# saving the edited dataframe
edited.to_csv("BackEnd\\Data\\SLALevelDataset\\al_edited_2020_new.csv")

