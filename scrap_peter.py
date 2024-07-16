import requests
from bs4 import BeautifulSoup
import os

from config import (PETER_GALLERY_URL,
                    PETER_GALLERY_DUMP,
                    GALLERY_SITE_BASE_URL)


# URL of website 
url = PETER_GALLERY_URL

# Headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
}


if __name__ == "__main__":
    # Send a GET request to website with headers
    response = requests.get(url, headers=headers)

    # Check if request was successful
    if response.status_code == 200:
        # # Print HTML content for debugging
        # print(response.content)
        
        # Parse HTML content of page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find <div> with specific ID
        div_tag = soup.find('div', {'id': 'sigplus_cda7e173fa71870f8685b498267aba67'})
        
        # Check if <div> tag was found
        if div_tag:
            # Find first <ul> element within this <div>
            ul_tag = div_tag.find('ul')
        
            # Check if <ul> tag was found
            if ul_tag:
                # Existing code to find <a> tags and extract image URLs
                a_tags = ul_tag.find_all('a')
                
                image_urls = []
                for a_tag in a_tags:
                    image_url = a_tag['href']
                    image_urls.append(image_url)
                
                # Print list of image URLs
                for img_url in image_urls:
                    print(img_url)
                
                # Download images
                download_directory = PETER_GALLERY_DUMP
                if not os.path.exists(download_directory):
                    os.makedirs(download_directory)
                
                for img_url in image_urls:
                    # Construct full image URL
                    full_img_url = GALLERY_SITE_BASE_URL + img_url
                    
                    # Send a GET request to download image with headers
                    img_response = requests.get(full_img_url, headers=headers)
                    
                    # Get image file name from URL
                    img_name = img_url.split('/')[-1]
                    
                    # Save image to download directory
                    img_path = os.path.join(download_directory, img_name)
                    with open(img_path, 'wb') as img_file:
                        img_file.write(img_response.content)
                
                print(f"Downloaded {len(image_urls)} images to '{download_directory}' directory.")
            else:
                print("Specified <ul> element was not found.")
        else:
            print("Specified <div> element was not found.")
    else:
        print(f"Failed to retrieve webpage. Status code: {response.status_code}")
