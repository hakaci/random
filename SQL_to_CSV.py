import os
import re
import pandas as pd

from config import (DATABASE_1_TXT)

# Path to SQL file
sql_file_path = DATABASE_1_TXT

# Output directory for CSV files
output_dir = 'resources/SQL_content_CSVs'
os.makedirs(output_dir, exist_ok=True)

# Regex patterns to match INSERT INTO statements and extract data
insert_into_pattern = re.compile(r"INSERT INTO `(\w+)` \((.*?)\) VALUES\s*(.*?);", re.DOTALL)


# Function to process and extract data from INSERT INTO statements
def extract_data_from_sql(sql_content):
    insert_statements = insert_into_pattern.findall(sql_content)
    
    table_data = {}
    
    for table_name, columns, values_block in insert_statements:
        columns = [col.strip().strip('`') for col in columns.split(',')]
        
        # Split values block into individual value sets
        values_block = values_block.replace('),', ')\n').replace('(', '').replace(')', '')
        values = values_block.split('\n')
        values = [val.replace('\'', '').split(',') for val in values if val.strip()]
        
        if table_name not in table_data:
            table_data[table_name] = {
                'columns': columns,
                'rows': []
            }
        
        for value_set in values:
            row = [val.strip() for val in value_set]
            table_data[table_name]['rows'].append(row)
    
    return table_data


# Function to write data to CSV files using pandas
def write_data_to_csv(table_data):
    for table_name, data in table_data.items():
        df = pd.DataFrame(data['rows'], columns=data['columns'])
        csv_file_path = os.path.join(output_dir, f"{table_name}.csv")
        df.to_csv(csv_file_path, index=False)


def main():
    # Read SQL file content
    with open(sql_file_path, 'r', encoding='utf-8') as sql_file:
        sql_content = sql_file.read()

    # Extract data from SQL content
    table_data = extract_data_from_sql(sql_content)

    # Write extracted data to CSV files
    write_data_to_csv(table_data)

    print("Data has been successfully extracted and written to CSV files.")


if __name__ == '__main__':
    main()
