import json

import requests

with open("api_key.json") as f:
    contents = json.loads(f.read())
    elevenlabs_api_key = contents.get("elevenlabs_api_key")
    dezgo_api_key = contents.get("dezgo_api_key")

with open("input_text.txt") as f:
    contents = f.read().strip()

with open("dezgo_negative_prompt.txt") as f:
    dezgo_negative_prompt = f.read().strip()

elevenlabs_headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": f"{elevenlabs_api_key}"
}

elevenlabs_bella_voice_id = "EXAVITQu4vr4xnSDxMaL"
elevenlabs_model_id = "eleven_monolingual_v1"

elevenlabs_api_url = "https://api.elevenlabs.io/v1/text-to-speech"
text_to_speech_url = f"{elevenlabs_api_url}/{elevenlabs_bella_voice_id}"

dezgo_model_id = "anything_5_0"
dezgo_api_url = "https://api.dezgo.com"
text_to_image_url = f"{dezgo_api_url}/text2image"

dezgo_headers = {
    "Content-Type": "application/json",
    "X-Dezgo-Key": f"{dezgo_api_key}"
}


def download_audio(text, output):
    data = {
        "text": text,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }

    response = requests.post(text_to_speech_url,
                             json=data,
                             headers=elevenlabs_headers)
    with open(f"Out/{output}.mp3", "wb") as f:
        for chunk in response.iter_content(chunk_size=10240):
            if chunk:
                f.write(chunk)


def download_image(text, output):
    data = {
        "width": 960,
        "height": 540,
        "prompt": text,
        "model": dezgo_model_id,
        "negative_prompt": dezgo_negative_prompt,
        "upscale": 2
    }

    response = requests.post(text_to_image_url,
                             json=data,
                             headers=dezgo_headers)

    with open(f"Out/{output}.png", "wb") as f:
        f.write(response.content)


for i, j in enumerate(contents.split("\n\n")):
    download_audio(j, i + 1)
    download_image(j, i+1)
