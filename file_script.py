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

print("Output #141:")
inputPath = sys.argv[1]
for input_file in glob.glob(os.path.join(inputPath, '*.txt')):
    with open(input_file, 'r', newline='') as filereader:
        for row in filereader:
            print("{}".format(row.strip()))

