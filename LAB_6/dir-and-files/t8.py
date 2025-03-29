import os

def delete_file(file_path):
    if os.path.exists(file_path) and os.access(file_path, os.W_OK):
        os.remove(file_path)
        return "File deleted"
    return "File not found or access denied"

print(delete_file("so-so.py"))
