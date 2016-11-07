import json
import urllib

#Ask user for URL, read it, and show how many chars retrieved
url = raw_input('Enter location: ')
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'

#JSON load string into a dictionary
info = json.loads(data)

total = 0

#Loop through the comments dictionary, get the counts, and add them
for item in info["comments"]:
    #print item
    count = item.get('count')
    total = count + total

print 'Sum:',total
