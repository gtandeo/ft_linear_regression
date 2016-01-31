#!/usr/bin/python

import sys
import os
from Tkinter import *

data = []
car_mileage = 0
car_price = 0

def		get_data(data):
	try:
		my_file = open("data/data.csv", "r")
	except IOError:
		print "error: missing data file \'data/data.csv\'"
		sys.exit(0)
	for line in my_file:
		data.append(line)
	my_file.close()

def		draw(data):
	master = Tk()
	w = Canvas(master, width=1000, height=650)
	w.pack()

	w.create_line(50, 600, 950, 600, width=5)
	w.create_line(50, 602, 50, 50, width=5)
	w.create_line(60, 600, 60, 50, fill="black", dash=(2, 100), width=20)
	w.create_line(50, 590, 950, 590, fill="black", dash=(2, 125), width=15)
	
	w.create_text(35, 25, text="Price ($)")
	w.create_text(950, 630, text="Mileage (miles)")

	w.create_text(25, 495, text="1 800")
	w.create_text(25, 290, text="5 400")
	w.create_text(25, 85, text="9 000")

	w.create_text(305, 625, text="80 000")
	w.create_text(560, 625, text="160 000")
	w.create_text(815, 625, text="240 000")

	i = 0
	for line in data:
		if i > 0:
			tmp = line.split(",", 2)
			x = 125 * int(tmp[0]) / 40000 + 50
			y = 650 - (100 * int(tmp[1]) / 1800) - 50
			w.create_line(x, y, x + 5, y, width=5)
		i += 1

	if os.path.exists("data/mileage.csv") is True and os.path.exists("data/estimated_price.csv") is True:
		car_mileage = open("data/mileage.csv", "r")
		car_price = open("data/estimated_price.csv", "r")
		x = 125 * int(car_mileage.getline()) / 40000 + 50
		y = 650 - (100 * int(car_price.getline()) / 1800) - 50
	else:
		print "no exists"

	mainloop()

get_data(data)
draw(data)

#25000 -> 100
#50000 -> 200