#!/usr/bin/python

import sys
import os

theta0 = 0
theta1 = 0
mileage = 0
estimated_price = 0.0

try:
	mileage = int(raw_input("Input: "))
except ValueError:
	print "please enter a valid value"

if os.path.exists("data/theta.csv") is True:
	theta_file = open("data/theta.csv", "r")
	tmp_line = theta_file.readline()
	theta0 = float(tmp_line.split(" ", 2)[0])
	theta1 = float(tmp_line.split(" ", 2)[1])
	theta_file.close()

estimated_price = theta0 + (theta1 * mileage)
print "This car worth " + str(estimated_price) + " euros"
