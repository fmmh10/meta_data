#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from PIL import Image
from PIL.ExifTags import TAGS
from PIL.ExifTags import GPSTAGS

def getMetaData(imgname, out):
	try:
		metaData = {}
		imgFile = Image.open(imgname)
		print "Tentar encontrar meta dados na fotografia..."
		info = imgFile._getexif()
		if info:
			print "Foram encontrados metadados!"
			for (tag, value) in info.items():
				tagname = TAGS.get(tag, tag)
				metaData[tagname] = value

				if not out:
					print tagname, value


			#if u want to send the total result to a file
			if out:
				print "A escrever resultados para o ficheiro..."
				#escrever no ficheiro
				with open(out, "w") as f:
					#this will stop the program here if your folder is protetect
					#so u need root access to create a file
					for(tagname, value) in metaData.items():
						f.write(str(tagname)+"\t"+\
								str(value)+"\n")

		direction_latitude = metaData["GPSInfo"][1] #dados de gps da latitude
		direction_longitude = metaData["GPSInfo"][3] #dados de gps da longitude
		
		
		dlat = to_degrees(metaData["GPSInfo"][2])
		dlon = to_degrees(metaData["GPSInfo"][4])

		
		if direction_latitude == "S":                     
			dlat = 0 - dlat

		if direction_longitude == "W":
			dlon = 0 - dlon

		
		print "A fotografia foi tirada com um dispositivo " + metaData["Make"]
		print "Esta foi a data e hora, respetivamente: " + metaData["DateTimeDigitized"]
		print "Estas são as coordenadas geográficas do momento da fotografia... "
		print "Latitude: " + str(dlat) 
		print "Longitude: " + str(dlon)

	except:
		print "Failed"


def to_degrees(gps_info):
	"""gps_info is a list of"""
	d0 = gps_info[0][0]
	d1 = gps_info[0][1]
	d = float(d0) / float(d1)

	m0 = gps_info[1][0]
	m1 = gps_info[1][1]
	m = float(m0) / float(m1)
	
	s0 = gps_info[2][0]
	s1 = gps_info[2][1]
	s = float(s0) / float(s1)

	return d + (m / 60.0) + (s / 3600.0)

def Main():
	parser = argparse.ArgumentParser()
	parser.add_argument("img",  help="name of an image file.")
	parser.add_argument("--output", "-o", help="dump data out to file")
	args = parser.parse_args()
	if args.img:
		getMetaData(args.img, args.output)

	else:
		print parser.usage

if __name__ == '__main__':
	Main()
	
"""
Add functionalities:
	3-that file opens google maps and sends the request using those variables ;)

"""
