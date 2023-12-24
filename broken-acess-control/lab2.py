import requests
import urllib3
import requests
import sys
import re

urllib3.disable_warnings(urllib3)

proxies = {
    'http': 'http://127.0.0.1:8080',
    'https':'http://127.0.0.1:8080',
}

def admin_panel(url):
    admin_panel = url

def main():
    print('Lab2 script')
    if len(sys.argv) != 2:
        print("Usage:%s<url>")
        print("Example: www.example.com")
        sys.exit(-1)
    url = sys.argv[0]
    admin_found = admin_panel(url)

if __name__ == '__main__':
    main()