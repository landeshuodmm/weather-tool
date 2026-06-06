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

## 快速开始

### 环境要求

- Python 3.6+
- requests 库

### 安装与运行

```bash
# 克隆仓库
git clone https://github.com/landeshuodmm/weather-tool.git
cd weather-tool

# 安装依赖
pip install requests

# 运行
python weather.py
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
| weather.py | 主程序：查询天气并保存历史记录 |
| weather_history.txt | 查询历史记录（自动生成） |

---

## 数据来源

本工具使用 [wttr.in](https://github.com/chubin/wttr.in) 提供的免费天气 API，无需注册，无需 API Key。

---

## 学习记录

本项目是 AI 开发者学习路线第一周的练习项目。
Day 4：调通第一个 API
Day 5：完善为可循环查询的命令行工具
Day 6：使用 Git 上传到 GitHub
