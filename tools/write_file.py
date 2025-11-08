import os

def write_file(working_dir, file_path, content):
    target_file = os.path.join(working_dir, file_path)
    # Ensure the directory exists
    # if file path doesn't exits create the directory and file
    
    os.makedirs(os.path.dirname(target_file), exist_ok=True)
    with open(target_file, 'w') as f:
        f.write(content)
    return f"File written: {target_file}"