import re

f = open('nodes_name.txt', 'r')
for line in f:
#    print(line)
    lnodename=re.findall('=.\w+',line)
    nodename=lnodename[0]
    print(nodename[2:])
