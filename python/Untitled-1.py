import re

with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

filtered_lines = []
for line in lines:
    line = line.strip()
    
    if not re.search(r'Chapter \d+|\d{2}/\d{2}/\d{4}|\d+ ngày trước|\d+ tháng trước|Bỏ theo dõi|\d+ giờ trước|\d+ năm trươc', line):
        if line: 
            filtered_lines.append(line)


unique_titles = []
for title in filtered_lines:
    if title not in unique_titles:
        unique_titles.append(title)


with open('output.txt', 'w', encoding='utf-8') as file:
    for title in unique_titles:
        file.write(title + '\n')

print("Lọc xong, kết quả đã được lưu vào output.txt")
