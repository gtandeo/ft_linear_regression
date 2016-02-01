#!/usr/bin/python

import sys
import os

mileages = []
prices = []

#parse data
i = 0
my_data = open("data/data.csv", "r")
for line in my_data:
	if i > 0:
		tmp = line.split(",", 2)
		mileages.append(int(tmp[0]))
		prices.append(int(tmp[1]))
	i += 1

#recover the estimated price value in the file 'estimated_price_tmp.lr'
estimated_price_file = open("data/estimated_price.csv", "r")
estimated_price = int(estimated_price_file.readline())
estimated_price_file.close()

learningRate = 1
m = len(mileages)
for i in range(0, len(mileages) - 1):
	tmptheta0 = learningRate * (1 / m) * i * (estimated_price * (mileages[i]) - prices[i])
	tmptheta1 = learningRate * (1 / m) * i * (estimated_price * (mileages[i]) - prices[i]) * mileages[i]

theta_file = open("data/theta.csv", "w+")
theta_file.write(str(tmptheta0) + ' ' + str(tmptheta1))
theta_file.close()
#os.system('python estimatePrice.py')
