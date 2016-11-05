# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
count = raw_input('Enter count: ')
count = int(count)
position = raw_input('Enter position: ')
position = int(position)

html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')

loopcount = 0


print 'Retrieving: ', url

while count > loopcount:
    positioncount = 0
    for tag in tags:
        hrefval = tag.get('href', None)
        positioncount = positioncount + 1
        if position == positioncount: break

    print 'Retrieving: ', hrefval
    html = urllib.urlopen(hrefval).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    loopcount = loopcount + 1
