# Profanity Checker
#
# By PK
# Udacity Programming Foundations
# August 2016


import urllib

def check_profanity(text):
	"""
	Takes text and runs it against www.wdylike.appspot.com
	to determine if text contains profanity. Returns string 
	'true' or 'false'
	"""

	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text)
	output = connection.read()
	connection.close()
	return output

def read_text(doc_path):
	"""
	Takes a document path as an argument. Checks the text
	of the document for profanity. Returns the line
	where 1st instance of profanity occurs.
	"""
	
	with open(doc_path, 'r') as file:
		file.seek(0)
		for line_num, line in enumerate(file.readlines()):
			result = check_profanity(line)
			if result == 'true':
				return "A bad word was found in the line below: \n \n" + line
	return "No bad words were found in your document."

print read_text("/Users/Patchy/Documents/Coding/Udacity_Programming Foundations/sample_text.txt")