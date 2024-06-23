# Hitler Crawler

This program finds a path from a given Wikipedia page to the Wikipedia page about Adolf Hitler (`/wiki/Adolf_Hitler`) using a breadth-first search (BFS) algorithm. It supports parallel fetching of Wikipedia links to improve efficiency.

## How to Run

1. **Clone the repository.** 
2. **Install Dependencies:**
```
pip install requests beautifulsoup4
```
3. **Run ther program with `python main.py`**
4. **Enter a starting Wiki URL when promted.**

## Output 

 - If a path to the Hitler Wikipedia page is found, the program will print each step of the path.
 - If the path is not found within 6 hops or if there are errors during execution, it will print "Hitler not found".

## Efficiency 

**Time Complexity:**

**Fetching Wikipedia Links:** Fetching links from a Wikipedia page involves making an HTTP request and parsing HTML. Let's denote the number of links fetched from a page as `L`.

- Time Complexity: O(L)

**BFS Exploration:** BFS explores each link up to a maximum depth of 6 hops (`max_hops`).

 - ***Time Complexity:*** O(V + E), where `V` is the number of vertices (pages) and `E` is the number of edges (links between pages).
 - In the worst case, BFS will explore up to `V` pages and `E` links, but for practical purposes, it's influenced by `max_hops` which limits the exploration.

**Parallelization:** Using a ThreadPoolExecutor with `max_workers` set to 10 allows fetching of multiple pages concurrently.

- ***Time Complexity:*** Effectively reduces the overall time by parallelizing the fetching process. The impact on time complexity depends on network latency, CPU cores, and concurrent HTTP requests.

**Space Complexity**

 - ***Visited Set and Queue***: The space used by the BFS queue and visited set depends on the number of pages (V) and links (E) explored.

***Space Complexity: O(V)***

- ***ThreadPoolExecutor:*** Allocates additional memory for threads and manages concurrent execution.

***Space Complexity:*** O(1) additional space per thread.