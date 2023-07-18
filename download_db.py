import pandas as pd
import pymysql

username = "admin"
password = "12345678"
host = "datagpt.cgtlbgxgrxsx.us-east-2.rds.amazonaws.com" 
port = 3306

# Conectar a la base de datos
db = pymysql.connect(
    host=host,
    user=username,
    password=password,
    cursorclass=pymysql.cursors.DictCursor
)

# Crear un objeto cursor para ejecutar consultas y obtener resultados
cursor = db.cursor()

# Seleccionar la base de datos a utilizar
cursor.connection.commit()
use_db = ''' USE datagpt'''
cursor.execute(use_db)

# Consultar todas las tablas en la base de datos
cursor.execute('SHOW TABLES')
tables = cursor.fetchall()

# Ejecutar la consulta SQL para seleccionar todas las filas de la tabla 'datagpt'
sql = '''SELECT * FROM datagpt'''
cursor.execute(sql)

# Obtener todas las filas devueltas por la consulta
result = cursor.fetchall()

# Crear un DataFrame a partir de los datos obtenidos
df = pd.DataFrame(result)

# Guardar el DataFrame en un archivo Excel
df.to_excel('GPT_TA800.xlsx')


df.to_excel('GPT_TA800.xlsx')
