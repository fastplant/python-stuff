name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

count = dict()
lst = list()

for line in handle:
    line = line.rstrip()
    words = line.split()
    if len(line) != 0 and words[0] == 'From':
    	time = words[5].split(':')
        hr = time[0]
        count[hr] = count.get(hr,0) + 1

lst = sorted([(k,v) for k,v in count.items()])
for k,v in lst:
    print k,v