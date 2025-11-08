import os
MAX_CHAR=10000
def get_file_content(working_dir,file_path):
    target_file = os.path.join(working_dir, file_path)
    # what if file does not exist
    if not os.path.exists(target_file):
        return f"File does not exist: {target_file}"
    with open(target_file, 'r') as f:
        content = f.read(MAX_CHAR)
    return content