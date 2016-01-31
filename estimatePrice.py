#!/usr/bin/python

import sys
import os

if os.path.exists("data/mileage_tmp.lr") is False:
	try:
		mileage = int(raw_input("Input: "))
		mileage_file = open("data/mileage_tmp.lr", "w+")
		mileage_file.write(str(mileage))
		mileage_file.close()
	except ValueError:
		print "please enter a valid value"

if os.path.exists("data/theta_tmp.lr") is True:
	theta_file = open("data/theta_tmp.lr", "r")
	tmp_line = theta_file.readline()
	theta0 = int(tmp_line.split(" ", 2)[0])
	theta1 = int(tmp_line.split(" ", 2)[1])
	theta_file.close()
else:
	theta0 = 0
	theta1 = 0

mileage = 0
estimated_price = theta0 + (theta1 * mileage)
estimated_price_file = open("data/estimated_price_tmp.lr", "w+")
estimated_price_file.write(str(estimated_price))
estimated_price_file.close()
os.system('python train_model.py')
