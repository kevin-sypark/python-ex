#! /usr/bin/env python3

from math import exp, log, sqrt
import re
from datetime import date, time, datetime, timedelta
from operator import itemgetter

# 리스트를 만들기 위해 대괄호를 사용한다
# len() 함수를 통해 리스트 내 원소의 수를 센다.
# max() 함수와 min() 함수는 최대/최소 값을 찾는다.
# count() 함수는 리스트 내 특정 값이 등장한 횟수를 센다.

a_list = [1, 2, 3]
print("Output #58: {}".format(a_list))
print("Output #59: a_list has {} elements.".format(len(a_list)))
print("Output #60: the maximum value in a_list is {}.".format(max(a_list)))
print("Output #61: the minimum vlaue in a_list is {}.".format(min(a_list)))
another_list = ['printer', 5, ['star', 'circle', 9]]
print("Output #62: {}.".format(another_list))
print("Output #63: another_list also has {} elements.".format(len(another_list)))
print("Output #64: 5 is another_list {} time.".format(another_list.count(5)))

# 리스트 내 특정 원소에 접근하려면 인덱스 이용하기
# [0]은 첫 번째 원소이다. [-1]은 마지막 원소이다.
print("Output #65: {}".format(a_list[0]))
print("Output #66: {}".format(a_list[1]))
print("Output #67: {}".format(a_list[2]))
print("Output #68: {}".format(a_list[-1]))
print("Output #69: {}".format(a_list[-2]))
print("Output #70: {}".format(a_list[-3]))
print("Output #71: {}".format(another_list[2]))
print("Output #72: {}".format(another_list[-1]))

print("Output #73: {}".format(a_list[0:2]))
print("Output #74: {}".format(another_list[:2]))
print("Output #75: {}".format(a_list[1:3]))
print("OUtput #76: {}".format(another_list[1:]))

a_new_list = a_list[:]
print("Output #77: {}".format(a_new_list))

a = 2 in a_list
print("Output #79: {}".format(a))
if 2 in a_list:
    print("Output #80: 2 is in {}.".format(a_list))
b = 6 not in a_list
print("Output #81: {}".format(b))
if 6 not in a_list:
    print("Output #82: 6 is not in {}.".format(a_list))

a_list.append(4)
a_list.append(5)
a_list.append(6)
print("Output #83: {}".format(a_list))
a_list.remove(5)
print("Output #84: {}".format(a_list))
a_list.pop()
print("Output #85-1: {}".format(a_list))
a_list.pop()
print("Output #85-2: {}".format(a_list))

a_list.reverse()
print("Output #86: {}".format(a_list))
a_list.reverse()
print("Output #87: {}".format(a_list))

unordered_list = [3, 5, 1, 7, 2, 8, 4, 9, 0 ,6]
print("Output #88: {}".format(unordered_list))
list_copy = unordered_list[:]
list_copy.sort()
print("Output #89: {}".format(list_copy))
print("Output #90: {}".format(unordered_list))

my_lists = [[1,2,3,4],[4,3,2,1],[2,4,1,3]]
my_lists_sorted_by_index_3 = sorted(my_lists, key=lambda index_value: index_value[3])
print("Output #91: {}".format(my_lists_sorted_by_index_3))

my_lists = [[123,2,2,444],[22,6,6,444],[354,4,4,678],[236,5,5,678],\
[578,1,1,290],[461,1,1,290]]
my_lists_sorted_by_index_3_and_0 = sorted(my_lists, key=itemgetter(3,0))
print("Output #92: {}".format(my_lists_sorted_by_index_3_and_0))
