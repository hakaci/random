import pandas as pd
import json

from config import (YOUTUBE_DOWNLOAD_LIST)

def csv_to_jsonl_pandas(csv_file_path, jsonl_file_path, chunksize=10000):
    chunks = pd.read_csv(csv_file_path, chunksize=chunksize)
    with open(jsonl_file_path, 'w', encoding='utf-8') as jsonl_file:
        for chunk in chunks:
            for row in chunk.to_dict(orient='records'):
                jsonl_file.write(json.dumps(row) + '\n')

           
# Enter inputs
csv_to_jsonl_pandas(YOUTUBE_DOWNLOAD_LIST, r'Resources\output_file1.jsonl')
