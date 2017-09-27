# UFO Report Timelapse
Timelapse heatmap of UFO reports in the U.S. from 1950-2014. Using a [dataset found online](https://www.kaggle.com/NUFORC/ufo-sightings) I was able to explore potential visualizations before deciding this was the most interesting option.
## Overview
The timelapse heatmap that I created uses gmplot to plot a heatmap on top of Google Maps. I then took a screenshot for each year's heatmap and cropped the screenshot to show just the U.S., then using imageio I was able to form a GIF from the cropped images being displayed one after another.
## Demonstration
![alt text](https://media.giphy.com/media/l1J9s9ibi130zGgj6/giphy.gif "UFO report timelapse")

The GIF shows the collection of reports over the 64 year span.
## Motivation
I recently discovered Kaggle, and have always been interested in extra-terrestrial life. I figured it would be a fun project to work on to develop my skills in data visualization and Python.
## Misc.
The file, state_report_counter.py, is not being used currently, but I plan to add additional features that show how many reports come from each state and each states relative frequency. This could lead to interesting insights that I plan to explore using this dataset. This was my first attempt at making a timelapse, I was inspired by [this post on Reddit's r/dataisbeautiful](https://www.reddit.com/r/dataisbeautiful/comments/71e3pp/heatmap_gif_of_reported_crimes_in_chicago_by/) to make my own timelapse of data that I found interesting.
