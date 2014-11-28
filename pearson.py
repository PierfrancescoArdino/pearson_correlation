__author__ = 'pier'
import csv
import random
import numpy
import sys
def run(name_file):
        file =open(name_file,"r")
        reader = csv.reader(file, delimiter= "\t",quotechar='"', quoting=csv.QUOTE_ALL)
        list1 = []
        list2 = []
        for row in reader:
            list1.append(float(row[0]))
            list2.append(float(row[1]))
        res= numpy.corrcoef(list1, list2)[0, 1]
        print(("The result is: {0:s}".format(str(res))))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print ("Error, usage: pearson.py <csv_file>")
        exit(1)
    run(sys.argv[1])
