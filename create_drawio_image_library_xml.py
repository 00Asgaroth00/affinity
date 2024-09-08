#!/usr/bin/env python3

#
# Borrowed from https://github.com/ecceman/affinity/pull/7#issuecomment-1424946510
#

import os
import base64
import json

folder_path = 'blue'
output_file = 'output.xml'
image_list = []

# Iterate through the files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.svg'):  # Only process SVG files
        # Read the file content and encode it to base64
        with open(os.path.join(folder_path, file_name), 'rb') as f:
            encoded_content = base64.b64encode(f.read()).decode('utf-8')
        
        # Add the file data to the list
        image_list.append({
            'data': f'data:image/svg+xml;base64,{encoded_content}',
            'w': 50,
            'h': 50,
            'title': os.path.splitext(file_name)[0].replace("_blue",""),
            'aspect': 'fixed'
        })

# Output the XML format to a file
with open(output_file, 'w') as f:
    f.write('<mxlibrary>\n[\n')
    for i, image_data in enumerate(image_list):
        json_str = json.dumps(image_data, ensure_ascii=False)
        if i == len(image_list) - 1:
            f.write(f'\t{json_str}\n')
        else:
            f.write(f'\t{json_str},\n')
    f.write(']\n</mxlibrary>')
    
