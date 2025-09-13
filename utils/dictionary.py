import requests

URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"


def get_definition(word):
    if word:
        url = URL + word
        response = requests.get(url)

        if response.status_code == 200:
            response_content = response.json()[0]
            print(
                response_content["meanings"][0]["definitions"][0]["definition"]
            )  # TODO: Show on gui
        else:
            print(f"Error: {response.status_code}")  # TODO: Show on gui
