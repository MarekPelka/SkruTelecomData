from warnings import filterwarnings
import MySQLdb

conn = MySQLdb.connect(host='localhost',
    user='grzegorz',
    passwd='123456',
    db='skru')

for day in range (1,31):
	cursor = conn.cursor()
	try:
		cursor.execute("SELECT VARIANCE(sms_in) as sms_in,VARIANCE(sms_out) as sms_out,VARIANCE(call_in) as call_in,VARIANCE(call_out) as call_out" \
		+",VARIANCE(internet_traffic) as internet_traffic from `milano_converted_2013-11-"+str(day).zfill(2)+"`")
	except Exception,e:
		print str(e)
	for (sms_in, sms_out, call_in, call_out, internet_traffic) in cursor:
		try:
			cursor.execute("INSERT INTO milano_variance_days(DATA_ID,MONTH,DAY,SMS_IN_VAR,SMS_OUT_VAR,CALL_IN_VAR,CALL_OUT_VAR,INTERNET_TRAFFIC_VAR) VALUES (NULL,{},{},{},{},{},{},{})".format(\
			11,day,sms_in,sms_out,call_in,call_out,internet_traffic))
			conn.commit()
		except Exception,e:
			print str(e)
for day in range (1,32):
	cursor = conn.cursor()
	try:
		cursor.execute("SELECT VARIANCE(sms_in) as sms_in,VARIANCE(sms_out) as sms_out,VARIANCE(call_in) as call_in,VARIANCE(call_out) as call_out" \
		+",VARIANCE(internet_traffic) as internet_traffic from `milano_converted_2013-12-"+str(day).zfill(2)+"`")
	except Exception,e:
		print str(e)
	for (sms_in, sms_out, call_in, call_out, internet_traffic) in cursor:
		try:
			cursor.execute("INSERT INTO milano_variance_days(DATA_ID,MONTH,DAY,SMS_IN_VAR,SMS_OUT_VAR,CALL_IN_VAR,CALL_OUT_VAR,INTERNET_TRAFFIC_VAR) VALUES (NULL,{},{},{},{},{},{},{})".format(\
			12,day,sms_in,sms_out,call_in,call_out,internet_traffic))
			conn.commit()
		except Exception,e:
			print str(e)


cursor = conn.cursor()
try:
	cursor.execute("SELECT VARIANCE(sms_in) as sms_in,VARIANCE(sms_out) as sms_out,VARIANCE(call_in) as call_in,VARIANCE(call_out) as call_out" \
	+",VARIANCE(internet_traffic) as internet_traffic from `milano_converted_2014-01-01`")
except Exception,e:
	print str(e)
for (sms_in, sms_out, call_in, call_out, internet_traffic) in cursor:
	try:
		cursor.execute("INSERT INTO milano_variance_days(DATA_ID,MONTH,DAY,SMS_IN_VAR,SMS_OUT_VAR,CALL_IN_VAR,CALL_OUT_VAR,INTERNET_TRAFFIC_VAR) VALUES (NULL,{},{},{},{},{},{},{})".format(\
		1,1,sms_in,sms_out,call_in,call_out,internet_traffic))
		conn.commit()
	except Exception,e:
		print str(e)