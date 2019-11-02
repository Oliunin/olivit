import sqlite3
import xml.etree.ElementTree as ET

#функция пишет в таблицу House в поле %tname% значение %v%
#def sqlrecord (tname,v):
#    cur.execute("INSERT INTO Houses ("+tname+") VALUES (?)",(v,))
#    conn.commit()

#подключаем базу
conn = sqlite3.connect('olivit.sqlite')
cur = conn.cursor()

#создаем словарь для парсинга xml houses.xml
Houses = dict(ID=None,GisGUID=None,GisUniqueNumber=None,FiasGuid=None,
Type=None,Address=None,CadastrNumber=None,UsedYear=None,
TotalSquare=None,FloorCount=None,UndergroundFloorCount=None,CulturalHeritage=None,
OKTMOCode=None,OlsonTZ=None,State=None,LifeCycleStage=None)

#парсим XML в дерево
tree = ET.ElementTree(file='.\XML\houses.xml')
root = tree.getroot()

#получаем список полей таблицы
#cur = conn.execute('select * from Houses')
#tnames = list(map(lambda x: x[0], cur.description))
#print(tnames)

#находим ноду дома
for housenode in tree.findall('./{http://sync.gkh.octonica.ru/main-sync}Houses/{http://sync.gkh.octonica.ru/main-sync}House/'):
    for k,v in Houses.items():
        if k == housenode.tag[39:]:
            v=housenode.text
            Houses[k]=v
#проверяем НЕПУСТОЙ словарь
for k,v in Houses.items():
    print(k,'value:', Houses.get(k))

#пробуем писать дом в базу
try:
    cur.execute('''INSERT INTO Houses (ID,GisGUID,GisUniqueNumber,FiasGuid,
    Type,Address,CadastrNumber,UsedYear,TotalSquare,FloorCount,UndergroundFloorCount,
    CulturalHeritage,OKTMOCode,OlsonTZ,State,LifeCycleStage) VALUES
    (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
    (Houses.get('ID'),Houses.get('GisGUID'),Houses.get('GisUniqueNumber'),Houses.get('FiasGuid'),
    Houses.get('Type'),Houses.get('Address'),Houses.get('CadastrNumber'),Houses.get('UsedYear'),
    Houses.get('TotalSquare'),Houses.get('FloorCount'),Houses.get('UndergroundFloorCount'),
    Houses.get('CulturalHeritage'),Houses.get('OKTMOCode'),Houses.get('OlsonTZ'),
    Houses.get('State'),Houses.get('LifeCycleStage')))
    print('data inserted')
    conn.commit()
except: print('shit happened')