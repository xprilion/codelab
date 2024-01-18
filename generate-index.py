import os
import re
import json
from markdown import markdown
from datetime import datetime

def parse_md_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    html = markdown(content)
    # Extract the title
    title_match = re.search(r'<h1>(.*?)</h1>', html, re.IGNORECASE)
    title = title_match.group(1) if title_match else 'Unknown Title'

    # Extract other metadata
    metadata = dict(re.findall(r'^(\w+):\s*(.*)\s*$', content, re.MULTILINE))
    return {
        'title': title,
        'slug': metadata.get('id', 'unknown-slug'),
        'publishedAt': metadata.get('publishedAt', datetime.now().isoformat() + 'Z'),  # Fallback to current datetime
        'brief': metadata.get('summary', 'No summary available'),
        'tech': metadata.get('categories', 'unknown'),
        'level': metadata.get('tags', 'unknown')
    }

def create_json(root_dir):
    entries = []

    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename == 'index.md':
                file_path = os.path.join(dirpath, filename)
                entry = parse_md_file(file_path)
                entries.append(entry)

    # Sort entries by publishedAt in descending order
    sorted_entries = sorted(entries, key=lambda x: x['publishedAt'], reverse=True)
    return json.dumps(sorted_entries, indent=4)

def main():
    root_dir = 'md' 
    json_data = create_json(root_dir)

    with open('index.json', 'w') as json_file:
        json_file.write(json_data)

if __name__ == "__main__":
    main()
