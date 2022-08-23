import requests
from pprint import pprint
import json

class Superhero:

    def test_req(self):
        the_url = 'https://akabab.github.io/superhero-api/api/all.json'
        response = requests.get(the_url)
        return response.json()


if __name__ == '__main__':
    heroes_list = ['Hulk', 'Captain America', 'Thanos']
    heroes_dict = {}
    chars_list = []
    hero = Superhero()
    the_file = hero.test_req()
    # pprint(the_file)
    for element in heroes_list:
        for item in the_file:
            if item['name'] == element:
                chars_list.append({'name': item['name'], 'intelligence': item['powerstats']['intelligence']})
    max_brain = 0
    for item in chars_list:
        if item['intelligence'] > max_brain:
            max_brain = item['intelligence']
            smartest_hero = item['name']
    print(smartest_hero)
