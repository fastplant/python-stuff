import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter location: ')

print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'

tree = ET.fromstring(data)
counts = tree.findall('.//count')

counttotal = len(counts)
print 'Count: ', counttotal

total = 0
countval = 0
for i in counts:
    countval = int(i.text)
    total = countval + total
print 'Sum: ', total
