import requests
import json
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

code_file = './src/code-sample.py'
docs_folder = 'docs'
markdown_file_path = os.path.join(docs_folder, f'doc_code-sample.md')

def read_code_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.read()
    else:
        logging.error(f"Code file not found: {file_path}")
        return "File not found"

if not os.path.exists(docs_folder):
    os.makedirs(docs_folder)
    logging.info(f"Folder '{docs_folder}' created.")

logging.info("Processing request...")
url = "http://localhost:11435/api/generate"
data = {
    "model": "llama3",
    "prompt": f"Add title how h1, description and document the following :\n\n```python\n{read_code_file(code_file)}\n```"
}

try:
    response = requests.post(url, json=data)
    response.raise_for_status() 
    
    response_text = response.text
    full_response = ""

    lines = response_text.splitlines()
    for line in lines:
        try:
            line_json = json.loads(line)
            full_response += line_json.get("response", "")
        except json.JSONDecodeError:
            full_response += line

    logging.info("Generating documentation...")

    code_content = read_code_file(code_file)

    markdown_content = f"""
    {full_response.strip()}

    ## Source Code (`{code_file}`)
    
    """
    with open(markdown_file_path, 'w') as markdown_file:
        markdown_file.write(markdown_content)
    
    print(f"Documentation saved to: {markdown_file_path}")

except requests.exceptions.RequestException as e:
    logging.error(f"Request error: {e}")
except Exception as e:
    logging.error(f"Unexpected error: {e}")
