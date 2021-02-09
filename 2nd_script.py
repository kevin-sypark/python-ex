#! /usr/bin/env python3
from math import exp, log, sqrt
import re

# 문자열 내에 등장하는 패턴의 횟수를 세기
string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
pattern = re.compile(r"The", re.I)
count = 0
for word in string_list:
    if pattern.search(word):
        count += 1
print("Output #38: {0:d}".format(count))

# 문자열 내에서 발견된 패턴 출력하기
string = "The quick brown for jumps over the lazy dog."
string_list = string.split()
pattern = re.compile(r"(?P<match_word>The)", re.I)
print("output #39:")
for word in string_list:
    if pattern.search(word):
        print("{0:s}".format(pattern.search(word).group('match_word')))

# 문자열 내 "the"를 "a"로 대체하기
string = "The quick brown fox jumps over the lazy dog."
string_to_find = r"The"
pattern = re.compile(string_to_find, re.I)
print("Outout #40: {:s}".format(pattern.sub("a", string)))
