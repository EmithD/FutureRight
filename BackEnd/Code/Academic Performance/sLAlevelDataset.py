import pandas as pd
import numpy

# # replace() syntax
# DataFrame.replace(to_replace=None, value=None, inplace=False, limit=None, regex=False, method='pad')

data = pd.read_csv("BackEnd\\Data\\SLALevelDataset\\al_results_2020.csv")
# replacing values
data['sub1'].replace(['POLITICAL SCIENCE', 'ECONOMICS ','ISLAM','HISTORY OF SRI LANKA & EUROPE','COMMUNICATION & MEDIA STUDIES','GEOGRAPHY',
                       'HOME ECONOMICS','INFORMATION & COMMUNICATION TECHNOLOGY','PHYSICS','LOGIC & SCIENTIFIC METHOD','HISTORY OF SRI LANKA & INDIA',
                       'CHEMISTRY','ART','AGRICULTURAL SCIENCE','BUSINESS STUDIES','CHRISTIANITY','MATHEMATICS','ISLAMIC CIVILIZATION','HINDU CIVILIZATION',
                       'BIO SYSTEMS TECHNOLOGY','BUSINESS STATISTICS','BUDDHIST CIVILIZATION','CHRISTIAN CIVILIZATION','GREEK & ROMAN CIVILIZATION',
                       'HISTORY OF SRI LANKA & MODERN WORLD','DRAMA AND THEATRE (SINHALA)','BUDDHISM','ACCOUNTING','DANCING(INDIGENOUS)','FOOD TECHNOLOGY',
                       'ELECTRICAL,ELECTRONIC AND IT','COMBINED MATHEMATICS','ORIENTAL MUSIC','ENGLISH','BIOLOGY','CIVIL TECHNOLOGY','AGRO TECHNOLOGY',
                       'SINHALA','ENGINEERING TECHNOLOGY','HINDUISM','WESTERN MUSIC','MECHANICAL TECHNOLOGY','TAMIL','PALI','BIO-RESOURCE TECHNOLOGY',
                       'CARNATIC MUSIC','DANCING(BHARATHA)'],
                        [0, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,
                         26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46], inplace=True)


data['sub1_r'].replace(['A', 'B ','C','S','F','Abent','Withheld'],
                        [0, 1,2,3,4,5,6], inplace=True)

data['stream'].replace(['ARTS', 'COMMERCE ','PHYSICAL SCIENCE','BIOLOGICAL SCIENCE','ENGINEERING TECHNOLOGY','BIOSYSTEMS TECHNOLOGY','NON','-'],
                        [0, 1,2,3,4,5,6,7], inplace=True)
print(data.values)
