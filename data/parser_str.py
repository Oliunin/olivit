import xml.etree.ElementTree as ET

fname = 'oct_agr.xml'
root = ET.fromstring(fname)
print(root)
