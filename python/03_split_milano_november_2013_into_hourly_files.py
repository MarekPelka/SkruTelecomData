import csv
from collections import defaultdict
from datetime import datetime, date,timedelta
def removekey(d, key):
	r = dict(d)
	del r[key]
	return r

def splitFiles(zeroTime,fromDay,lastDay):
	mapToLowRangeTimeValue = {}
	for day in range(fromDay,lastDay):
		
		for hour in range(25):
			fromRangeTime = 13832604 + 36*hour + 36*24*(day-1)		
			for sixMinutes in range(6):
				mapToLowRangeTimeValue[zeroTime] = fromRangeTime
				zeroTime = zeroTime + 6
		finalDict = defaultdict(list)
		print (str(day).zfill(2))
		csv_data = csv.reader(file("sms-call-internet-mi-2013-11-"+str(day).zfill(2)+".txt"))
		for row in csv_data:
			rowtab = row[0].split('\t')
			finalDict[mapToLowRangeTimeValue[int(rowtab[1][:-5])]].append(rowtab)
		print "ended."
		counter = 0
		for key, value in finalDict.items():
			keyDate = datetime.fromtimestamp(int(key) * 100) + timedelta(hours =1)
			with open("milano_converted_{}.txt".format(keyDate.strftime('%Y-%b-%d--%H')), 'a+') as csvfile:
					spamwriter = csv.writer(csvfile)
					spamwriter.writerows(value)
			counter = counter + 1

			
splitFiles(13832604,1,10)
splitFiles(13840380,10,20)
splitFiles(13849020,20,31)