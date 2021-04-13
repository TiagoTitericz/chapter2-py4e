# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl, re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
count = 0
total = 0
for tag in tags:
    tag = str(tag)
    # Look at the parts of a tag
    count += 1
    number = re.findall('^<s.*>([0-9]+)', tag)
    number = int(number[0])
    total = number + total

print('Count', count)
print('Sum', total)