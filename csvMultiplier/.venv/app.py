import csv
with open('C:/Users/Kamien/Desktop/keypoint.csv', newline='') as csvfileread, open('C:/Users/Kamien/Desktop/keypointoutput.csv',  mode='w', newline='') as csvfilewrite:
    writer = csv.writer(csvfilewrite, delimiter=',')
    reader = csv.reader(csvfileread, delimiter=',')
    step = 0.99
    for row in reader:
        i = 1
        while i <= 10:
            for column in range(len(row)):
                if column > 2 and column % 2 != 0:
                    a = float(row[column])
                    a = a * step
                    row[column] = str(a)
            i += 1
            writer.writerow(row)
        i = 1
        while i <= 10:
            for column in range(len(row)):
                if column > 2 and column % 2 == 0:
                    a = float(row[column])
                    a = a * step
                    row[column] = str(a)
            i += 1
            writer.writerow(row)