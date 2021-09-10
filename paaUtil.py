import re
import shutil
import os

def readConfig(config):

	# read the config.cpp into a string
	with open(config) as c:
		lines = c.readlines()

	return lines

def parseTextures(config, section):

	inSection = False
	Section = []
	Textures = []

	# only look in the designated section of config.cpp
	pattern = re.compile(section)
	for line in config:
		match = re.search(pattern, line)

		if match:
			inSection = True
		
		if inSection:
			Section.append(line)

	# search for lines containing *.paa
	pattern = re.compile("\w+.paa")
	for line in Section:
		match = re.search(pattern, line)

		if match:
			Textures.append(match.group())

	# remove duplicates
	Textures = list(set(Textures))

	return Textures

def createTextures(TextureSource, Textures):
	
	# loop through all textures to create
	for line in Textures:
		# create output directory
		dir = os.getcwd()
		dir = os.path.join(dir, 'output')
		
		if  not os.path.exists(dir):
			os.mkdir(dir)

		# create duplicate of TextureSource named after line in Textures
		shutil.copyfile(TextureSource, os.path.join(dir, line))

	return

def main():

	# get section of config to parse
	section = input("Enter the Section of the config.cpp to parse: ")
	source = input("Enter source texture file name (include extension): ")

	print("Generating *.paa files . . . ")

	config = readConfig('config.cpp')
	Textures = parseTextures(config, section)

	createTextures(source, Textures)

	print("Success!")

	

if __name__ == "__main__":
	# calling main function
	main()