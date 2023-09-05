#!/usr/bin/python3

import mysql.connector
import os

mysql_user = os.environ['MYSQL_USER']
mysql_password = os.environ['MYSQL_PASSWORD']
mysql_host = os.environ['MYSQL_HOST']
mysql_database = os.environ['MYSQL_DATABASE']
user_domain = os.environ['USER_DOMAIN']
network_bind = os.environ['NETWORK_BIND']
network_local_host = os.environ['NETWORK_LOCAL_HOST']
network_local_bind = os.environ['NETWORK_LOCAL_BIND']

server_addr = "ts.platform." + user_domain
stun_addr = "stun:ts.platform." + user_domain + ":" + str(network_bind)

cnx = mysql.connector.connect(user=mysql_user, password=mysql_password, host=mysql_host, database=mysql_database)
cursor = cnx.cursor()

update_query = f"UPDATE network_server_info SET server_addr='{server_addr}', server_port='{network_bind}', identifier='{network_local_host}', extra='{{\"stun_addr\":\"{stun_addr}\"}}' WHERE server_addr != '{server_addr}' OR server_port != '{network_bind}' OR identifier != '{network_local_host}' OR extra != '{{\"stun_addr\":\"{stun_addr}\"}}'"
cursor.execute(update_query)
cnx.commit()

# Close the cursor and connection
cursor.close()
cnx.close()
