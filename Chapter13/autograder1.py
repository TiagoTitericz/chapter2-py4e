import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    serviceurl = input('Enter location: ')
    if len(serviceurl) < 1: 
        break

    print('Retrieving', serviceurl)
    uh = urllib.request.urlopen(serviceurl, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    tree = ET.fromstring(data)

    counts = tree.findall('.//count')
    print('Count:', len(counts))
    total = 0
    for item in counts:
        item = int(item.text)
        total = total + item
    print('Sum:', total)

