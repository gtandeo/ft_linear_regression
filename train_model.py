#!/usr/bin/python

import sys
import os

#parse data
my_data = open("data/dataset.lr", "r")
for line in my_data:
	tmp = line.split(" ", 2)
	mileage += tmp[0]
	prices += tmp[1]

#recover the estimated price value in the file 'estimated_price_tmp.lr'
estimated_price_file = open("data/estimated_price_tmp.lr", "r")
estimated_price = int(estimated_price_file.readline())
estimated_price_file.close()
#for i in range(0, m - 1):
	#tmptheta0 = learningRate * (1 / m) * i * (estimated_price(mileage[i]) - price[i])
	#tmptheta1 = learningRate * (1 / m) * i * (estimated_price(mileage[i]) - price[i]) * milleage[i]
tmptheta0 = 4
tmptheta1 = 5
theta_file = open("data/theta_tmp.lr", "w+")
theta_file.write(str(tmptheta0) + ' ' + str(tmptheta1))
theta_file.close()
#os.system('python estimatePrice.py')
