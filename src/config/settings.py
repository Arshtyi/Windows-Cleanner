import os
import json

class Settings:
    def __init__(self):
        self.config_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "config")
        # 确保配置目录存在
        if not os.path.exists(self.config_dir):
            os.makedirs(self.config_dir)
        
        # 配置文件路径
        self.paths_file = os.path.join(self.config_dir, "clean_paths.txt")
        self.extensions_file = os.path.join(self.config_dir, "file_extensions.txt")
        self.folder_names_file = os.path.join(self.config_dir, "folder_names.txt")
        self.file_names_file = os.path.join(self.config_dir, "file_names.txt")
        self.sensitive_files_file = os.path.join(self.config_dir, "sensitive_files.txt")
        self.sensitive_folders_file = os.path.join(self.config_dir, "sensitive_folders.txt")
        
        # 初始化配置文件
        self._initialize_files()
    
    def _initialize_files(self):
        """初始化所有配置文件"""
        files = [
            self.paths_file,
            self.extensions_file,
            self.folder_names_file,
            self.file_names_file,
            self.sensitive_files_file,
            self.sensitive_folders_file
        ]
        
        for file_path in files:
            if not os.path.exists(file_path):
                with open(file_path, 'w', encoding='utf-8'):
                    pass
    
    def _read_lines(self, file_path):
        """读取文件中的所有行"""
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                return [line.strip() for line in file.readlines() if line.strip()]
        return []
    
    def _write_lines(self, file_path, lines):
        """写入行到文件"""
        with open(file_path, 'w', encoding='utf-8') as file:
            for line in lines:
                file.write(f"{line}\n")
    
    # 路径管理
    def get_clean_paths(self):
        return self._read_lines(self.paths_file)
    
    def add_clean_path(self, path):
        paths = self.get_clean_paths()
        if path not in paths:
            paths.append(path)
            self._write_lines(self.paths_file, paths)
            return True
        return False
    
    def remove_clean_path(self, path):
        paths = self.get_clean_paths()
        if path in paths:
            paths.remove(path)
            self._write_lines(self.paths_file, paths)
            return True
        return False
    
    # 文件扩展名管理
    def get_file_extensions(self):
        return self._read_lines(self.extensions_file)
    
    def add_file_extension(self, extension):
        extensions = self.get_file_extensions()
        if extension not in extensions:
            extensions.append(extension)
            self._write_lines(self.extensions_file, extensions)
            return True
        return False
    
    def remove_file_extension(self, extension):
        extensions = self.get_file_extensions()
        if extension in extensions:
            extensions.remove(extension)
            self._write_lines(self.extensions_file, extensions)
            return True
        return False
    
    # 文件夹名管理
    def get_folder_names(self):
        return self._read_lines(self.folder_names_file)
    
    def add_folder_name(self, name):
        names = self.get_folder_names()
        if name not in names:
            names.append(name)
            self._write_lines(self.folder_names_file, names)
            return True
        return False
    
    def remove_folder_name(self, name):
        names = self.get_folder_names()
        if name in names:
            names.remove(name)
            self._write_lines(self.folder_names_file, names)
            return True
        return False
    
    # 文件名管理
    def get_file_names(self):
        return self._read_lines(self.file_names_file)
    
    def add_file_name(self, name):
        names = self.get_file_names()
        if name not in names:
            names.append(name)
            self._write_lines(self.file_names_file, names)
            return True
        return False
    
    def remove_file_name(self, name):
        names = self.get_file_names()
        if name in names:
            names.remove(name)
            self._write_lines(self.file_names_file, names)
            return True
        return False
    
    # 敏感文件名管理
    def get_sensitive_files(self):
        return self._read_lines(self.sensitive_files_file)
    
    def add_sensitive_file(self, name):
        names = self.get_sensitive_files()
        if name not in names:
            names.append(name)
            self._write_lines(self.sensitive_files_file, names)
            return True
        return False
    
    def remove_sensitive_file(self, name):
        names = self.get_sensitive_files()
        if name in names:
            names.remove(name)
            self._write_lines(self.sensitive_files_file, names)
            return True
        return False
    
    # 敏感文件夹名管理
    def get_sensitive_folders(self):
        return self._read_lines(self.sensitive_folders_file)
    
    def add_sensitive_folder(self, name):
        names = self.get_sensitive_folders()
        if name not in names:
            names.append(name)
            self._write_lines(self.sensitive_folders_file, names)
            return True
        return False
    
    def remove_sensitive_folder(self, name):
        names = self.get_sensitive_folders()
        if name in names:
            names.remove(name)
            self._write_lines(self.sensitive_folders_file, names)
            return True
        return False

# 单例模式，保证全局只有一个配置实例
_settings_instance = None

def get_settings():
    global _settings_instance
    if _settings_instance is None:
        _settings_instance = Settings()
    return _settings_instance