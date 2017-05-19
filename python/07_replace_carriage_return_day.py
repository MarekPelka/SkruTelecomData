import os
import glob

replacement  = '\r'
files = glob.glob("./*sms-call-internet-mi-*.txt")
for name in files:
	fileName = name[2:]
	with open(fileName) as f:
		s = f.read()
		s = s.replace('\n', replacement)
	with open(fileName, "wb") as f:
		f.write(s)

replacement  = '\n'
files = glob.glob("./*sms-call-internet-mi-*.txt")
for name in files:
	fileName = name[2:]
	with open(fileName) as f:
		s = f.read()
		s = s.replace('\r', replacement)
	with open(fileName, "wb") as f:
		f.write(s)