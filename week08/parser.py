import json

with open('bulbasaur.txt', 'r') as infile:
	json_data = json.load(infile)

def extract_base_experience(json_blob):
	return json_blob['base_experience']

base_experience = extract_base_experience(json_data)

print 'Bulbasaur\'s base experience is %s' % base_experience