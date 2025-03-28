import os
import shutil

def get_file_size(file_path):
    """获取文件大小（以字节为单位）"""
    try:
        if os.path.isfile(file_path):
            return os.path.getsize(file_path)
        return None
    except:
        return None

def confirm_deletion(path):
    """确认删除操作"""
    print("\n" + "!"*50)
    print(f"警告：即将删除敏感项目:")
    print(f"路径: {path}")
    
    if os.path.isfile(path) and os.path.exists(path):
        size = get_file_size(path)
        print(f"类型: 文件")
        print(f"大小: {format_size(size) if size else '未知'}")
    elif os.path.isdir(path) and os.path.exists(path):
        print(f"类型: 文件夹")
    
    print("!"*50)
    
    response = input("确定要删除吗? (y/n): ")
    return response.lower() == 'y'

def format_size(size_bytes):
    """格式化文件大小显示"""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes/1024:.2f} KB"
    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes/(1024*1024):.2f} MB"
    else:
        return f"{size_bytes/(1024*1024*1024):.2f} GB"