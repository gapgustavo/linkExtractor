import requests
from bs4 import BeautifulSoup
import networkx as nx

def bing_search(query, page_count):
    # Base URL for Bing search
    base_url = 'https://www.bing.com/search'
    # List to store the found links
    links = []

    # Loop through result pages
    for page in range(1, page_count + 1):
        # Parameters for the search, including the query and starting position of results
        params = {'q': query, 'first': str((page - 1) * 10)}
        # Make an HTTP request to Bing with the search parameters
        response = requests.get(base_url, params=params)
        # Create a BeautifulSoup object to parse the HTML content of the response
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all 'li' elements with the class 'b_algo' that contain search results
        search_results = soup.find_all('li', class_='b_algo')
        # Loop to extract links from each search result
        for result in search_results:
            # Find the 'a' element within each result and get the value of the 'href' attribute containing the link
            link = result.find('a')['href']
            # Append the link to the list of found links
            links.append(link)

    # Return the list of links
    return links

def get_relevant_links(urls):
    # Create a directed graph
    G = nx.DiGraph()

    # Add URLs as nodes to the graph
    G.add_nodes_from(urls)

    # Add edges between the URLs
    for i in range(len(urls)):
        for j in range(len(urls)):
            if i != j:
                G.add_edge(urls[i], urls[j])

    # Calculate PageRank
    pagerank = nx.pagerank(G)

    # Sort the URLs based on PageRank
    ranked_urls = sorted(pagerank, key=pagerank.get, reverse=True)

    # Select the top 10 most relevant URLs
    top_10_urls = ranked_urls[:10]
    return top_10_urls