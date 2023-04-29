import json

import requests

with open("api_key.json") as f:
    contents = json.loads(f)
    elevenlabs_api_key = contents.get("elevenlabs_api_key")
    dezgo_api_key = contents.get("dezgo_api_key")

elevenlabs_bella_voice_id = "EXAVITQu4vr4xnSDxMaL"
elevenlabs_model_id = "eleven_monolingual_v1"

text_to_speech_url = "https://api.elevenlabs.io/v1/text-to-speech"
text_to_speech_url = f"{text_to_speech_url}/{elevenlabs_bella_voice_id}"

headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": f"{elevenlabs_api_key}"
}

data = {
    "text": "Captain Fluffington's treasure had achieved its true purpose",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.75
    }
}

response = requests.post(text_to_speech_url, json=data, headers=headers)
with open('output.mp3', 'wb') as f:
    for chunk in response.iter_content(chunk_size=300):
        if chunk:
            f.write(chunk)
