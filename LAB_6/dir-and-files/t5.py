path = "your/path"

def write_list_to_file(file_path, lst):
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(f"{item}\n" for item in lst)

write_list_to_file(path, ["apple", "banana", "cherry"])
