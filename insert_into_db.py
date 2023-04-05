import sqlite3
connection = sqlite3.connect(':memory:')
cursor=connection.cursor()
cursor.execute('create table components (rowid int,name varchar(50))')    

number = int(input('Enter number:'))
name = str(input('Enter name: '))

cursor.execute("INSERT INTO components VALUES (?,?)",(number,name))
cursor.execute('select * from components')

w = cursor.fetchall()[0]
print(w)

# for name in ('bar','foo', 'weed'): 
#     cursor.execute("SELECT count(*) FROM components WHERE name = ?", (name,))
#     data=cursor.fetchone()[0]
#     if data==0:
#         print('There is no component named %s'%name)
#     else:
#         print('Component %s found in %s row(s)'%(name,data))