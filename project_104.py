import csv
from collections import Counter
with open('height-weight.csv',newline = '') as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)    

newData = []
for i in range(len(fileData)):
    n_num = fileData[i][2]
    newData.append(float(n_num))

#getting the mean
n = len(newData)
total = 0
for x in newData:
    total += x
mean = total/n
print("Mean is: "+ str(mean))

#median
newData.sort()
if n % 2 == 0:
    median1 = float(newData[n//2])
    median2 = float(newData[n//2-1])
    median = (median1 + median2)/2
else:
    median = newData[n//2]
print("Median is: " + str(median))   

#mode
data  = Counter(newData)
mode_data_for_range = {
                        "90-110": 0,
                        "110-130": 0,
                        "130-150": 0
                    }
for weight, occurence in data.items():
    if 90 < float(weight) < 110:
        mode_data_for_range["90-110"] += occurence
    elif 110 < float(weight) < 130:
        mode_data_for_range["110-130"] += occurence
    elif 130 < float(weight) < 150:
        mode_data_for_range["130-150"] += occurence

mode_range, mode_occurence = 0, 0
for range, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)
print(f"Mode is -> {mode:2f}")
