**Asynchronous Web Crawler**

**1. Objective**

To develop a simple asynchronous web crawler using asyncio and aiohttp with retry support and compare it with a sequential web crawler.

**2. Input**

The program accepts:

List of website URLs

Number of retry attempts

**3. Output**

The program displays:

URLs fetched by the sequential crawler

URLs fetched by the asynchronous crawler

Sequential execution time

Asynchronous execution time

Retry attempts for failed requests

**4. Algorithm**

Start.

Create a list of website URLs.

Implement a sequential crawler to fetch URLs one by one.

Implement an asynchronous crawler using asyncio and aiohttp.

Fetch multiple URLs concurrently.

Retry a request if it fails.

Measure the execution time of both crawlers.

Compare the sequential and asynchronous execution times.

Display the results.

Stop.

**5. Time and Space Complexity**

**Time Complexity**

Sequential = O(n)

Asynchronous = Approximately O(1) for concurrent requests, depending on network and server response time.

Where n is the number of URLs.

**Space Complexity**

O(n)

The URLs and fetched results are stored in memory.
