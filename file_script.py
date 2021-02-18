#! /usr/bin/env python3

from math import exp, log, sqrt
import re
from datetime import date, time, datetime, timedelta
from operator import itemgetter
import numpy as np
import sys
import glob
import os

#print("Output #139: ")
#input_file = sys.argv[1]
#filereader = open(input_file, 'r')
#for row in filereader:
#    print(row.strip())
#filereader.close()

#input_file = sys.argv[1]
#print("Output #140: ")
#with open(input_file, 'r', newline='') as filereader:
#    for row in filereader:
#        print("{}".format(row.strip()))

#print("Output #141:")
#inputPath = sys.argv[1]
#for input_file in glob.glob(os.path.join(inputPath, '*.txt')):
#    with open(input_file, 'r', newline='') as filereader:
#        for row in filereader:
#            print("{}".format(row.strip()))

#my_letters = ['a','b','c','d','e','f','g','h','i','j']
#max_index = len(my_letters)
#output_file = sys.argv[1]
#filewriter = open(output_file, 'w')
#for index_value in range(len(my_letters)):
#    if index_value < (max_index-1):
#        filewriter.write(my_letters[index_value]+'\t')
#    else:
#        filewriter.write(my_letters[index_value]+'\n')
#filewriter.close()
#print("Output #142: Output written to file")

my_numbers = [0,1,2,3,4,5,6,7,8,9]
max_index = len(my_numbers)
output_file = sys.argv[1]
filewriter = open(output_file, 'a')
for index_value in range(len(my_numbers)):
    if index_value < (max_index-1):
        filewriter.write(str(my_numbers[index_value])+',')
    else:
        filewriter.write(str(my_numbers[index_value])+'\n')
filewriter.close()
print("Output #143: Output appended to file")


