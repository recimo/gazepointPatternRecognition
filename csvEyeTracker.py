import csv
import os

def csvFile(data):
    if os.path.isfile('./eyeTrackerData.csv'):
        with open('eyeTrackerData.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(data)

        csvFile.close()
    else:
        with open('eyeTrackerData.csv', 'wb') as csvFile:
            filewriter = csv.writer(csvFile, delimiter='', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvFile.close()

