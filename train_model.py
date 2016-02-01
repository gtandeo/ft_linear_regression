#!/usr/bin/python

import sys
import os

mileages = []
prices = []
learningRate = 2
tmptheta0 = 0
tmptheta1 = 0
estimated_price = 1

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

#recover the estimated price value in the file 'estimated_price.csv'
if os.path.exists("data/estimated_price.csv") is True:
	estimated_price_file = open("data/estimated_price.csv", "r")
	estimated_price = int(estimated_price_file.readline())
	estimated_price_file.close()

for i in range(0, len(mileages)):
	print tmptheta0
	print tmptheta1
	tmptheta0 += learningRate * (1 / len(mileages)) * i * (estimated_price * (mileages[i]) - prices[i])
	tmptheta1 += learningRate * (1 / len(mileages)) * i * (estimated_price * (mileages[i]) - prices[i]) * mileages[i]

theta_file = open("data/theta.csv", "w+")
theta_file.write(str(tmptheta0) + ' ' + str(tmptheta1))
theta_file.close()
#os.system('python estimatePrice.py')
