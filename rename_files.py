# Rename Files
# By PK
# Udacity Programming Foundations
# August 2016

import os
import os.path

def remove_char_filename():
	"""
	Function that takes a file name and removes characters
	from file name as specified by the user. 
	Takes no arguments. Prompts 2 input strings from the user:
	1) Folder path  2) characters to remove from file name.
	"""

	folder = raw_input("What folder are your files located?")
	file_list = os.listdir(folder)
	chars_to_del = raw_input("Which characters do you want to have removed from the file names?")
	start_dir = os.getcwd()

	os.chdir(folder)

	for file in file_list:
		new_name = file.translate(None, chars_to_del)
		print "Old File Name: ", file
		print "New File Name: ", new_name 
		os.rename(file, new_name)

	os.chdir(start_dir)	
	print "Done."


remove_char_filename()














