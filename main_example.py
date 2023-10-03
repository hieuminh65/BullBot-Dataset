import requests
import pickle
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from collections import deque

base_urls = [
    "https://usf.campusdish.com",
]

visited_links = set()
queue = deque()
def get_links_from_url(url):
    links = []
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        for link in soup.find_all('a', href=True):
            href = link['href']
            # Check if the href is a full URL (either http or https) 
            if href.startswith(("https://")) and 'usf.edu' in href:
                full_url = href
            # If not, try to identify the correct base URL
            else:
                for base in base_urls:
                    if href.startswith(base):
                        full_url = urljoin(base, href)
                        break
                else:
                    # Default to current page's base URL if not matched with known base URLs
                    full_url = urljoin(url, href)
            
            if full_url and full_url not in visited_links and full_url.startswith(("https://")):
                links.append(full_url)
                visited_links.add(full_url)
    except Exception as e:
        print(f"Error fetching {url}: {e}")

    return links

    

def deep_scrape(start_urls):
    all_links = []
    
    for url in start_urls:
        # Add the starting URL to the queue
        queue.append(url)
        visited_links.add(url)
    
    while queue:
        current_url = queue.popleft()
        links = get_links_from_url(current_url)
        all_links.extend(links)
        
        # Add unvisited links to the queue
        for link in links:
            if link not in visited_links:
                queue.append(link)
                visited_links.add(link)
                
    return all_links

if __name__ == "__main__":
    urls1 = deep_scrape(base_urls)
    print(urls1)
    print("The number of links found is: ", len(urls1))
    # urls2 = deep_scrape(urls1)
    # print("The number of links found is: ", len(urls2))

