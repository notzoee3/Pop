import requests

def fetch_proxyscrape():
    url = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=3000&country=all'
    r = requests.get(url)
    return r.text.strip().splitlines()

def fetch_free_proxy_cz():
    url = 'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt'
    r = requests.get(url)
    return r.text.strip().splitlines()

def fetch_spys_one():
    url = 'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt'
    r = requests.get(url)
    return r.text.strip().splitlines()

def save_proxy(proxy_list):
    with open("proxy_list.txt", "w") as f:
        for proxy in proxy_list:
            f.write(f"{proxy}\n")
    print(f"[+] {len(proxy_list)} proxies saved to proxy_list.txt")

if __name__ == "__main__":
    proxies = []
    proxies += fetch_proxyscrape()
    proxies += fetch_free_proxy_cz()
    proxies += fetch_spys_one()
    proxies = list(set(proxies))
    save_proxy(proxies)
