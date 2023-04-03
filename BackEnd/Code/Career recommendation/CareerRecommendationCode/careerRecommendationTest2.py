import csv


def prediction(stream, personality, academic_performance):
    careers = []
    with open('BackEnd\\Data\\CareerPredictions\\TrainSet.csv') as csvfile:
        csvreader = csv.DictReader(csvfile)

        # loop through rows
        for row in csvreader:
            if row['Stream'] == stream:
                if row['Personality'] == personality:
                    if row['Academic Performance'] == academic_performance:
                        careers.append(row['Career'])

    return careers


print(prediction('physical science', 'lively', 'Average'))
