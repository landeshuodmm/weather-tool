# 读取文件
file = open("test.txt", "r", encoding="utf-8")
content = file.read()
file.close()

print("文件内容:")
print(content)
# 写入文件
file = open("output.txt", "w", encoding="utf-8")
file.write("这是我用 Python 写的第一行文字\n")
file.write("这是第二行\n")
file.close()

print("写入完成！")

# 再读回来确认一下
file = open("output.txt", "r", encoding="utf-8")
print(file.read())
file.close()
words = content.split()
print(words)
print(f"单词数: {len(words)}")