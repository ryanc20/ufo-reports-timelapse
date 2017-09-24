import csv
import time

import pandas as pd 
import gmplot
from selenium import webdriver
from PIL import Image 

import state_report_counter as sc

def get_lat_and_long(row):
	"""Retreives the current rows latitude and longitude."""
	latitude = row['latitude']
	longitude = row['longitude']
	return latitude, longitude

def get_screenshot(html_file, year):
	"""Takes a screen shot of the HTML file and saves it."""
	driver = webdriver.PhantomJS()
	driver.set_window_size(800, 800)
	driver.get(html_file)

	#allows the page to load completely
	time.sleep(2)

	image = 'images/' + str(year) + '.png'

	driver.save_screenshot(image)
	driver.quit()

	crop_image(image, year)

def crop_image(image_to_crop, year):
	"""Crops the image to the desired size."""
	img = Image.open(image_to_crop)
	#The dimensions of just the US in the image
	img = img.crop((80, 240, 800, 615))

	file_destination = "images/cropped_images/" + str(year) + ".png"

	image_file = open(file_destination, 'wb')
	img.save(image_file, 'png')
	image_file.close()

def plot(lats, lons, year):
	"""Plots the position of each report forming heatmap."""
	html_file = "html_files/ufo_sightings_" + str(year) + ".html"

	gmap = gmplot.GoogleMapPlotter(40, -100, 4)
	gmap.heatmap(lats, lons)
	gmap.draw(html_file)

	get_screenshot(html_file, year)

def run(file_name, first_year, last_year):
	"""Iterates through the dataset to retrieve necessary info."""
	with open(file_name) as file:
		reader = csv.DictReader(file)

		#Counts amount of reports per state.
		#counter = sc.ReportCounter()

		#Allows the csv to be iterable more than once.
		rows = list(reader)

		lats, lons = [], []
		for year in range(first_year, last_year+1):
			for row in rows:
				#counter.update_count(row['state'])
				if row['year'] == str(year):
					latitude, longitude = get_lat_and_long(row)
					lats.append(float(latitude))
					lons.append(float(longitude))
			
			plot(lats, lons, year)

file_name = 'ufo_sightings_us.csv'
run(file_name, 1950, 2014)