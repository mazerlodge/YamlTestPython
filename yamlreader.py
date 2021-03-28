#!/usr/local/bin/python3 
# Usage: yamlreader filename

import yaml 
import sys

# check for filename to read 
if (len(sys.argv) < 2): 
	print("Usage: yamlreader filename")
	exit() 
	
# check for valid file type, only handling fruits and categories
inFile = sys.argv[1]
print(inFile.find("fruits"))

fileType="NOT_SET"
if (inFile.find("fruits") > -1): 
	fileType = "FRUITS"
if ((inFile.find("categories") > -1)
	or(inFile.find("outfile") > -1)): 
	fileType = "CATEGORIES"
	
if (fileType == "NOT_SET"):
	print("Invalid file type, expected fruits or categories")
	exit() 

# read the file specified 
yamlFile = open(inFile) 

if (fileType == "FRUITS"): 
	fruitsDict = yaml.load(yamlFile, Loader=yaml.FullLoader) 
	print(fruitsDict) 

if (fileType == "CATEGORIES"):
	categories = yaml.full_load(yamlFile) 
	
	for item, cat in categories.items():
		print("%s : %s " % (item, cat))
		
	# pull country list from dictionary 
	countriesList = categories["countries"]
	for aCountry in countriesList: 
		print(aCountry) 
		
	