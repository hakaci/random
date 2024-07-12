import os
import re
import csv

from config import (DATABASE_1_TXT)

# Regex pattern to match INSERT INTO statements
insert_pattern = re.compile(r"INSERT INTO `(\w+)` \((.*?)\) VALUES\s*\((.*?)\);", re.DOTALL)

# Function to parse and process SQL insert statements
def parse_sql_inserts(sql_file):
    output_folder = "Resources/wp_content_csv"
    os.makedirs(output_folder, exist_ok=True)  # Create output folder if it doesn't exist
    
    with open(sql_file, 'r', encoding='utf-8') as file:
        sql_content = file.read()

    insert_matches = insert_pattern.findall(sql_content)
    
    for match in insert_matches:
        table_name = match[0]
        columns = match[1].split(', ')
        values = match[2].split('), (')
        
        # Clean up values and format for CSV
        cleaned_values = []
        for value_set in values:
            cleaned_value_set = value_set.strip().replace("'", "").replace("(", "").replace(")", "")
            cleaned_values.append(cleaned_value_set)
        
        # # CSV filename based on table name
        # csv_filename = os.path.join(output_folder, f"{table_name}.csv")
        
        # # Write to CSV file
        # with open(csv_filename, 'a', newline='', encoding='utf-8') as csv_file:
        #     csv_writer = csv.writer(csv_file)
            
        #     # Write header if file is new
        #     if os.path.getsize(csv_filename) == 0:  # Check if file is empty
        #         csv_writer.writerow(columns)
            
        #     # Write values
        #     for cleaned_value_set in cleaned_values:
        #         csv_writer.writerow(cleaned_value_set.split(','))
        
        # print(f"Processed {len(cleaned_values)} rows into {csv_filename}")


if __name__ == "__main__":
    parse_sql_inserts(DATABASE_1_TXT)
