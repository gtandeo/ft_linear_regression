#!/usr/bin/python

import sys
import os

theta0 = 0
theta1 = 0
mileage = 0
estimated_price = 0.0

#get user mileage input
try:
	mileage = int(raw_input("Input: "))
except ValueError:
	print "please enter a valid value"
	sys.exit(0)

#parse theta0 and theta1's values
if os.path.exists("data/theta.csv") is True:
	theta_file = open("data/theta.csv", "r")
	tmp_line = theta_file.readline()
	theta0 = float(tmp_line.split(" ", 2)[0])
	theta1 = float(tmp_line.split(" ", 2)[1])
	theta_file.close()

#calc estimate_price
estimated_price = theta0 + (theta1 * mileage)
print "This car worth " + str(estimated_price) + " euros"
