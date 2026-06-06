import requests
from datetime import datetime

while True:
    city = input("请输入城市名（输入 q 退出）：")
    
    if city == "q":
        with open("weather_history.txt", "a", encoding="utf-8") as f:
            f.write(f"=== 会话结束于 {datetime.now()} ===\n\n")
        print("再见！已保存查询历史到 weather_history.txt")
        break
    
    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)
    
    data = response.json()
    current = data["current_condition"][0]
    
    temp = current["temp_C"]
    feels = current["FeelsLikeC"]
    desc = current["weatherDesc"][0]["value"]
    humidity = current["humidity"]
    wind = current["windspeedKmph"]
    
    print(f"\n===== {city} 天气 =====")
    print(f"温度：{temp}°C（体感 {feels}°C）")
    print(f"天气：{desc}")
    print(f"湿度：{humidity}%")
    print(f"风速：{wind} km/h\n")
    
    with open("weather_history.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M')} | {city} | {temp}°C | {desc} | 湿度{humidity}% | 风速{wind}km/h\n")