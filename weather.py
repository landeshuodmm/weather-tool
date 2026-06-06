import requests
from datetime import datetime
import json

print('===== 天气查询工具 =====')
print('输入城市英文名即可查询，例如：Beijing、Tokyo、London')
print('输入 q 退出程序\n')

while True:
    try:
        city = input('请输入城市名（输入 q 退出）：')
    except EOFError:
        break

    if city == 'q':
        with open('weather_history.txt', 'a', encoding='utf-8') as f:
            f.write(f'=== 会话结束于 {datetime.now()} ===\n\n')
        print('再见！已保存查询历史到 weather_history.txt')
        break

    try:
        url = f'https://wttr.in/{city}?format=j1'
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print(f'网络请求失败（状态码：{response.status_code}），请稍后重试\n')
            continue

        try:
            data = response.json()
        except json.JSONDecodeError:
            print(f'没有找到 {city} 的天气数据，请检查城市名是否正确\n')
            continue

        if 'error' in data or not data.get('current_condition'):
            print(f'没有找到 {city} 的天气数据，请检查城市名是否正确\n')
            continue

        current = data['current_condition'][0]
        temp = current['temp_C']
        feels = current['FeelsLikeC']
        desc = current['weatherDesc'][0]['value']
        humidity = current['humidity']
        wind = current['windspeedKmph']

        print(f'\n===== {city} 天气 =====')
        print(f'温度：{temp}°C（体感 {feels}°C）')
        print(f'天气：{desc}')
        print(f'湿度：{humidity}%')
        print(f'风速：{wind} km/h\n')

        with open('weather_history.txt', 'a', encoding='utf-8') as f:
            f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M')} | {city} | {temp}\u00b0C | {desc} | 湿度{humidity}% | 风速{wind}km/h\n")

    except requests.exceptions.ConnectionError:
        print('网络连接失败，请检查网络连接\n')
    except requests.exceptions.Timeout:
        print('请求超时，请检查网络后重试\n')
    except Exception as e:
        print(f'出错了：{e}\n')
