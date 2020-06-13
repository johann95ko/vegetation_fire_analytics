import os
from ibm_db import connect, fetch_assoc, tables, exec_immediate


from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

DATABASE= os.getenv('DATABASE')
HOSTNAME=os.getenv('HOSTNAME')
PORT=os.getenv('PORT')
UID=os.getenv('UID')
PWD=os.getenv('PWD')
TABLE=os.getenv('TABLE')

connection = connect('DATABASE=' + DATABASE +  ';'
                     'HOSTNAME=' + HOSTNAME +  ';' 
                     'PORT=' + PORT +  ';'
                     'PROTOCOL=TCPIP;'
                     'UID=' + UID +  ';'
                     'PWD=' + PWD +  ';', '', '')
class Db2:
    def results(self, command):
        ret = []
        result = fetch_assoc(command)
        while result:
            ret.append(result)
            result = fetch_assoc(command)
        return ret 

    def read_table(self):
        sql = "SELECT * FROM "+ TABLE + ";"
        res = self.results(exec_immediate(connection, sql))
        
        return res
    
    def update_table(self, location_name:str, risk:float):
        sql = 'UPDATE ' + TABLE + ' SET RISK = ' + str(risk) + ' WHERE LOCATION_ID = '+ location_name + ';'
        res = exec_immediate(connection, sql)
        if res is None:
            return -1
        else:
            return 0
