import json

with open('bulbasaur.txt', 'r') as infile:
	json_data = json.load(infile)

with open('bulbasaur_gender.txt', 'r') as infile:
	gender_data = json.load(infile)

def extract_base(json_blob, json_key):
	return json_blob[json_key]

def stats_list(list_of_data):
	return [(item['stat']['name'], item['base_stat']) for item in list_of_data]

def types_list(list_of_data):
	return [(item['slot'], item['type']['name']) for item in list_of_data]

def rate_parse(number):
	if number == -1:
		return -1
	else:
		return number / float(8)

def get_pokenumber(url):
	return url.split('/')[-2]

def all_pokemon_gender(list_of_data):
	data_dictionary = {}
	for item in list_of_data:
		rate = rate_parse(item['rate'])
		pokemon_name = item['pokemon_species']['name']
		id_number = get_pokenumber(item['pokemon_species']['url'])
		data_dictionary[id_number] = {'name': pokemon_name, 'rate': rate}
	return data_dictionary

base_experience = extract_base(json_data, 'base_experience')
height = extract_base(json_data, 'height')
weight = extract_base(json_data, 'weight')
base_stats = stats_list(extract_base(json_data, 'stats'))
gender_dictionary = all_pokemon_gender(extract_base(gender_data, 'pokemon_species_details'))

print 'Bulbasaur\'s base experience is %s' % base_experience
print 'Its height is %s' % height
print 'Its weight is %s' % weight
for item in base_stats:
	print 'Bulby\'s %s starts at %s' % (item[0], item[1])

for item in types_list(extract_base(json_data, 'types')):
	print 'Bulby\'s type %s is %s' % (item[0], item[1])

print 'Bulbasaur has a %s chance of being female' % gender_dictionary['1']['rate']