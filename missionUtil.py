import re
from xml.dom import minidom
import os

# imports config.cpp lines into array
def readConfig(config):

	# read the config.cpp into a string
	with open(config) as c:
		lines = c.readlines()

	return lines

# parses class names from config.cpp
def parseTypes(config, camo):
	
	Types = []

	# only pull class names of designated camo type
	pattern = re.compile("class.+_" + camo)
	for line in config:
		match = re.search(pattern, line)

		if match:
			newLine = match.group()

			# remove 'class'
			patternClass = re.compile("class ")
			newLine = patternClass.sub('', newLine)
			Types.append(newLine)
		

	# remove duplicates
	Types = list(set(Types))
	return Types

# generates types.xml entries from class array
def createTypesXML(Types):
	typesDoc = minidom.Document()
	save_path_file = "output\\types.xml"
	typesXML = []
	typeChildren = [[
		"nominal",
		"lifetime",
		"restock",
		"min",
		"quantmin",
		"quantmax",
		"cost",
		"flags",
		"category",
		"usage"
	], 
	[
		"3",
		"7200",
		"0",
		"2",
		"-1",
		"-1",
		"100",
		"-2",
		"-2",
		"-2"
	]]

	# for looping through 2D array
	# rows = len(typeChildren)
	columns = len(typeChildren[0])-1

	# create parent 'types' element
	types = typesDoc.createElement("types")
	typesDoc.appendChild(types)

	for line in Types:
		# create type
		type = typesDoc.createElement("type")
		type.setAttribute('name', line)
		types.appendChild(type)

		# create children
		for j in range(columns):
			typeChild = typesDoc.createElement(typeChildren[0][j])
			if (j < columns-2):
				typeChildText = typesDoc.createTextNode(typeChildren[1][j])
				typeChild.appendChild(typeChildText)
			elif (j == columns-2):
				typeChild.setAttribute('count_in_cargo', "0")
				typeChild.setAttribute('count_in_hoarder', "0")
				typeChild.setAttribute('count_in_map', "1")
				typeChild.setAttribute('count_in_player', "0")
				typeChild.setAttribute('crafted', "0")
				typeChild.setAttribute('deloot', "0")
			elif (j == columns-1):
				typeChild.setAttribute('name', "clothes")
			elif (j == columns):
				typeChild.setAttribute('name', "Military")

			type.appendChild(typeChild)
		
	# prettify the document
	xml_str = typesDoc.toprettyxml(indent = "\t")

	# create output directory
	dir = os.getcwd()
	dir = os.path.join(dir, 'output')
	
	if  not os.path.exists(dir):
		os.mkdir(dir)

	# write the document
	with open(save_path_file, "w") as f:
		f.write(xml_str)
	
	return

# generates trader entries from class array
def createTraderConf(Types):
	
	# create TraderConfig.txt
	traderPath = 'output\\TraderConfig.txt'

	# create output directory
	dir = os.getcwd()
	dir = os.path.join(dir, 'output')
	
	if  not os.path.exists(dir):
		os.mkdir(dir)

	with open(traderPath, 'w') as traderConf:
		
		# create <Category> Header
		traderConf.write("<Category> Modular Vest System\n")

		# loop through Types
		for type in Types:
			line = '\t'+'{:<50s}{:<10s}{:<10s}{:<s}\n'.format(type+",", '*,', '500,', '250')
			traderConf.write(line)

	return

def main():
	print("Parsing config.cpp . . . ")
	config = readConfig('config.cpp')
	Types = parseTypes(config, "M8")
	print("Generating types.xml . . . ")
	createTypesXML(Types)
	print("Generating TraderConfig.txt . . . ")
	createTraderConf(Types)
	print("Success!")

	return

	

if __name__ == "__main__":
	# calling main function
	main()