import json

with open('bulbasaur.txt', 'r') as infile:
	json_data = json.load(infile)

def extract_base(json_blob, json_key):
	return json_blob[json_key]

def stats_list(list_of_data):
	return [(item['stat']['name'], item['base_stat']) for item in list_of_data]

def types_list(list_of_data):
	return [(item['slot'], item['type']['name']) for item in list_of_data]

base_experience = extract_base(json_data, 'base_experience')
height = extract_base(json_data, 'height')
weight = extract_base(json_data, 'weight')
base_stats = stats_list(extract_base(json_data, 'stats'))

print 'Bulbasaur\'s base experience is %s' % base_experience
print 'Its height is %s' % height
print 'Its weight is %s' % weight
for item in base_stats:
	print 'Bulby\'s %s starts at %s' % (item[0], item[1])

for item in types_list(extract_base(json_data, 'types')):
	print 'Bulby\'s type %s is %s' % (item[0], item[1])