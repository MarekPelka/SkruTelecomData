import os
import glob
replacement  = '\n'
files = glob.glob("./*sms-call-internet*.txt")
for name in files:
	fileName = name[2:]
	with open(fileName) as f:
		s = f.read()
		s = s.replace('\r', replacement)
	with open(fileName, "wb") as f:
		f.write(s)