# 🌤 天气查询工具

一个基于 Python 的命令行天气查询工具，调用 wttr.in 免费 API 获取全球城市的实时天气数据。

---

## 功能

- ✅ 查询任意城市的实时天气（温度、体感温度、天气描述、湿度、风速）
- ✅ 支持循环查询，一个会话内可查询多个城市
- ✅ 输入 `q` 安全退出程序
- ✅ 每次查询自动保存到 weather_history.txt
- ✅ 附带时间戳的查询记录，方便回溯

---

## 运行环境

- Python 3.6+
- requests 库

---

## 安装

1. 克隆仓库：

```bash
git clone https://github.com/landeshuodmm/weather-tool.git
cd weather-tool
```

2. 安装依赖：

```bash
pip install requests
```

---

## 使用

```bash
python ai代码练习/day5.py
```

### 示例会话

```
请输入城市名（输入 q 退出）：Beijing

===== Beijing 天气 =====
温度：26°C（体感 25°C）
天气：Partly Cloudy
湿度：30%
风速：13 km/h

请输入城市名（输入 q 退出）：Tokyo

===== Tokyo 天气 =====
温度：19°C（体感 8°C）
天气：Patchy rain nearby
湿度：78%
风速：37 km/h

请输入城市名（输入 q 退出）：q
再见！已保存查询历史到 weather_history.txt
```

### 支持的城市

wttr.in 支持全球绝大多数城市，输入城市英文名即可查询，例如：

- Beijing（北京）
- Shanghai（上海）
- Tokyo（东京）
- London（伦敦）
- New York（纽约）
- Paris（巴黎）

---

## 文件说明

| 文件 | 说明 |
|------|------|
| ai代码练习/day3.py | Day 3 练习：文件读写与单词统计 |
| ai代码练习/day4.py | Day 4 练习：第一个 API 调用（写死城市） |
| ai代码练习/day5.py | 主要程序：可循环查询 + 历史记录的天气工具 |
| weather_history.txt | 查询历史记录（自动生成） |

---

## 数据来源

本工具使用 wttr.in 提供的免费天气 API，无需注册，无需 API Key。

---

## 学习记录

本项目是 AI 开发者学习路线第一周的练习项目。
Day 4：调通第一个 API
Day 5：完善为可循环查询的命令行工具
Day 6：使用 Git 上传到 GitHub
