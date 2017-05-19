from warnings import filterwarnings
import MySQLdb

conn = MySQLdb.connect(host='localhost',
    user='grzegorz',
    passwd='123456',
    db='skru')
cursor = conn.cursor()
try:
	query = "SELECT k.* from (SELECT m.square_id,SUM(m.internet_traffic) as sum FROM `milano_converted_2014-01-01` m GROUP BY square_id) k"\
	+" ORDER BY k.sum DESC LIMIT 1"
	cursor.execute(query)
except Exception,e:
	print str(e)
for (square_id) in cursor:
	print str(square_id) + "Jan internet_traffic"

cursor = conn.cursor()
try:
	query = "SELECT k.* from (SELECT m.square_id,SUM(m.sms_out) as sum FROM `milano_converted_2014-01-01` m GROUP BY square_id) k"\
	+" ORDER BY k.sum DESC LIMIT 1"
	cursor.execute(query)
except Exception,e:
	print str(e)
for (square_id) in cursor:
	print str(square_id) + "Jan sms out"





for day in range (1,31):
	cursor = conn.cursor()
	try:
		query = "SELECT k.* from (SELECT m.square_id,SUM(m.call_in) as sum FROM `milano_converted_2013-11-"+str(day).zfill(2)+"` m GROUP BY square_id) k"\
		+" ORDER BY k.sum DESC LIMIT 1"
		cursor.execute(query)
	except Exception,e:
		print str(e)
	for (square_id) in cursor:
		print str(square_id) + "Nov" + str(day) + " call_in"
for day in range (1,32):
	cursor = conn.cursor()
	try:
		query = "SELECT k.* from (SELECT m.square_id,SUM(m.call_in) as sum FROM `milano_converted_2013-12-"+str(day).zfill(2)+"` m GROUP BY square_id) k"\
		+" ORDER BY k.sum DESC LIMIT 1"
		cursor.execute(query)
	except Exception,e:
		print str(e)
	for (square_id) in cursor:
		print str(square_id) + "Dec" + str(day)+ " call_in"


cursor = conn.cursor()
try:
	query = "SELECT k.* from (SELECT m.square_id,SUM(m.call_in) as sum FROM `milano_converted_2014-01-01` m GROUP BY square_id) k"\
	+" ORDER BY k.sum DESC LIMIT 1"
	cursor.execute(query)
except Exception,e:
	print str(e)
for (square_id) in cursor:
	print str(square_id) + "Jan call_in"




for day in range (1,31):
	cursor = conn.cursor()
	try:
		query = "SELECT k.* from (SELECT m.square_id,SUM(m.call_out) as sum FROM `milano_converted_2013-11-"+str(day).zfill(2)+"` m GROUP BY square_id) k"\
		+" ORDER BY k.sum DESC LIMIT 1"
		cursor.execute(query)
	except Exception,e:
		print str(e)
	for (square_id) in cursor:
		print str(square_id) + "Nov" + str(day) + " call_out"
for day in range (1,32):
	cursor = conn.cursor()
	try:
		query = "SELECT k.* from (SELECT m.square_id,SUM(m.call_out) as sum FROM `milano_converted_2013-12-"+str(day).zfill(2)+"` m GROUP BY square_id) k"\
		+" ORDER BY k.sum DESC LIMIT 1"
		cursor.execute(query)
	except Exception,e:
		print str(e)
	for (square_id) in cursor:
		print str(square_id) + "Dec" + str(day)+ " call_out"


cursor = conn.cursor()
try:
	query = "SELECT k.* from (SELECT m.square_id,SUM(m.call_out) as sum FROM `milano_converted_2014-01-01` m GROUP BY square_id) k"\
	+" ORDER BY k.sum DESC LIMIT 1"
	cursor.execute(query)
except Exception,e:
	print str(e)
for (square_id) in cursor:
	print str(square_id) + "Jan call_out"




for day in range (1,31):
	cursor = conn.cursor()
	try:
		query = "SELECT k.* from (SELECT m.square_id,SUM(m.internet_traffic) as sum FROM `milano_converted_2013-11-"+str(day).zfill(2)+"` m GROUP BY square_id) k"\
		+" ORDER BY k.sum DESC LIMIT 1"
		cursor.execute(query)
	except Exception,e:
		print str(e)
	for (square_id) in cursor:
		print str(square_id) + "Nov" + str(day) + " internet_traffic"
for day in range (1,32):
	cursor = conn.cursor()
	try:
		query = "SELECT k.* from (SELECT m.square_id,SUM(m.internet_traffic) as sum FROM `milano_converted_2013-12-"+str(day).zfill(2)+"` m GROUP BY square_id) k"\
		+" ORDER BY k.sum DESC LIMIT 1"
		cursor.execute(query)
	except Exception,e:
		print str(e)
	for (square_id) in cursor:
		print str(square_id) + "Dec" + str(day)+ " internet_traffic"


