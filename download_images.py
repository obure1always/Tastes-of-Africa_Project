import os
import requests
from pathlib import Path

# Create images directory if it doesn't exist
images_dir = Path("images")
images_dir.mkdir(exist_ok=True)

# Image URLs and their local filenames
images = {
    "jollof-rice.jpg": "https://images.unsplash.com/photo-1603133872878-684f208fb84b",
    "injera.jpg": "https://images.unsplash.com/photo-1563245372-f21724e3856d",
    "tagine.jpg": "https://images.unsplash.com/photo-1563245372-f21724e3856d",
    "west-africa.jpg": "https://images.unsplash.com/photo-1563245372-f21724e3856d",
    "east-africa.jpg": "https://images.unsplash.com/photo-1563245372-f21724e3856d",
    "north-africa.jpg": "https://images.unsplash.com/photo-1563245372-f21724e3856d",
    "south-africa.jpg": "https://images.unsplash.com/photo-1563245372-f21724e3856d",
    "team.jpg": "https://images.unsplash.com/photo-1563245372-f21724e3856d"
}

def download_image(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        filepath = images_dir / filename
        with open(filepath, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {filename}")
    except Exception as e:
        print(f"Error downloading {filename}: {e}")

def main():
    for filename, url in images.items():
        download_image(url, filename)

if __name__ == "__main__":
    main() 