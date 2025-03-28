# WindowsCleanner

-   WindowsCleanner 是一个用于清理 Windows 系统中不必要文件的 Python 项目。该项目旨在帮助用户释放磁盘空间，优化系统性能，并保持系统的整洁。
-   ~~本项目没有人工痕迹~~
-   使用前请务必注意配置规则，~~误删请吟唱亲人两行泪~~

## 功能

-   **磁盘清理**：通过指定路径，删除符合条件的文件和文件夹。
-   **临时文件清理**：专门处理和删除临时文件，释放存储空间。
-   **配置管理**：可以灵活配置清理规则，包括：
    -   清理路径
    -   文件扩展名
    -   文件夹名称
    -   文件名称
    -   敏感文件（需确认）
    -   敏感文件夹（需确认）

## 文件结构

```
WindowsCleanner
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── cleaner
│   │   ├── __init__.py
│   │   ├── disk_cleaner.py
│   │   ├── temp_cleaner.py
│   │   └── registry_cleaner.py
│   ├── utils
│   │   ├── __init__.py
│   │   ├── file_utils.py
│   │   └── system_utils.py
│   └── config
│       ├── __init__.py
│       └── settings.py
├── tests
│   ├── __init__.py
│   ├── test_disk_cleaner.py
│   ├── test_temp_cleaner.py
│   └── test_registry_cleaner.py
├── requirements.txt
├── setup.py
└── README.md
```

## 安装

1. 克隆该项目到本地：
    ```
    git clone https://github.com/Arshtyi/Windows-Cleanner.git
    ```
2. 进入项目目录：
    ```
    cd WindowsCleanner
    ```
3. 安装依赖：
    ```
    pip install -r requirements.txt
    ```

## 使用

1. 运行主程序：
    ```
    python src/main.py
    ```
2. 在主菜单中选择操作：

-   执行清理
-   管理清理路径
-   管理文件扩展名
-   管理文件夹名
-   管理文件名
-   管理敏感文件
-   管理敏感文件夹

## 注意事项

-   在执行清理前，请确保已正确配置清理规则
-   对于敏感文件和文件夹，系统会在删除前请求确认
-   每次清理操作完成后，会在项目根目录生成详细的清理报告

## 作者

-   **Arshtyi** - _初始工作_ - [Arshtyi](https://github.com/Arshtyi)

## 版本

-   版本：V0.0.0
-   日期：2025/3/25

## 许可证

该项目采用 MIT 许可证，详情请参阅 LICENSE 文件。
