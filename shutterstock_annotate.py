from bs4 import BeautifulSoup
import requests
import os
from PIL import Image, ImageFilter, ImageDraw, ImageFont


def download_file(url, local_filename=None):
    # from: https://stackoverflow.com/questions/16694907/how-to-download-large-file-in-python-with-requests-py

    if local_filename is None:
        local_filename = url.split('/')[-1]

    if os.path.exists(local_filename):
        return local_filename

    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    return local_filename


def write_text(imgfilename, text):
    im = Image.open(imgfilename)
    canvas = ImageDraw.Draw(im)
    canvas.rectangle([0, 125, im.size[0], 170], fill=(0, 0, 0))
    fnt = ImageFont.truetype('/Library/Fonts/Brush Script.ttf', 20)
    canvas.text((10, 125), text, font=fnt, fill=(255, 255, 255))
    im.save(imgfilename + '.modified.jpg')

def get_shutterstock_images(q):
    url = 'https://www.shutterstock.com/search'
    params = {'searchterm': q}
    html = requests.get(url, params=params).text
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.select('.img-wrap img')

    for image in images:
        img_url = 'https:' + image.get('src')
        title = image.get('alt')
        print title
        filename = download_file(img_url)
        write_text(filename, title)


def get_images(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.select('img')
    for image in images:
        img_url = image.get('src')
        try:
            download_file(img_url)
        except:
            continue

# get_images('https://www.bing.com/images/search?q=babies+crying&FORM=HDRSC2')
# get_images('baby crying')

get_shutterstock_images('baby crying')

