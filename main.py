import requests
from pprint import pprint
import os



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



class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, path_to_file):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": path_to_file, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload(self, path_to_file, file_name):
        href = self._get_upload_link(path_to_file=path_to_file).get("href", "")
        response = requests.put(href, data=open(file_name, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':
    file_name = 'Superheroes_api.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload('folder/heroes','Superheroes_api.txt')