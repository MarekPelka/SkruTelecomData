import csv
import os
from warnings import filterwarnings
import glob
import MySQLdb
filterwarnings('ignore', category = MySQLdb.Warning)

mydb = MySQLdb.connect(host='localhost',
    user='grzegorz',
    passwd='123456',
    db='skru')
	
TABLES = {}

files = glob.glob('./*milano_converted_range*.txt')
for name in files:
	print (name[2:])

#for i in range(1,30):
 #   cursor = mydb.cursor()
  #  cursor.execute('LOAD DATA LOCAL INFILE "sms-call-internet-tn-2014-01-'+str(i).zfill(2)+'.txt" INTO TABLE `skru`.`trento` CHARACTER SET latin2 FIELDS TERMINATED BY "	" LINES TERMINATED BY "\n" (`square_id`, `time`, `country_code`, `sms_in`, `sms_out`, `call_in`, `call_out`, `internet_traffic`)')
   # mydb.commit()
    #cursor.close()
    #print "Done" + str(i) + "/30"