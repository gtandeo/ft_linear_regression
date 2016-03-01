#!/usr/bin/python

import sys
import os
import math

mileages = []
prices = []
learningRate = 0.15
theta0 = 0.0
theta1 = 0.0

#parse data file
try:
	my_data = open("data/data.csv", "r")
except IOError:
	print "error: missing data file \'data/data.csv\'"
	sys.exit(0)

#parse theta0 and theta1's values
if os.path.exists("data/theta.csv") is True:
	theta_file = open("data/theta.csv", "r")
	tmp_line = theta_file.readline()
	theta0 = float(tmp_line.split(" ", 2)[0])
	theta1 = float(tmp_line.split(" ", 2)[1])
	theta_file.close()

#stock data in tab
i = 0
for line in my_data:
	if i > 0:
		tmp = line.split(",", 2)
		mileages.append(int(tmp[0]))
		prices.append(int(tmp[1]))
	i += 1

#calc sigma
sumtheta0 = sum([theta0 + (theta1 * mileages[i]) - prices[i] for i in range(0, len(mileages))])
sumtheta1 = sum([(theta0 + (theta1 * mileages[i]) - prices[i]) * mileages[i] for i in range(0, len(mileages))])

#calc theta's tmp values
tmptheta0 = learningRate * float(1) / len(mileages) * sumtheta0
tmptheta1 = learningRate * float(1) / len(mileages) * sumtheta1

#calc final theta's values
theta0 = theta0 - tmptheta0
theta1 = theta1 - tmptheta1

#write theta0 and theta1 in data file
theta_file = open("data/theta.csv", "w+")
theta_file.write(str(theta0) + ' ' + str(theta1))
theta_file.close()
