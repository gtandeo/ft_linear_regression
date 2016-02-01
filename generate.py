#!/usr/bin/python

import sys
import os
import random

if os.path.exists("data/mileage.csv") is True:
	os.remove("data/mileage.csv")
if os.path.exists("data/theta.csv") is True:
	os.remove("data/theta.csv")
if os.path.exists("data/estimated_price.csv") is True:
	os.remove("data/estimated_price.csv")
