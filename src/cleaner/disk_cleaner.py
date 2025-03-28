import os
import time
from datetime import datetime
from utils.system_utils import get_file_size, confirm_deletion
from utils.file_utils import write_file
from config.settings import get_settings

class DiskCleaner:
    def __init__(self):
        self.settings = get_settings()
        self.deleted_files = []
        self.deleted_folders = []
        self.total_size = 0

    def clean(self):
        """执行清理操作"""
        paths = self.settings.get_clean_paths()
        
        if not paths:
            print("警告：未设置任何清理路径，请先添加清理路径。")
            return
        
        for path in paths:
            if os.path.exists(path):
                self._clean_path(path)
            else:
                print(f"路径不存在：{path}")
        
        self._print_summary()
    
    def _clean_path(self, path):
        """清理指定路径下的文件和文件夹"""
        print(f"\n开始清理路径: {path}")
        
        for root, dirs, files in os.walk(path, topdown=False):
            # 处理文件
            for file in files:
                file_path = os.path.join(root, file)
                self._process_file(file_path, file)
            
            # 处理文件夹
            for folder in dirs:
                folder_path = os.path.join(root, folder)
                self._process_folder(folder_path, folder)
    
    def _process_file(self, file_path, file_name):
        """处理单个文件"""
        # 检查是否匹配文件名规则
        if file_name in self.settings.get_file_names():
            reason = f"匹配文件名规则: {file_name}"
            self._delete_file(file_path, reason)
            return
        
        # 检查是否匹配敏感文件名规则
        if file_name in self.settings.get_sensitive_files():
            reason = f"匹配敏感文件名规则: {file_name}"
            if confirm_deletion(file_path):
                self._delete_file(file_path, reason)
            return
        
        # 检查是否匹配文件扩展名规则
        _, ext = os.path.splitext(file_name)
        if ext and ext.lower() in [f".{e.lower()}" for e in self.settings.get_file_extensions()]:
            reason = f"匹配文件扩展名规则: {ext}"
            self._delete_file(file_path, reason)
            return
    
    def _process_folder(self, folder_path, folder_name):
        """处理单个文件夹"""
        # 检查是否为空文件夹
        if not os.listdir(folder_path):
            reason = "空文件夹"
            self._delete_folder(folder_path, reason)
            return
        
        # 检查是否匹配文件夹名规则
        if folder_name in self.settings.get_folder_names():
            reason = f"匹配文件夹名规则: {folder_name}"
            self._delete_folder(folder_path, reason)
            return
        
        # 检查是否匹配敏感文件夹名规则
        if folder_name in self.settings.get_sensitive_folders():
            reason = f"匹配敏感文件夹名规则: {folder_name}"
            if confirm_deletion(folder_path):
                self._delete_folder(folder_path, reason)
            return
    
    def _delete_file(self, file_path, reason):
        """删除文件"""
        try:
            file_size = get_file_size(file_path)
            os.remove(file_path)
            deleted_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            file_info = {
                "path": file_path,
                "name": os.path.basename(file_path),
                "size": file_size,
                "reason": reason,
                "time": deleted_time
            }
            
            self.deleted_files.append(file_info)
            self.total_size += file_size if file_size else 0
            
            print(f"已删除文件: {file_path}")
            print(f"  原因: {reason}")
            print(f"  大小: {self._format_size(file_size) if file_size else '未知'}")
        except Exception as e:
            print(f"删除文件 {file_path} 时出错: {e}")
    
    def _delete_folder(self, folder_path, reason):
        """删除文件夹"""
        try:
            # 递归计算文件夹大小
            folder_size = self._calculate_folder_size(folder_path)
            
            try:
                os.rmdir(folder_path)  # 尝试删除空文件夹
            except OSError:
                # 如果不是空文件夹，则递归删除内容
                self._remove_folder_recursively(folder_path)
            
            deleted_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            folder_info = {
                "path": folder_path,
                "name": os.path.basename(folder_path),
                "size": folder_size,
                "reason": reason,
                "time": deleted_time
            }
            
            self.deleted_folders.append(folder_info)
            self.total_size += folder_size
            
            print(f"已删除文件夹: {folder_path}")
            print(f"  原因: {reason}")
            print(f"  大小: {self._format_size(folder_size)}")
        except Exception as e:
            print(f"删除文件夹 {folder_path} 时出错: {e}")
    
    def _calculate_folder_size(self, folder_path):
        """计算文件夹大小"""
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(folder_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                if os.path.exists(fp):
                    total_size += os.path.getsize(fp)
        return total_size
    
    def _remove_folder_recursively(self, folder_path):
        """递归删除文件夹及其内容"""
        for root, dirs, files in os.walk(folder_path, topdown=False):
            for file in files:
                os.remove(os.path.join(root, file))
            for folder in dirs:
                os.rmdir(os.path.join(root, folder))
        os.rmdir(folder_path)
    
    def _format_size(self, size_bytes):
        """格式化文件大小显示"""
        if size_bytes < 1024:
            return f"{size_bytes} B"
        elif size_bytes < 1024 * 1024:
            return f"{size_bytes/1024:.2f} KB"
        elif size_bytes < 1024 * 1024 * 1024:
            return f"{size_bytes/(1024*1024):.2f} MB"
        else:
            return f"{size_bytes/(1024*1024*1024):.2f} GB"
    
    def _print_summary(self):
        """打印清理摘要"""
        if not self.deleted_files and not self.deleted_folders:
            print("\n=== 清理完成 ===")
            print("未删除任何文件或文件夹。")
            return
        
        print("\n" + "="*50)
        print("=== 清理摘要 ===")
        print(f"删除文件总数: {len(self.deleted_files)}")
        print(f"删除文件夹总数: {len(self.deleted_folders)}")
        print(f"总节省空间: {self._format_size(self.total_size)}")
        print("="*50)
        
        # 生成详细报告
        self._generate_report()
    
    def _generate_report(self):
        """生成详细清理报告"""
        report_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "清理报告.txt")
        
        report = []
        report.append("="*80)
        report.append(f"WindowsCleanner 清理报告 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("="*80)
        report.append("")
        
        report.append("=== 删除的文件 ===")
        if self.deleted_files:
            for i, file in enumerate(self.deleted_files, 1):
                report.append(f"{i}. {file['name']}")
                report.append(f"   路径: {file['path']}")
                report.append(f"   大小: {self._format_size(file['size']) if file['size'] else '未知'}")
                report.append(f"   原因: {file['reason']}")
                report.append(f"   时间: {file['time']}")
                report.append("")
        else:
            report.append("无")
            report.append("")
        
        report.append("=== 删除的文件夹 ===")
        if self.deleted_folders:
            for i, folder in enumerate(self.deleted_folders, 1):
                report.append(f"{i}. {folder['name']}")
                report.append(f"   路径: {folder['path']}")
                report.append(f"   大小: {self._format_size(folder['size'])}")
                report.append(f"   原因: {folder['reason']}")
                report.append(f"   时间: {folder['time']}")
                report.append("")
        else:
            report.append("无")
            report.append("")
        
        report.append("="*80)
        report.append(f"总节省空间: {self._format_size(self.total_size)}")
        report.append("="*80)
        
        try:
            write_file(report_path, "\n".join(report))
            print(f"\n详细报告已保存到: {report_path}")
        except Exception as e:
            print(f"生成报告时出错: {e}")