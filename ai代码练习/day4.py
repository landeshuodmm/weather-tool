import requests

url = f"https://wttr.in/Shanghai?format=j1"
response = requests.get(url)

data = response.json()
current = data["current_condition"][0]

temp = current["temp_C"]
feels = current["FeelsLikeC"]
desc = current["weatherDesc"][0]["value"]
humidity = current["humidity"]
wind = current["windspeedKmph"]

print(f"\n===== shanghai 天气 =====")
print(f"温度：{temp}°C（体感 {feels}°C）")
print(f"天气：{desc}")
print(f"湿度：{humidity}%")
print(f"风速：{wind} km/h")