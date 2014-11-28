__author__ = 'pier'
import csv
import random
import numpy

j = 5
for i in range(0, 180):
    file = open('test' + str(i) + '.csv', "w")
    writer = csv.writer(file, delimiter="\t", quotechar='"', quoting=csv.QUOTE_ALL)
    for y in range(0, j):
        pippo = (random.gauss(0, 1), random.gauss(0, 1))
        writer.writerow(pippo)
    if i % 30 == 0:
        j += j
for i in range(0, 180):
    list1 = []
    list2 = []
    file = open('test' + str(i) + '.csv', "r")
    reader = csv.reader(file, delimiter="\t", quotechar='"', quoting=csv.QUOTE_ALL)
    for row in reader:
        list1.append(float(row[0]))
        list2.append(float(row[1]))
    file1 = open('test' + str(i) + '.csv', "a")
    writer = csv.writer(file1, delimiter='\t', quotechar='"', quoting=csv.QUOTE_NONE)
    res= numpy.corrcoef(list1, list2)[0, 1]
    writer.writerow(("The result is: ",str(res)))
