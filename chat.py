import os

#讀取檔案
def read_flie():
	lines = []
	with open("input.txt", "r", encoding = "utf-8") as f:
		for line in f:
			lines.append(line)
	return lines


lines = read_flie()
print(lines)
