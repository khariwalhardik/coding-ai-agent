import os

def get_file_info(working_dir, directory=None):
    target_dir = os.path.join(working_dir, directory) if directory else working_dir
    file_info_list = []

    for root, dirs, files in os.walk(target_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            file_info_list.append((file_path, file_size))

    return file_info_list