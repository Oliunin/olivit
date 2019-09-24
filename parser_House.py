import sqlite3
import xml.etree.ElementTree as ET

#пишет в таблицу House в поле %tname% значение %v%
def sqlrecord (tname,v):
    cur.execute("INSERT INTO Houses ("+tname+") VALUES (?)",(v,))
#    conn.commit()

#словарь для парсинга xml houses.xml
conn = sqlite3.connect('olivit.sqlite')
cur = conn.cursor()
Houses = dict(ID=None,GisGUID=None,GisUniqueNumber=None,FiasGuid=None,
Type=None,Address=None,CadastrNumber=None,UsedYear=None,
TotalSquare=None,FloorCount=None,UndergroundFloorCount=None,CulturalHeritage=None,
OKTMOCode=None,OlsonTZ=None,State=None,LifeCycleStage=None)
cur.executescript('''DELETE TABLE IF EXISTS Houses''')

tree = ET.ElementTree(file='.\XML\houses.xml')
root = tree.getroot()

cur = conn.execute('select * from Houses')
tnames = list(map(lambda x: x[0], cur.description))
#print(tnames)

for housenode in tree.findall('./{http://sync.gkh.octonica.ru/main-sync}Houses/{http://sync.gkh.octonica.ru/main-sync}House/'):
    for k,v in Houses.items():
        if k == housenode.tag[39:]:
            v=housenode.text
            for tname in tnames:
                if tname == k:
                    print('columnname:',tname,'dict key:',k,'dict value:',v)
                    print(type(tname),type(v))
                    sqlrecord(tname,v)
