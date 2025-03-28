import os
import sys
from config.settings import get_settings
from cleaner.disk_cleaner import DiskCleaner

def clear_screen():
    """清屏"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """打印程序头信息"""
    print("="*60)
    print("  WindowsCleanner V0.0.0")
    print("  作者: Arshtyi")
    print("  日期: 2025/3/25")
    print("="*60)
    print()

def show_main_menu():
    """显示主菜单"""
    print("请选择操作:")
    print("1. 执行清理")
    print("2. 管理清理路径")
    print("3. 管理文件扩展名")
    print("4. 管理文件夹名")
    print("5. 管理文件名")
    print("6. 管理敏感文件")
    print("7. 管理敏感文件夹")
    print("0. 退出程序")
    
    choice = input("\n请输入选项 [0-7]: ")
    return choice

def manage_paths():
    """管理清理路径"""
    settings = get_settings()
    while True:
        clear_screen()
        print_header()
        print("=== 管理清理路径 ===\n")
        
        paths = settings.get_clean_paths()
        if paths:
            print("当前清理路径:")
            for i, path in enumerate(paths, 1):
                print(f"{i}. {path}")
        else:
            print("当前没有设置任何清理路径。")
        
        print("\n操作选项:")
        print("1. 添加路径")
        print("2. 删除路径")
        print("0. 返回主菜单")
        
        choice = input("\n请输入选项 [0-2]: ")
        
        if choice == '0':
            break
        elif choice == '1':
            new_path = input("请输入要添加的路径: ")
            if os.path.exists(new_path):
                if settings.add_clean_path(new_path):
                    print(f"成功添加路径: {new_path}")
                else:
                    print("该路径已存在，无需重复添加。")
            else:
                print("错误: 路径不存在，请检查后重试。")
            input("按Enter键继续...")
        elif choice == '2':
            if not paths:
                print("没有路径可删除。")
                input("按Enter键继续...")
                continue
            
            index = input(f"请输入要删除的路径编号 [1-{len(paths)}]: ")
            try:
                index = int(index) - 1
                if 0 <= index < len(paths):
                    removed_path = paths[index]
                    if settings.remove_clean_path(removed_path):
                        print(f"成功删除路径: {removed_path}")
                    else:
                        print("删除失败。")
                else:
                    print("无效的编号。")
            except ValueError:
                print("请输入有效的数字。")
            input("按Enter键继续...")

def manage_list(get_func, add_func, remove_func, title, item_type):
    """通用列表管理函数"""
    while True:
        clear_screen()
        print_header()
        print(f"=== {title} ===\n")
        
        items = get_func()
        if items:
            print(f"当前{item_type}:")
            for i, item in enumerate(items, 1):
                print(f"{i}. {item}")
        else:
            print(f"当前没有设置任何{item_type}。")
        
        print("\n操作选项:")
        print(f"1. 添加{item_type}")
        print(f"2. 删除{item_type}")
        print("0. 返回主菜单")
        
        choice = input("\n请输入选项 [0-2]: ")
        
        if choice == '0':
            break
        elif choice == '1':
            new_item = input(f"请输入要添加的{item_type}: ")
            if add_func(new_item):
                print(f"成功添加{item_type}: {new_item}")
            else:
                print(f"该{item_type}已存在，无需重复添加。")
            input("按Enter键继续...")
        elif choice == '2':
            if not items:
                print(f"没有{item_type}可删除。")
                input("按Enter键继续...")
                continue
            
            index = input(f"请输入要删除的{item_type}编号 [1-{len(items)}]: ")
            try:
                index = int(index) - 1
                if 0 <= index < len(items):
                    removed_item = items[index]
                    if remove_func(removed_item):
                        print(f"成功删除{item_type}: {removed_item}")
                    else:
                        print("删除失败。")
                else:
                    print("无效的编号。")
            except ValueError:
                print("请输入有效的数字。")
            input("按Enter键继续...")

def main():
    """主函数"""
    settings = get_settings()
    
    while True:
        clear_screen()
        print_header()
        choice = show_main_menu()
        
        if choice == '0':
            print("\n感谢使用WindowsCleanner! 再见!")
            break
        elif choice == '1':
            clear_screen()
            print_header()
            print("=== 开始执行清理 ===\n")
            
            cleaner = DiskCleaner()
            cleaner.clean()
            
            input("\n清理完成。按Enter键返回主菜单...")
        elif choice == '2':
            manage_paths()
        elif choice == '3':
            manage_list(
                settings.get_file_extensions,
                settings.add_file_extension,
                settings.remove_file_extension,
                "管理文件扩展名",
                "文件扩展名"
            )
        elif choice == '4':
            manage_list(
                settings.get_folder_names,
                settings.add_folder_name,
                settings.remove_folder_name,
                "管理文件夹名",
                "文件夹名"
            )
        elif choice == '5':
            manage_list(
                settings.get_file_names,
                settings.add_file_name,
                settings.remove_file_name,
                "管理文件名",
                "文件名"
            )
        elif choice == '6':
            manage_list(
                settings.get_sensitive_files,
                settings.add_sensitive_file,
                settings.remove_sensitive_file,
                "管理敏感文件",
                "敏感文件名"
            )
        elif choice == '7':
            manage_list(
                settings.get_sensitive_folders,
                settings.add_sensitive_folder,
                settings.remove_sensitive_folder,
                "管理敏感文件夹",
                "敏感文件夹名"
            )
        else:
            print("无效选项，请重试。")
            input("按Enter键继续...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n程序被用户中断。")
        sys.exit(0)
    except Exception as e:
        print(f"\n程序出错: {e}")
        input("按Enter键退出...")
        sys.exit(1)