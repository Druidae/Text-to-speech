import json
import time
import requests

from environs import Env

env: Env = Env()
env.read_env()


def text_to_speech(text="Hello World!"):
    unx_time = int(time.time())

    headers = {
        'Authorization': f'Bearer {env("API_KEY")}'
    }
    url = "https://api.edenai.run/v2/audio/text_to_speech"

    payload = {
        'providers': 'lovoai',
        'language': 'ru-RU',
        # 'option': 'FEMALE',
        # 'lovoai': 'ru-RU_Anna Kravchuk',
        'option': 'MALE',
        'lovoai': 'ru-RU_Alexei Syomin',
        'text': f'{text}'
    }

    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)

    audio_url = result.get('lovoai').get('audio_resource_url')
    r = requests.get(audio_url)

    with open(f"{unx_time}.wav", "wb") as file:
        file.write(r.content)


def main():
    text_to_speech(text="Я много путешествую и, когда в марте 2022 года карты «Виза» и «Мастеркард» российских банков перестали принимать за границей, столкнулся с серьезными проблемами.")
    # print(env('API_KEY'))

if __name__ == "__main__":
    main()
