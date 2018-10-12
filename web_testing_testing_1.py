import sys
from datetime import datetime
date = datetime.today()

print(date)
test_nummer = -1
if test_nummer == 0:
    file1 = open("filetest.txt","r")
    if file1.mode == 'r':
        inside1 = file1.read()
        print(inside1 + ".")

if test_nummer == 1:
    file2 = open("filetest.txt", "a")
    if file2.mode == "a":
        for i in range(20):
            file2.write("\n----------------------------------------\nThis is a test\n---------------------------\n")