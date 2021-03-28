#!/usr/local/bin/python3
# Usage: yamlwriter filename 

import yaml 
import sys 

if (len(sys.argv) < 2): 
	print("Usage yamlwriter filename")
	exit() 

# make a list of dictionaries to be serialized out to a yaml file 
categoriesList = [
				{'sports' : ['soccer', 'football', 'baseball']},
				{'countries' : ['USA', 'Mexico', 'Spain', 'Italy']}
]

# preview the data, ,showing the dictionary is formatted correctly 
for aDict in categoriesList: 
	for aKey in aDict.keys(): 	
		print("%s" % aKey)

		for anItem in aDict.get(aKey):
			print("\t%s" % anItem) 

# write to the specified output file
fn = sys.argv[1]
outFile = open(fn, "w") 
someRVal = yaml.dump(categoriesList, outFile)
print(someRVal)