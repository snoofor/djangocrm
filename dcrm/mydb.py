# Connection to mysql database
# Do not forget to type the following command in terminal - pip install mysqlclient

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '+23@F-Oe+h5'
)

cursorObject = dataBase.cursor()

try:
    cursorObject.execute('use CRM')
    print('All done')
except:
    print('Error occured')
