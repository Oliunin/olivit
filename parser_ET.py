import xml.etree.ElementTree as ET
import re
import sqlite3

conn = sqlite3.connect('olivit.sqlite')
cur = conn.cursor()
# Создаю таблицы
cur.executescript('''
DROP TABLE IF EXISTS Houses;
DROP TABLE IF EXISTS Agreements;
DROP TABLE IF EXISTS Services;

CREATE TABLE Houses (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    FIASHouseGuid  TEXT UNIQUE
);

CREATE TABLE Agreements (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    FIASHouseGuid   TEXT UNIQUE,
    StartDate TEXT,
    Status TEXT,
    IsManagedByContract TEXT
);

CREATE TABLE Services (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    GisGUID     TEXT,
    GisUniqueNumber   INTEGER,
    Kind        TEXT,
    IsActual TEXT,
    StartDate TEXT,
    EndDate TEXT,
    Name TEXT,
    MeasureOKEICode
)
''')

tree = ET.ElementTree(file='oct_agr.xml')
root = tree.getroot()
#print(root)
#print(root.tag)
#print(root.text)
#print(root.attrib)
#ET.dump(root)
for item in tree.iter():
#    ET.dump(item)
    if item.tag=='{http://sync.gkh.octonica.ru/main-sync}ManagedObject':
        print(type(item))
        print(item.attrib)
        print(item.child)
        FIASHouseGuid=item.find('{http://sync.gkh.octonica.ru/main-sync}FIASHouseGuid').text
        StartDate=item.find('{http://sync.gkh.octonica.ru/main-sync}StartDate').text
        Status=item.find('{http://sync.gkh.octonica.ru/main-sync}StartDate').text
        IsManagedByContract=item.find('{http://sync.gkh.octonica.ru/main-sync}IsManagedByContract').text
#        print(FIASHouseGuid,StartDate, Status, IsManagedByContract)
#        cur.execute('''INSERT OR REPLACE INTO Agreements
#            (FIASHouseGuid, StartDate, Status, IsManagedByContract) VALUES ( ?, ?, ?, ? )''',
#
#        conn.commit()

#    elif item.tag=='{http://sync.gkh.octonica.ru/main-sync}DocumentType':
#        ET.dump(item)
#        DocumentType=item.find('{http://sync.gkh.octonica.ru/main-sync}StartDate').text
#        Name=item.find('{http://sync.gkh.octonica.ru/main-sync}Name').text
#        Description=item.find('{http://sync.gkh.octonica.ru/main-sync}Description').text
#        Date=item.find('{http://sync.gkh.octonica.ru/main-sync}Date').text
#        Status=item.find('{http://sync.gkh.octonica.ru/main-sync}Status').text
#        print(DocumentType, Name, Description, Date, Status)
#    elif item.tag=='{http://sync.gkh.octonica.ru/main-sync}Document': ET.dump(item)
    elif item.tag=='{http://sync.gkh.octonica.ru/main-sync}ServiceType':
#        ET.dump(item)
        ID=item.find('{http://sync.gkh.octonica.ru/main-sync}ID').text
        GisGUID=item.find('{http://sync.gkh.octonica.ru/main-sync}GisGUID').text
        GisUniqueNumber=item.find('{http://sync.gkh.octonica.ru/main-sync}GisUniqueNumber').text
        Kind=item.find('{http://sync.gkh.octonica.ru/main-sync}Kind').text
        IsActual=item.find('{http://sync.gkh.octonica.ru/main-sync}IsActual').text
        StartDate=item.find('{http://sync.gkh.octonica.ru/main-sync}StartDate').text
        EndDate=item.find('{http://sync.gkh.octonica.ru/main-sync}EndDate').text
#        try:
#            Name=item.find('{http://sync.gkh.octonica.ru/main-sync}Name').text
#            MeasureOKEICode=item.find('{http://sync.gkh.octonica.ru/main-sync}MeasureOKEICode').text
#            print(ID,GisGUID, GisUniqueNumber, MeasureOKEICode, Kind, IsActual, StartDate, EndDate)
#            cur.execute('''INSERT OR REPLACE INTO Services
#                        (ID,GisGUID, GisUniqueNumber, Kind, IsActual, StartDate, EndDate)
#                        VALUES ( ?, ?, ?, ?, ?, ?, ?, ? )''',
#                        (ID,GisGUID, GisUniqueNumber, MeasureOKEICode, Kind, IsActual, StartDate, EndDate) )
#            continue
#        print(ID,GisGUID, GisUniqueNumber, Name, MeasureOKEICode, Kind, IsActual, StartDate, EndDate)
#        cur.execute('''INSERT OR REPLACE INTO Services
#                    (ID,GisGUID, GisUniqueNumber, Name, MeasureOKEICode, Kind, IsActual, StartDate, EndDate)
#                    VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ? )''',
#                    (ID,GisGUID, GisUniqueNumber, Name, MeasureOKEICode, Kind, IsActual, StartDate, EndDate) )
#    elif item.tag=='{http://sync.gkh.octonica.ru/main-sync}AssociatedDocuments':
#        ET.dump(item)
#        ID=item.iterfind('{http://sync.gkh.octonica.ru/main-sync}ID')
#        print(ID)
#        for child in item.iter('{http://sync.gkh.octonica.ru/main-sync}Document'):
#            ID=child.find('{http://sync.gkh.octonica.ru/main-sync}ID').text
#            DocumentType=child.find('{http://sync.gkh.octonica.ru/main-sync}DocumentType').text
#            print(child)
#print(root.text)
#for child in root:
#    print('tag:',child.tag,'atrib:',child.attrib,'text:',child.text)
#    print('tag type:',type(child.tag))
#    print('atrib type:',type(child.attrib))
#    print('text type:',type(child.text))

#for child_of_root in root:
#        print(child_of_root.tag, child_of_root.keys(), child_of_root.items())


#for item in tree.iter():
# смотрим древо
#    print('Find:',
#    'tag:', item.tag, type(item.tag),
#    'attrib:', item.attrib, type(item.attrib),
#    'text:', item.text, type(item.text))

#отрежу так, потом заменю на regular expression
#    print(type(item))
#    tag=item.tag[39:]
#    print('tag:',tag)
#    attrib=item.attrib
#    print('attrib:',attrib)
#    text=item.text
#    print('text:',text)
#    if tag == 'DocumentType' and text == 'Charter':
#        print('tag:',tag)
#        print('attrib:',attrib)
#        print('text:',text)

#    print(type(item))
#    print('tag:',item.tag)
#    print('attrib:',item.attrib)
#    print('text:',item.text)
#    for child in item:
#        print('child type:',type(child))
#        print('tag:',child.tag)
#        print('attrib:',child.attrib)
#        print('text:',child.text)
#    print(item.SubElement())


# Ищем нужный тэг
#    if item.tag =='{http://sync.gkh.octonica.ru/main-sync}ID':
#        print('tag',item.tag)
#        print('atrib',item.attrib)
#        print('text',item.text)
