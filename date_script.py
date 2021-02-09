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

# To calculate date using timedelta function
one_day = timedelta(days=-1)
yesterday = today + one_day
print("Output #46: yesterday: {0!s}".format(yesterday))
eight_hours = timedelta(hours=-8)
print("Output #47: {0!s} {1!s}".format(eight_hours.days, eight_hours.seconds))

# 두 날짜 사이의 날짜 차이를 계산하기
date_diff = today - yesterday
print("Output #48: {0!s}".format(date_diff))
print("Output #49: {0!s}".format(str(date_diff).split()[0]))

# date 객체를 특정 형식의 문자열로 만들기
print("Output #50: {:s}".format(today.strftime('%m/%d/%Y')))
print("Output #51: {:s}".format(today.strftime('%b %d, %Y')))
print("Output #52: {:s}".format(today.strftime('%B %d, %Y')))
print("Output #53: {:s}".format(today.strftime('%Y-%m-%d')))

# 날짜 문자열로부터 특정 형식의 datetime 객체를 생성하기
date1 = today.strftime('%m/%d/%Y')
date2 = today.strftime('%b %d, %Y')
date3 = today.strftime('%Y-%m-%d')
date4 = today.strftime('%B %d, %Y')

# 다른 date 형식을 지닌 4가지 문자열에 기반한
# 각각 2종류의 datetime 객체들과 data 객체들
print("Output #54: {!s}".format(datetime.strptime(date1, '%m/%d/%Y')))
print("Output #55: {!s}".format(datetime.strptime(date2, '%b %d, %Y')))

# 날짜 부문만 출력하기
print("Output #56: {!s}".format(datetime.date(datetime.strptime(date3, '%Y-%m-%d'))))
print("Output #57: {!s}".format(datetime.date(datetime.strptime(date4, '%B %d, %Y'))))
