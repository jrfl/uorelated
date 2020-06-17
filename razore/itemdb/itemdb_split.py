#!/usr/bin/env python3
""" Process the itemdb.xml file first with this shell command:
    Turns mushy nasty xml into a sqlite3 file.  Woohoo!

    grep "^\s\+<object" itemdb.xml  | \
         grep -ve "Server\.Engines\." -ve "Server\.Mobiles\."-ve \
         'gfx="1"' -ve "\.Quests\." -ve "Server\.Factions\." | \
         sed -e "s/^\s\+//g" -e "s/^<object type=//g" -e"s/[\s/>]\+$//g" | \
         sort >itemdb_2ndstage.txt

    It's a biggun... and took < 10 minutes to create vs wasting an hour fucking
    with an xml parser.

    Next, run this python script, which will produce uoitemdb.sqlite3 in the
    current directory
"""

import re
import sqlite3
dbfile = "./uoitemdb.sqlite3"
dbtable = "items"

conn = sqlite3.connect(dbfile)
cur = conn.cursor()

# It's ok if there's no table to drop
try:
    cur.execute('DROP TABLE {};'.format(dbtable))
except:
    pass

cvt = re.compile(r'(?<!^)(?=[A-Z])')

f = open("itemdb_2ndstage.txt", "r")

data = f.read()
data = data.splitlines()
f.close()

cur.execute('''CREATE TABLE
               {} (id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               gfxid INTEGER NOT NULL,
               color INTEGER DEFAULT 0
               ); '''
            .format(dbtable))

for x in data:
    if x.find(".") > -1:
        ndx = x.rfind(".")
        x = x[ndx+1:]
    x = x.replace('"', '')
    spl = x.split(" ")
    f1 = cvt.sub(" ", spl[0])
    f2 = hex(int(spl[1].replace("gfx=", "")))
    f3 = "0x00"
    if (len(spl) > 2) and len(spl[2]) > 0:
        f3 = hex(int(spl[2].replace("hue=", "")))
    print("%s: ID: %s, HUE: %s" % (f1, f2, f3))
    cur.execute('''Insert into {} values
          (NULL, ?, ?, ?);'''.format(dbtable), (f1, int(f2, 16), int(f3, 16)))
conn.commit()
conn.close()
print('Finis')

