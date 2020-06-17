#!/usr/bin/env python3
import re
import sqlite3

dbfile = "./boddb.sqlite3"
dbtable = "bods"
conn = sqlite3.connect(dbfile)
cur = conn.cursor()

# It's ok if there's no table to drop
try:
    cur.execute('DROP TABLE {};'.format(dbtable))
except:
    pass

cur.execute('''CREATE TABLE
               {} (id INTEGER PRIMARY KEY,
               item TEXT NOT NULL,
               quality TEXT NOT NULL,
               material TEXT NOT NULL,
               largeInd INTEGER NOT NULL,
               complete INTEGER NOT NULL,
               needed INTEGER NOT NULL
               ); '''
            .format(dbtable))




numFinder = re.compile("^[0-9]+\s+/\s[0-9]+")
skips = [
    "Bulk Order Book",
    "Type",
    "Item",
    "Quality",
    "Material",
    "Amount",
    "Set Filter",
    "Using No Filter",
    "EXIT",
    "Previous page",
    "Next page",
    "Small",
#    "Large"
]

metalTypes = [
    "Iron",
    "Shadow Iron",
    "Dull Copper",
    "Copper",
    "Bronze",
    "Gold",
    "Agapite",
    "Verite",
    "Valorite"
]

itemQuality = [
    "normal",
    "exceptional"
]


data = ""

with open("bodlist.txt", "r") as f:
    data = f.read()

metType = None
item = None
quality = None

lines = data.splitlines()
allItems = []
quantities = []
largeIndex = -1
isLarge = False

for ndx, line in enumerate(lines):
    line = line.strip()
    if line in skips:
        metType = ""
        item = ""
        quality = ""
        isLarge = False
        continue

    elif line == "Large":
        isLarge = True
        largeIndex += 1
        metType = ""
        item = ""
        quality = ""

    elif line in metalTypes:
        metType = line
        if isLarge:
            boi = (item, quality, metType, largeIndex)
        else:
            boi = (item, quality, metType, -1)

        allItems.append(boi)
        continue

    elif line in itemQuality:
        quality = line
        continue

    elif numFinder.match(line):
        metType = ""
        item = ""
        quality = ""
        v = line.split("/")
        v = list(map(str.strip, v))
        quantities.append((int(v[0]), int(v[1])))

    else:
        item = line

for i in range(0, len(allItems)):
    print(str((*allItems[i], *quantities[i])))
    cur.execute('''Insert into {} values
          (NULL, ?, ?, ?, ?, ?, ?);'''.format(dbtable),
          (*allItems[i][:3], int(allItems[i][3]), int(quantities[i][0]),
          int(quantities[i][1])))

conn.commit()
conn.close()
print('Done')

"""
select b1.item, b1.material, b1.quality, b1.largeInd, b1.needed, b2.needed, b1.id, b2.id from bods b1
left outer join bods b2 on
      b1.item = b2.item AND
	  b1.quality = b2.quality AND
	  b1.material = b2.material AND
	  b1.needed = b2.needed
WHERE
      b1.largeInd != -1 AND
	  b2.largeInd = -1
order by
      b1.largeInd ASC
"""

