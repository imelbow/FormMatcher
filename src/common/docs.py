import yaml
from pathlib import Path

def load_api_docs():
    docs_path = Path(__file__).parent.parent / 'api_docs.yaml'
    with open(docs_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


api_docs = load_api_docs()
