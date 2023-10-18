import sys
import contextlib

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen


def make_tiny(url):
    request_url = 'http://tinyurl.com/api-create.php?' + urlencode({'url': url})
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8')


def main():
    if len(sys.argv) < 2:
        print("Kullanım: python script.py [URL1] [URL2] ...")
        return

    for tinyurl in map(make_tiny, sys.argv[1:]):
        print(tinyurl)


if __name__ == '__main__':
    main()