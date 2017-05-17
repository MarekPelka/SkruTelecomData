import csv
import os
from warnings import filterwarnings
import MySQLdb
filterwarnings('ignore', category = MySQLdb.Warning)

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='',
    db='skru')


for i in range(1,31):
    cursor = mydb.cursor()
    cursor.execute('LOAD DATA LOCAL INFILE "sms-call-internet-mi-2013-11-'+str(i).zfill(2)+'.txt" INTO TABLE `skru`.`milano` CHARACTER SET latin2 FIELDS TERMINATED BY "	" LINES TERMINATED BY "\n" (`square_id`, `time`, `country_code`, `sms_in`, `sms_out`, `call_in`, `call_out`, `internet_traffic`)')
    mydb.commit()
    cursor.close()
    print "Done" + str(i) + "/30 november milano"

for i in range(1,32):
    cursor = mydb.cursor()
    cursor.execute('LOAD DATA LOCAL INFILE "sms-call-internet-mi-2013-12-'+str(i).zfill(2)+'.txt" INTO TABLE `skru`.`milano` CHARACTER SET latin2 FIELDS TERMINATED BY "	" LINES TERMINATED BY "\n" (`square_id`, `time`, `country_code`, `sms_in`, `sms_out`, `call_in`, `call_out`, `internet_traffic`)')
    mydb.commit()
    cursor.close()
    print "Done" + str(i) + "/31 december milano"

cursor = mydb.cursor()
cursor.execute('LOAD DATA LOCAL INFILE "sms-call-internet-mi-2014-01-'+str(i).zfill(2)+'.txt" INTO TABLE `skru`.`milano` CHARACTER SET latin2 FIELDS TERMINATED BY "	" LINES TERMINATED BY "\n" (`square_id`, `time`, `country_code`, `sms_in`, `sms_out`, `call_in`, `call_out`, `internet_traffic`)')
mydb.commit()
cursor.close()
print "Done" + str(i) + "/1 january milano"


for i in range(1,31):
    cursor = mydb.cursor()
    cursor.execute('LOAD DATA LOCAL INFILE "sms-call-internet-tn-2013-11-'+str(i).zfill(2)+'.txt" INTO TABLE `skru`.`trento` CHARACTER SET latin2 FIELDS TERMINATED BY "	" LINES TERMINATED BY "\n" (`square_id`, `time`, `country_code`, `sms_in`, `sms_out`, `call_in`, `call_out`, `internet_traffic`)')
    mydb.commit()
    cursor.close()
    print "Done" + str(i) + "/30 november trento"

for i in range(1,32):
    cursor = mydb.cursor()
    cursor.execute('LOAD DATA LOCAL INFILE "sms-call-internet-tn-2013-12-'+str(i).zfill(2)+'.txt" INTO TABLE `skru`.`trento` CHARACTER SET latin2 FIELDS TERMINATED BY "	" LINES TERMINATED BY "\n" (`square_id`, `time`, `country_code`, `sms_in`, `sms_out`, `call_in`, `call_out`, `internet_traffic`)')
    mydb.commit()
    cursor.close()
    print "Done" + str(i) + "/31 december trento"

cursor = mydb.cursor()
cursor.execute('LOAD DATA LOCAL INFILE "sms-call-internet-mi-2014-01-'+str(i).zfill(2)+'.txt" INTO TABLE `skru`.`trento` CHARACTER SET latin2 FIELDS TERMINATED BY "	" LINES TERMINATED BY "\n" (`square_id`, `time`, `country_code`, `sms_in`, `sms_out`, `call_in`, `call_out`, `internet_traffic`)')
mydb.commit()
cursor.close()
print "Done" + str(i) + "/1 january trento"