import pandas as pd
import pymysql

username = "admin"
password = "12345678"
host = "datagpt.cgtlbgxgrxsx.us-east-2.rds.amazonaws.com" 
port = 3306

'''
pymysql.cursors.DictCursor para que los resultados que devuelva sean diccionarios,
por defecto devuelve tuplas. Asi podemos acceder por clave a las columnas.
'''

db = pymysql.connect(host = host,
                     user = username,
                     password = password,
                     cursorclass = pymysql.cursors.DictCursor
)

# El objeto cursor es el que ejecutará las queries y devolverá los resultados

cursor = db.cursor()

# Para usar la BD  recien creada

cursor.connection.commit()
use_db = ''' USE datagpt'''
cursor.execute(use_db)

# checkear todas las tablas que tiene mi db
cursor.execute('SHOW TABLES')
cursor.fetchall()

sql = '''SELECT * FROM datagpt'''
cursor.execute(sql)

mi_lista = cursor.fetchall()

df = pd.DataFrame(mi_lista)

df.to_excel('GPT_TA800.xlsx')