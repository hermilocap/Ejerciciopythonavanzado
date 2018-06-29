import sqlite3

con=sqlite3.connect('pythondb.sqlite')
##
##query="INSERT INTO 'Usuarios'('nombre','tipo','edad') VALUES('Jose','Normal','99')"
##
##con.execute(query)
##con.commit()
##con.close()

#Leer datos
##for row in con.execute("SELECT * FROM 'Usuarios'"):
##    print(row)
##num='3'
##for row in con.execute("SELECT * FROM 'Usuarios' WHERE id=?",num):
## print(row)

quitar="DELETE FROM 'Usuarios' WHERE id=3"
con.execute(quitar)
con.commit()
con.close()
