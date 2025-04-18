import os

files = ['1.txt', '2.txt', '3.txt']
folder = '.'
result_file = 'result.txt'

file_lines_count = {}

for file in files:
    file_path = os.path.join(folder, file)
    with open(file_path, 'r') as f:
        lines = f.readlines()
        file_lines_count[file] = len(lines)

sorted_files = sorted(file_lines_count, key=file_lines_count.get)

with open(result_file, 'w') as result:
    for file in sorted_files:
        file_path = os.path.join(folder, file)
        with open(file_path, 'r') as f:
            lines = f.readlines()
            result.write(f"{len(lines)}\n")
            for i, line in enumerate(lines):
                cleaned_line = ' '.join(line.split())
                result.write(f"Строка номер {i+1} файла номер {file.split('.')[0]}\n")
                result.write(f"{cleaned_line}\n")
            result.write("\n")

print("Файлы объединены успешно.")