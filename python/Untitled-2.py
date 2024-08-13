import re

# Hàm để chuyển đổi dòng dữ liệu thành định dạng mới
def convert_format(line):
    # Tìm tên truyện, số chương, và ngày
    match = re.match(r'^(.*) Chapter (\d+) (\d{2}/\d{2}/\d{4})$', line)
    if match:
        title = match.group(1).strip()
        chapter = match.group(2).strip()
        date = match.group(3).strip()
        return f"{title} Chapter {chapter} {date}"
    
    return line

# Mở file và đọc dữ liệu
with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Chuyển đổi định dạng cho từng dòng dữ liệu
converted_lines = [convert_format(line.strip()) for line in lines]

# Ghi lại dữ liệu đã chuyển đổi vào file mới
with open('output_formatted.txt', 'w', encoding='utf-8') as file:
    for line in converted_lines:
        
        file.write(line + '\n')

print("Chuyển đổi xong, kết quả đã được lưu vào output_formatted.txt")
