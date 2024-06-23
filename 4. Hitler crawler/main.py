import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor
from collections import deque

max_hops = 6 # Maximum number of hops allowed
max_workers = 10  # Maximum number of workers

def fetch_wikipedia_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=True)
    wikipedia_links = []
    for link in links:
        href = link['href']
        if href.startswith('/wiki/') and ':' not in href:
            wikipedia_links.append(urljoin(url, href))
    return wikipedia_links

# Finds the path from start_url to the Hitler Wikipedia page using BFS
def find_hitler_path(start_url):
    queue = deque([(start_url, [start_url])])  
    visited = set([start_url])  # Set to keep visited URLs
    
    def fetch_and_process(url):
        try:
            links = fetch_wikipedia_links(url)
            return links
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return []

    with ThreadPoolExecutor(max_workers) as executor:
        while queue:
            url, path = queue.popleft()  
            try:
                links = executor.submit(fetch_and_process, url).result()  
                for link in links:
                    if link not in visited:
                        if link.endswith('/wiki/Adolf_Hitler'):
                            return path + [link]  # Return path if found
                        elif len(path) < max_hops:
                            visited.add(link)  # Mark as visited
                            queue.append((link, path + [link])) 
            except Exception as e:
                print(f"Error processing {url}: {e}")

if __name__ == "__main__":
    start_url = input("Enter Wiki-page URL: ").strip()
    path = find_hitler_path(start_url)
    if path:
        print("The path to the HITLER is:")
        for step, url in enumerate(path):
            print(f"{step + 1}. {url}")
