def read_file(file_path):
    """读取文件内容"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(file_path, content):
    """写入内容到文件"""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)