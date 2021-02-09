#! /usr/bin/env python3
from math import exp, log, sqrt
import re
from datetime import date, time, datetime, timedelta

# 오늘 날짜와 년, 월, 일 요소들을 출력하기
today = date.today()
print("Output #41: today: {0!s}".format(today))
print("Output #42: {0!s}".format(today.year))
print("Output #43: {0!s}".format(today.month))
print("Output #44: {0!s}".format(today.day))
current_datetime = datetime.today()
print("Output #45: {0!s}".format(current_datetime))
