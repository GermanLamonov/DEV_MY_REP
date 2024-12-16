def file_reader(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line


def file_reader_python(file_path):
    for line in file_reader(file_path):
        if 'Python' in line:
            yield line


for line in file_reader("example.txt"):
    print(line)
for line in file_reader_python("example.txt"):
    print(line)
