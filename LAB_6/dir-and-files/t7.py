def copy_file(src, dest):
    with open(src, "r", encoding="utf-8") as f1, open(dest, "w", encoding="utf-8") as f2:
        f2.write(f1.read())

path = "your/path"
path2 = "your/path"

copy_file(path, path2)
