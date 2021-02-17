#! /usr/bin/env python3

from math import exp, log, sqrt
import re
from datetime import date, time, datetime, timedelta
from operator import itemgetter
import numpy as np

def getMean(numericValues):
    return sum(numericValues)/len(numericValues) if len(numericValues) > 0 \
    else float('nan')

my_list = [1,2,3,4,5,6,7,8,9,10]
print("Output #135 (mean): {!s}".format(getMean(my_list)))
print("Output #136 (mean): {!s}".format(np.mean(my_list)))

def getMean2(numericValues):
    return sum(numericValues)/len(numericValues)

my_list2 = [ ]

try:
    print("Output #137: {}".format(getMean2(my_list2)))
except ZeroDivisionError as detail:
    print("Output #137 (Error): {}".format(float('nan')))
    print("Output #137 (Error): {}".format(detail))

try:
    result = getMean2(my_list2)
except ZeroDivisionError as detail:
    print("Output #138 (Error): {}".format(float('nan')))
    print("Output #138 (Error): {}".format(detail))
else:
    print("Output #138 (The mean is): {}".format(result))
finally:
    print("Output #138 (Finally): The finally block is executed every time.")

