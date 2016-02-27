#!/usr/bin/python

import sys
import os

mileages = []
prices = []
learningRate = 0.15
theta0 = 0.0
theta1 = 0.0
sumtheta0 = 0.0
sumtheta1 = 0.0
tmptheta0 = 0.0
tmptheta1 = 0.0

if os.path.exists("data/theta.csv") is True:
	theta_file = open("data/theta.csv", "r")
	tmp_line = theta_file.readline()
	theta0 = float(tmp_line.split(" ", 2)[0])
	theta1 = float(tmp_line.split(" ", 2)[1])
	theta_file.close()

#parse data file
try:
	my_data = open("data/data.csv", "r")
except IOError:
	print "error: missing data file \'data/data.csv\'"
	sys.exit(0)

i = 0
for line in my_data:
	if i > 0:
		tmp = line.split(",", 2)
		mileages.append(int(tmp[0]))
		prices.append(int(tmp[1]))
	i += 1

for i in range(0, len(mileages)):
	sumtheta0 = sumtheta0 + learningRate * 0.04166 * (float(mileages[i]) - float(prices[i]))
	sumtheta1 = sumtheta1 + learningRate * 0.04166 * (float(mileages[i]) - float(prices[i])) * float(mileages[i])
	print sumtheta0

tmptheta0 += sumtheta0
tmptheta1 += sumtheta1

theta0 = theta0 - tmptheta0
theta1 = theta1 - tmptheta1

theta_file = open("data/theta.csv", "w+")
theta_file.write(str(theta0) + ' ' + str(theta1))
theta_file.close()
