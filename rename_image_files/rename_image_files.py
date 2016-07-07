import os
from urllib.parse import unquote

dir = '/Users/vasilty/Documents/Treehouse/project6_mineral_catalog/rename_image_files/images'
with open('rename.sh', 'w') as f:
    f.write('#!/bin/bash\n')
    for root, dirs, filenames in os.walk(dir):
        for file in filenames:
            new_name = unquote(file)
            if '(' in new_name:
                new_name = new_name.replace('(', '\(')
            if ')' in new_name:
                new_name = new_name.replace(')', '\)')
            if "'" in new_name:
                new_name = new_name.replace("'", "\'")
            # print(file, new_name)
            if file != new_name:
                print(file, new_name)
                f.write('mv -v images/{} images/{}\n'.format(file, new_name))
