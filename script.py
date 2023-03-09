import os
import sys
from tqdm import tqdm
import urllib.request

def print_usage():
    print('Usage: python script.py [options] [URL]')
    print('Options:')
    print('  --help  Show this help message and exit')
    print('URL:')
    print('  The URL of the file to download (default: https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned.ckpt)')

# Parse command line arguments
url = 'https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned.ckpt'
for arg in sys.argv[1:]:
    if arg == '--help':
        print_usage()
        sys.exit(0)
    else:
        url = arg

# Extract filename from URL
filename = url.split('/')[-1]

# Create directory
path = './models/Stable-diffusion'
if not os.path.exists(path):
    os.makedirs(path)

# Download file with progress bar
filepath = os.path.join(path, filename)
with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1) as t:
    def reporthook(blocknum, blocksize, totalsize):
        t.total = totalsize
        t.update(blocksize)
    
    urllib.request.urlretrieve(url, filepath, reporthook)

# Create symbolic link
os.symlink(filepath, '{}/model.ckpt'.format(path))