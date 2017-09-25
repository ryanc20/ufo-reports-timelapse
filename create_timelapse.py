import imageio
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def create_timelapse(first_year, last_year):
	"""Creates a timelapse of all of the cropped images."""
	file_location = "images/cropped_images/"
	images = []
	for file in range(first_year, last_year + 1):
		try:
			image = file_location + str(file) + ".png"
			labeled_image = add_timestamp(image, file)
			images.append(imageio.imread(labeled_image))
		except:
			print("File not found: " + file_location + "with_year/" + str(file) + ".png")
	
	imageio.mimsave('ufo_report_timelapse.gif', images, fps=5)
	print("The files that were found were added to the GIF.")

def add_timestamp(image, year):
	"""Adds the current year to the bottom right of the image for each frame."""
	img = Image.open(image)
	draw = ImageDraw.Draw(img)
	font =ImageFont.truetype("font/OpenSans-Regular.ttf", 16)
	draw.text((575, 300), str(year), (0,0,0), font=font)
	draw.text((220, 13), "UFO Reported Sightings 1950-2014", (0,0,0), font=font)
	img.save('images/cropped_images/with_year/' + str(year) + '.png')
	return 'images/cropped_images/with_year/' + str(year) + '.png'
	
create_timelapse(1950, 2014)