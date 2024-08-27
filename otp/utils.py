import yaml
import re
import os
from datetime import datetime

def read_md(path):
    with open(path, 'r') as file:
        content = file.read()

    yaml_pattern = re.compile(r'^---\n(.*?)\n---', re.DOTALL)
    match = yaml_pattern.search(content)

    if match:
        yaml_content = match.group(1)
        markdown_content = content[match.end():].lstrip()

        try:
            yaml_data = yaml.safe_load(yaml_content)
            return {"yaml" : yaml_data, "markdown" : markdown_content}
        except yaml.YAMLError as e:
            return {"yaml" : None, "markdown" : markdown_content}
    else:
        return {"yaml" : None, "markdown" : markdown_content}
    
def convert_date(date):
    date_format = '%Y-%m-%dT%H:%M'
    return datetime.strptime(date, date_format)

def is_markdown_file(file_path):
    markdown_extensions = {'.md', '.markdown', '.mdown', '.mkd', '.mkdn'}
    _, ext = os.path.splitext(file_path)
    return ext.lower() in markdown_extensions