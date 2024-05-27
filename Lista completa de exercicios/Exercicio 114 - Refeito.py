import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.facebook.com')
except:
    print('Deu erro.')
else:
    print('Tudo ok')
    print(site.read())
