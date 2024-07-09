import requests
from bs4 import BeautifulSoup
import csv

from config import (IRREGULAR_VERB_LIST_URL)

# URL of webpage containing table
url = IRREGULAR_VERB_LIST_URL


# Function to scrape table and save it to a CSV file
def scrape_table_to_csv(url, csv_filename):
    # Fetch webpage content
    response = requests.get(url)
    
    # Check if request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find table element by ID
        table = soup.find('table', {'id': 'irregular-verbs-list'}) 
        
        if table:
            # Open a CSV file for writing
            with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                
                # Find all rows in table
                rows = table.find_all('tr')
                
                for row in rows:
                    # Extract all cells in each row
                    cells = row.find_all(['th', 'td'])
                    
                    # Check if it's a valid row (skip if header row or other non-data row)
                    if cells:
                        # Extract text from each cell and write to CSV
                        row_data = [cell.get_text(strip=True) for cell in cells]
                        writer.writerow(row_data)
                        
            print(f"Table scraped successfully and saved to {csv_filename}")
        else:
            print("Table with specified ID not found on webpage.")
    else:
        print(f"Failed to fetch webpage. Status code: {response.status_code}")


# Call function to scrape and save table
scrape_table_to_csv(url, 'irregular_verbs.csv')
