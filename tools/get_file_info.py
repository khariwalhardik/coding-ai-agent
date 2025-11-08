import os

def get_file_info(working_dir, directory=None):
    target_dir = os.path.join(working_dir, directory) if directory else working_dir
    file_info_list = []
    #what if directory does not exit 
    if not os.path.exists(target_dir):
        return f"Directory does not exist: {target_dir}"
    # i have to print file name, file size and isdir or not
    output_string = ""
    for root, dirs, files in os.walk(target_dir):
        for name in files:
            file_path = os.path.join(root, name)
            file_size = os.path.getsize(file_path)
            output_string += f"File: {name}, Size: {file_size} bytes, IsDir: False\n"
        for name in dirs:
            dir_path = os.path.join(root, name)
            dir_size = sum(os.path.getsize(os.path.join(dirpath, filename)) 
                           for dirpath, dirnames, filenames in os.walk(dir_path) 
                           for filename in filenames)
            output_string += f"Directory: {name}, Size: {dir_size} bytes, IsDir: True\n"
        break  # prevent descending into subdirectories
    return output_string
