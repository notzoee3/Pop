from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from concurrent.futures import ThreadPoolExecutor
import time, random, datetime

# Load video list
with open("video_list.txt") as f:
    urls = f.read().splitlines()

# Load proxy list
with open("proxy_list.txt") as f:
    proxies = f.read().splitlines()

def log_view(info):
    with open("view_log.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - {info}\n")

def start_view(url):
    ua = UserAgent()
    user_agent = ua.random

    chrome_options = Options()
    chrome_options.add_argument(f'user-agent={user_agent}')
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920,1080")

    proxy = random.choice(proxies)
    chrome_options.add_argument(f'--proxy-server=http://{proxy}')

    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get(url)
        print(f"[+] View {url} via {proxy}")
        log_view(f"SUCCESS - {url} via {proxy}")

        for _ in range(random.randint(3, 7)):
            driver.execute_script(f"window.scrollBy(0, {random.randint(100, 500)});")
            time.sleep(random.uniform(1, 3))

        time.sleep(random.randint(35, 65))

    except Exception as e:
        print(f"[!] Error: {e}")
        log_view(f"ERROR - {url} via {proxy} - {e}")
    finally:
        driver.quit()

def worker():
    while True:
        url = random.choice(urls)
        start_view(url)
        time.sleep(random.randint(5, 15))

if __name__ == "__main__":
    thread_count = 10
    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        for _ in range(thread_count):
            executor.submit(worker)
