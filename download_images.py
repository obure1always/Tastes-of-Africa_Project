import os
import requests
from PIL import Image
from io import BytesIO

# Create images directory if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# Image URLs and their corresponding filenames
images = {
    'jollof-rice.jpg': 'https://images.unsplash.com/photo-1603133872878-684f208fb84b',
    'injera.jpg': 'https://images.unsplash.com/photo-1563245372-f21724e3856d',
    'tagine.jpg': 'https://images.unsplash.com/photo-1565557623262-b51c2513a641',
    'west-africa.jpg': 'https://images.unsplash.com/photo-1547592180-85f173990554',
    'east-africa.jpg': 'https://images.unsplash.com/photo-1544145945-f90425340c7e',
    'north-africa.jpg': 'https://images.unsplash.com/photo-1516026672322-bc52d61a55d5',
    'south-africa.jpg': 'https://images.unsplash.com/photo-1520250497591-112f2f40a3f4'
}

def download_image(url, filename):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Open the image and resize it to a reasonable size
            img = Image.open(BytesIO(response.content))
            img = img.resize((800, 600), Image.Resampling.LANCZOS)
            
            # Save the image
            img.save(os.path.join('images', filename), 'JPEG', quality=85)
            print(f'Successfully downloaded {filename}')
        else:
            print(f'Failed to download {filename}: HTTP {response.status_code}')
    except Exception as e:
        print(f'Error downloading {filename}: {str(e)}')

def main():
    print('Starting image downloads...')
    for filename, url in images.items():
        download_image(url, filename)
    print('All downloads completed!')

if __name__ == '__main__':
    main() 