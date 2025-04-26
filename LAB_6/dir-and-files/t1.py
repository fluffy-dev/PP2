import os

path = r"C:\Users\JJ\code"

print("DIRS:")
for item in os.listdir(path):
    if os.path.isdir(os.path.join(path, item)):
        print(item)

print("FILES:")
for item in os.listdir(path):
    if os.path.isfile(os.path.join(path, item)):
        print(item)

print(os.listdir(path))
