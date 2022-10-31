import requests
import json

API_Key = "ff0f47d28bbc4da4184b9e973fc44d12"
lat = 50.45466
lon = 30.5238
url = (f"http://api.openweathermap.org/date/2.5/weather?lat={lat}&lon={lon}&appid={API_Key}")

resposta = requests.request("GET" ,url)
objetos = json.loads(resposta.text)
dados = objetos["dados"]

for i in objetos:
    print(f"{i} :: {objetos[i]}")
