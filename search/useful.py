
import requests
from bs4 import BeautifulSoup
import networkx as nx

def extract_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = []

    for link in soup.find_all('a'):
        href = link.get('href')
        if href != '#':
            links.append(href)
        if len(links) == 5:
            break

    return links


def get_relevant_links(links):
    graph = nx.Graph()
    graph.add_nodes_from(links)

    for link in links:
        extracted_links = extract_links(link)
        for extracted_link in extracted_links:
            graph.add_edge(link, extracted_link)

    page_rank = nx.pagerank(graph)

    relevant_links = sorted(page_rank, key=page_rank.get, reverse=True)[:100]
    return relevant_links


def is_valid_url(url):
    return bool(url.strip()) and ('http://' in url or 'https://' in url)