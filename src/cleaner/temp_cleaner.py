class TempCleaner:
    def __init__(self, temp_directory):
        self.temp_directory = temp_directory

    def clean_temp_files(self):
        import os
        import time

        # Define the age threshold for temporary files (e.g., 7 days)
        age_threshold = 7 * 24 * 60 * 60  # 7 days in seconds
        current_time = time.time()

        for root, dirs, files in os.walk(self.temp_directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_age = current_time - os.path.getmtime(file_path)

                if file_age > age_threshold:
                    try:
                        os.remove(file_path)
                        print(f"Deleted: {file_path}")
                    except Exception as e:
                        print(f"Error deleting {file_path}: {e}")