#!/usr/bin/python

import sys
import os

mileage = 0
if os.path.exists("data/mileage.csv") is False:
	try:
		mileage = int(raw_input("Input: "))
		mileage_file = open("data/mileage.csv", "w+")
		mileage_file.write(str(mileage))
		mileage_file.close()
	except ValueError:
		print "please enter a valid value"
else:
	mileage_file = open("data/mileage.csv", "r")
	mileage = int(mileage_file.readline())
	mileage_file.close()

if os.path.exists("data/theta.csv") is True:
	theta_file = open("data/theta.csv", "r")
	tmp_line = theta_file.readline()
	theta0 = int(tmp_line.split(" ", 2)[0])
	theta1 = int(tmp_line.split(" ", 2)[1])
	theta_file.close()
else:
	theta0 = 0
	theta1 = 0

estimated_price = theta0 + (theta1 * mileage) + 1
estimated_price_file = open("data/estimated_price.csv", "w+")
estimated_price_file.write(str(estimated_price))
estimated_price_file.close()
#os.system('python train_model.py')
