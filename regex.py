import re
hand = open('C:\\Users\\mattr\\Desktop\\python-code\\data\\regex_sum_324255.txt')
sumthem = 0
for line in hand:
    line = line.rstrip()
    x = re.findall('[0-9]\S*', line)
    for i in x:
        i = int(i)
        sumthem = sumthem + i
print sumthem
