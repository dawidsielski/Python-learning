import shutil
import os

script_path = os.path.dirname(os.path.abspath(__file__))
print(script_path)

# shutil.copy(str(os.path.join(script_path, "folder1", "something.txt")), str(os.path.join(script_path, "folder2")))

# shutil.copytree(str(os.path.join(script_path, "folder1")), str(os.path.join(script_path, "folder3")))

shutil.copy(str(os.path.join(script_path, "folder1")), str(os.path.join(script_path, "folder2")))