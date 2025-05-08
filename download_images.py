import os
import requests
from urllib.parse import urlparse

# Create images directory if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# Image URLs (using free-to-use images from Unsplash)
image_urls = {
    'hero-image.jpg': 'https://images.unsplash.com/photo-1540189549336-e6e99c3679fe',
    'jollof-rice.jpg': 'https://images.unsplash.com/photo-1603133872878-684f208fb84b',
    'injera.jpg': 'https://images.unsplash.com/photo-1563245372-f21724e3856d',
    'tagine.jpg': 'https://images.unsplash.com/photo-1563379926898-05f4575a45d8',
    'egusi-soup.jpg': 'https://images.unsplash.com/photo-1547592180-85f173990554',
    'fufu.jpg': 'https://images.unsplash.com/photo-1563379926898-05f4575a45d8',
    'nyama-choma.jpg': 'https://images.unsplash.com/photo-1544025162-d76694265947',
    'ugali.jpg': 'https://images.unsplash.com/photo-1563379926898-05f4575a45d8',
    'couscous.jpg': 'https://images.unsplash.com/photo-1563379926898-05f4575a45d8',
    'shakshuka.jpg': 'https://images.unsplash.com/photo-1563379926898-05f4575a45d8'
}

def download_image(url, filename):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        # Get the file extension from the URL
        parsed_url = urlparse(url)
        file_ext = os.path.splitext(parsed_url.path)[1]
        if not file_ext:
            file_ext = '.jpg'
            
        # Save the image
        filepath = os.path.join('images', filename)
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"Successfully downloaded {filename}")
    except Exception as e:
        print(f"Error downloading {filename}: {str(e)}")

# Download all images
for filename, url in image_urls.items():
    download_image(url, filename) 