# Day 2 笔记：Python 核心语法（上）

## 一、变量与赋值

\`\`\`python
name = "小明"        # 字符串 str
age = 18             # 整数 int
height = 1.75        # 浮点数 float
is_student = True    # 布尔值 bool
\`\`\`

- Python 是**动态类型**：变量可以随时换值、换类型
- \`type(变量名)\` 查看变量的类型

---

## 二、字符串操作

\`\`\`python
# 拼接
greeting = "你好" + "，" + "世界" + "！"

# f-string（推荐，最常用）
name = "Alice"
msg = f"我是{name}，今天学 AI 的第 2 天"

# 常用方法
text = "  hello, Python!  "
text.upper()               # 大写
text.strip()               # 去首尾空格
text.replace("Python", "AI") # 替换
len(text)                  # 字符数
\`\`\`

---

## 三、数字运算

\`\`\`python
a = 10
b = 3

a + b   # 13   加法
a - b   # 7    减法
a * b   # 30   乘法
a / b   # 3.33 除法（结果是浮点数）
a // b  # 3    整除
a % b   # 1    取余
a ** 2  # 100  幂运算
\`\`\`

---

## 四、列表（List）

\`\`\`python
fruits = ["苹果", "香蕉", "橘子", "葡萄"]

# 索引（从 0 开始）
fruits[0]       # "苹果"
fruits[-1]      # "葡萄"（-1 是倒数第一个）
fruits[0:2]     # ["苹果", "香蕉"]

# 修改
fruits.append("草莓")    # 末尾追加
fruits[1] = "芒果"       # 按索引替换

# 遍历
for f in fruits:
    print(f)

# 长度
len(fruits)     # 5
\`\`\`

---

## 五、条件判断 if / elif / else

\`\`\`python
score = 85

if score >= 90:
    grade = "优秀"
elif score >= 80:
    grade = "良好"
elif score >= 70:
    grade = "中等"
else:
    grade = "不及格"

# 组合条件
if is_weekend and is_sunny:
    print("去公园！")
elif is_weekend and not is_sunny:
    print("在家看电影")
else:
    print("去上课")
\`\`\`

**规则：**
- 条件后要加冒号 \`:\`
- 条件内的代码要缩进（4 个空格）
- 从上往下匹配，碰到第一个满足的就执行
- \`and\` / \`or\` / \`not\` 组合多个条件

---

## 六、用户输入

\`\`\`python
name = input("请输入你的名字：")
print(f"你好，{name}！")
\`\`\`

- \`input()\` 程序会停下来等用户输入
- 输入的内容作为字符串返回

---

## 记忆口诀

变量是标签，类型自动判
字符串加 f，格式化不愁
列表方括号，索引从 0 数
条件 if 冒号缩进，满足就走不回头
