from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl, re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
main_count = int(input('Enter count: '))
position = int(input('Enter position: '))

# Retrieve all of the anchor tags
while main_count > 0:
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    href_list = list()
    name_list = list()
    for tag in tags:
        tag = str(tag)
        # Look at the parts of a tag
        x1 = re.findall('href=\S(\S+html)', tag)
        x2 = re.findall('^<a.+>([A-Z][a-z]+)<', tag)
        href_list.append(x1)
        name_list.append(x2)
    print('Retrieving:', href_list[position-1])
    url = href_list[position-1][0]
    main_count -= 1

print(name_list[position-1][0])

 