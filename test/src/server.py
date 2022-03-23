from configparser import ConfigParser
import pyodbc
from bottle import route, run, template


@route('/hello')
def hello():
    return "Hello!"

@route('/sql')
def sql():
    parser = ConfigParser()
    parser.read('config.ini')

    server = parser.get('DATABASE', 'server')
    username = parser.get('DATABASE', 'username')
    password = parser.get('DATABASE', 'password')

    cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';UID='+username+';PWD='+ password+';TrustServerCertificate=Yes;')
    cursor = cnxn.cursor()

    cursor.execute("SELECT @@version;") 
    row = cursor.fetchone()
    version = ''
    while row: 
        version = row[0]
        print(version)
        row = cursor.fetchone()

    cursor.close()
    cnxn.close()

    return template('<b>Version: {{version}}</b>!', version=version)

run(host='0.0.0.0', port=8080)