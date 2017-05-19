from warnings import filterwarnings
import MySQLdb

conn = MySQLdb.connect(host='localhost',
    user='grzegorz',
    passwd='123456',
    db='skru')

for day in range (1,31):
	cursor = conn.cursor()
	try:
		cursor.execute("SELECT AVG(sms_in) as sms_in,AVG(sms_out) as sms_out,AVG(call_in) as call_in,AVG(call_out) as call_out" \
		+",AVG(internet_traffic) as internet_traffic from `milano_converted_2013-11-"+str(day).zfill(2)+"` where country_code='39' AND (sms_in != 0.0 AND sms_out != 0.0 AND call_in != 0.0 AND call_out != 0.0 AND internet_traffic != 0.0)")
	except Exception,e:
		print str(e)
	for (sms_in, sms_out, call_in, call_out, internet_traffic) in cursor:
		try:
			cursor.execute("INSERT INTO milano_averages_days_39_wuthout_zeros(DATA_ID,MONTH,DAY,SMS_IN_AVG,SMS_OUT_AVG,CALL_IN_AVG,CALL_OUT_AVG,INTERNET_TRAFFIC_AVG) VALUES (NULL,{},{},{},{},{},{},{})".format(\
			11,day,sms_in,sms_out,call_in,call_out,internet_traffic))
			conn.commit()
		except Exception,e:
			print str(e)
for day in range (1,32):
	cursor = conn.cursor()
	try:
		cursor.execute("SELECT AVG(sms_in) as sms_in,AVG(sms_out) as sms_out,AVG(call_in) as call_in,AVG(call_out) as call_out" \
		+",AVG(internet_traffic) as internet_traffic from `milano_converted_2013-12-"+str(day).zfill(2)+"` where country_code='39' AND (sms_in != 0.0 AND sms_out != 0.0 AND call_in != 0.0 AND call_out != 0.0 AND internet_traffic != 0.0)")
	except Exception,e:
		print str(e)
	for (sms_in, sms_out, call_in, call_out, internet_traffic) in cursor:
		try:
			cursor.execute("INSERT INTO milano_averages_days_39_wuthout_zeros(DATA_ID,MONTH,DAY,SMS_IN_AVG,SMS_OUT_AVG,CALL_IN_AVG,CALL_OUT_AVG,INTERNET_TRAFFIC_AVG) VALUES (NULL,{},{},{},{},{},{},{})".format(\
			12,day,sms_in,sms_out,call_in,call_out,internet_traffic))
			conn.commit()
		except Exception,e:
			print str(e)


cursor = conn.cursor()
try:
	cursor.execute("SELECT AVG(sms_in) as sms_in,AVG(sms_out) as sms_out,AVG(call_in) as call_in,AVG(call_out) as call_out" \
	+",AVG(internet_traffic) as internet_traffic from `milano_converted_2014-01-01` where country_code='39' AND (sms_in != 0.0 AND sms_out != 0.0 AND call_in != 0.0 AND call_out != 0.0 AND internet_traffic != 0.0)")
except Exception,e:
	print str(e)
for (sms_in, sms_out, call_in, call_out, internet_traffic) in cursor:
	try:
		cursor.execute("INSERT INTO milano_averages_days_39_wuthout_zeros(DATA_ID,MONTH,DAY,SMS_IN_AVG,SMS_OUT_AVG,CALL_IN_AVG,CALL_OUT_AVG,INTERNET_TRAFFIC_AVG) VALUES (NULL,{},{},{},{},{},{},{})".format(\
		1,1,sms_in,sms_out,call_in,call_out,internet_traffic))
		conn.commit()
	except Exception,e:
		print str(e)