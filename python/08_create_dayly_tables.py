import os
import glob
import csv
import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'skru'
files = glob.glob("./sms-call-internet-mi-*.txt")

cnx = mysql.connector.connect(user='grzegorz',passwd='123456')
cursor = cnx.cursor()
	
try:
	cnx.database = DB_NAME  
except mysql.connector.Error as err:
	if err.errno == errorcode.ER_BAD_DB_ERROR:
		create_database(cursor)
		cnx.database = DB_NAME
	else:
		print(err)
		exit(1)
			
for name in files:
	filename = name[2:].replace(".txt","")
	tablename = "milano_converted_" + name[23:].replace(".txt","")
	createQuery = (
	"CREATE TABLE `"+tablename+"` ("
	+"  `DATA_ID` int(11) NOT NULL AUTO_INCREMENT,"
	+"  `SQUARE_ID` int(11) NOT NULL,"
	+"	`TIME` bigint(11) NOT NULL,"
	+"	`country_code` varchar(20) NOT NULL,"
	+"  `SMS_IN` double,"
	+"  `SMS_OUT` double,"
	+"  `CALL_IN` double,"
	+"  `CALL_OUT` double,"
	+"  `INTERNET_TRAFFIC` double ,"
	+" PRIMARY KEY (`data_id`), "
	+" KEY `square_id` (`square_id`)"
	+") ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1")
	
	
	try:
		print("Creating table {}: ".format(tablename))
		cursor.execute(createQuery)
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
			print("already exists.")
		else:
			print(err.msg)
	else:
		print("OK")
	
	cursor.execute('LOAD DATA LOCAL INFILE "'+filename+'.txt" INTO TABLE `'+tablename+'` CHARACTER SET latin2 FIELDS TERMINATED BY "	" LINES TERMINATED BY "\n" (`square_id`, `time`, `country_code`, `sms_in`, `sms_out`, `call_in`, `call_out`, `internet_traffic`)')
	print tablename
	cnx.commit()
cnx.close()