#!/usr/bin/python

import sys
import os
import random

def		generate_random_data(my_file, num):
	for i in range(0, num):
		my_file.write(str(int(random.uniform(100, 350000))) + ' ' + str(int(random.uniform(2000, 120000))) + '\n')

try:
	if sys.argv[1] == "--create":
		my_file = open("data/dataset.lr", "w+")
		generate_random_data(my_file, int(sys.argv[2]))
		my_file.close()
	elif sys.argv[1] == "--remove":
		if os.path.exists("data/dataset.lr") is True:
			os.remove("data/dataset.lr")
		else:
			print "Error: dataset.lr data file does not exist"
	else:
		print "Usage: python generate.py [--create | --remove]"
except IndexError:
	print "Index"
except ValueError:
	print "Value"