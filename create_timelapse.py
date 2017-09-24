import imageio

def create_timelapse(first_year, last_year):
	"""Creates a timelapse of all of the cropped images."""
	file_location = "images/cropped_images/"
	images = []
	for file in range(first_year, last_year + 1):
		try:
			image = file_location + str(file) + ".png"
			images.append(imageio.imread(image))
		except:
			print("File not found: " + file_location + str(file) + ".png")
	
	imageio.mimsave('ufo_report_timelapse.gif', images)
	print("The files that were found were added to the GIF.")

create_timelapse(1950,2014)