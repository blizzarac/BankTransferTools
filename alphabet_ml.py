
import re

# Split a string into words
def disect_string(str):
	return re.findall(r"[\w']+", str)

# assign a number to a string and fill dict
def map_string(str, hash):
	if(not hash.has_key(str)):
		hash[str] = len(hash)

# takes a string splits it into words and uses map_string to fill hash dict
def hash_string(str, hash):
	for str in disect_string(str):
		map_string(str, hash)