import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl = input('Enter location: ')

print('Retrieving', serviceurl)
uh = urllib.request.urlopen(serviceurl, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

js = json.loads(data)

count = 0
total = 0

for item in js['comments']:
    count += 1
    total = total + item['count']
  
print('Count:', count)
print('Sum:', total)