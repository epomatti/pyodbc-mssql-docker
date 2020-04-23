from configparser import ConfigParser
import pyodbc

parser = ConfigParser()
parser.read('config.ini')

server = parser.get('DATABASE', 'server')
username = parser.get('DATABASE', 'username')
password = parser.get('DATABASE', 'password')

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

cursor.execute("SELECT @@version;") 
row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()