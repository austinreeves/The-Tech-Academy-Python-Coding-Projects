

import sqlite3

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

conn = sqlite3.connect('drill.db')

with conn:
    cur = conn.cursor()
    cur.execute("create table if not exists tbl_drill( \
        id integer primary key autoincrement, \
        col_fname text \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect('drill.db')

with conn:
    cur = conn.cursor()
    for file in fileList:
        if file.endswith(".txt"):
            cur.execute("insert into tbl_drill(col_fname) values (?)", [file])
    conn.commit()
conn.close()
        
