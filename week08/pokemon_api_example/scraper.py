import requests as r
import json
import parser
import time

BASE_URL = 'http://pokeapi.co/api/v2/'

def get_pokemon_data(pokenumber):
	request_url = BASE_URL + 'pokemon/%s' % pokenumber
	pokedata = r.get(request_url)
	return pokedata.json()

def get_gender_data(pokenumber):
	request_url = BASE_URL + 'gender/%s' % pokenumber
	pokedata = r.get(request_url)
	return pokedata.json()

# with open('bulbasaur.txt', 'w') as outfile:
# 	json.dump(get_pokemon_data(1), outfile)

# with open('bulbasaur_gender.txt', 'w') as outfile:
# 	json.dump(get_gender_data(1), outfile)

gender_data = get_gender_data(1)

for x in range(1, 5):
	pokemon_data = get_pokemon_data(x)
	time.sleep(1)
	print parser.return_pokemon_information(pokemon_data, gender_data)