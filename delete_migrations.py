import os
import re
import shutil

for root, dirs, files in os.walk("."):
    for name in dirs:
        if name == '__pycache__':
            print('删除：', os.path.join(root, name), '文件夹')
            shutil.rmtree(os.path.join(root, name))
    for name in files:
        if re.search(r'\d{4}_.+\.py', name):
            print('删除：', os.path.join(root, name), '文件')
            os.remove(os.path.join(root, name))
