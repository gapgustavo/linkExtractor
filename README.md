# Project Name: Django Bing Search

A Django-based website that resembles Google search functionality. Given a user-provided link, the application searches Bing and retrieves the top 10 most relevant URLs from the first 40 pages of results.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API](#api)
- [Examples](#examples)

## Introduction
The Django Bing Search project is a web application that allows users to perform searches similar to Google. It utilizes the Bing search engine to retrieve the top 10 relevant URLs from the first 40 pages of search results. The application provides three main views: home, history, and search_done.

- The home page is accessible at http://127.0.0.1:8000/search/home/ and contains a search field where users can enter a link.
- The history page, available at http://127.0.0.1:8000/search/history/, displays the search history. Users can select a filter option to view specific searches and use buttons to delete or access individual search records.
- The search_done page, found at http://127.0.0.1:8000/search/search_done/, shows the results of the most recent search performed.

## Features

- Perform searches by entering a link.
- Retrieve the top 10 most relevant URLs from the first 40 pages of Bing search results.
- View search history and filter records based on specific criteria.
- Delete individual search records.
- Access the results of the most recent search.

## Installation
1. Clone the repository:
```bash
git clone https://github.com/gapgustavo/linkExtractor.git
```

2. Navigate to the project directory:
```bash
cd linkExtractor
```

3. Create a virtual environment:
```bash
python3 -m venv venv
```

4. Activate the virtual environment:
- For Windows:
```bash
venv\Scripts\activate.bat
```

- For macOS and Linux:
```bash
source venv/bin/activate
```

5. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage
1. Start the Django development server:
```bash
python manage.py runserver
```
2. Access the application in your web browser at http://127.0.0.1:8000/search/home/.

## API
### Docs:
- http://localhost:8000/searchapi/docs


The application provides an API endpoint that accepts both POST and GET requests.

- POST Request: http://localhost:8000/searchapi/

    - Parameters:
        - link: The link you want to search for.

    - Response format:
        ```json
        {
        "result": ["https://m.facebook.com/", "https://m.facebook.com/login.php", "https://pt-pt.facebook.com/login", "https://pt-pt.facebook.com/", "https://m.facebook.com/login.php?login_attempt=1&display=popup", "https://www.facebook.com/.facebook.com/", "https://m.facebook.com/facebook/", "https://m.facebook.com/r.php", "https://mbasic.facebook.com/", "https://m.facebook.com/help/"]
        }
        ```

- GET Request: http://localhost:8000/searchapi/
    - Response format:
        ```json
        {
        "id": 7,
        "link": "https://facebook.com/",
        "date": "2023-07-11",
        "links_list": ["links_list_example"]
        }
        ```
## Examples

1. Python request example for POST:
```python
import requests
import json

url = 'http://localhost:8000/searchapi/'
data = {
    'link': 'facebook.com'
}
response = requests.post(url, data=data).json()
print(response)
```

2. Python request example for GET:
```python
import requests
import json

url = 'http://localhost:8000/searchapi/'
response = requests.get(url).json()
print(response)
```