# I couldnt get this fully working but this is where I am at... (try it with a mediawiki docker, and a bookstack docker!)

import requests
from bs4 import BeautifulSoup
import bookstack

# Get the MediaWiki page
url_root = "https://example.com/wiki"
url = url_root + "/Main_Page"
response = requests.get(url)

# Parse the page with BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the article titles
article_titles = soup.find_all("a", class_="mw-jump-link")

# Create a list of article titles
article_titles_list = []
for article_title in article_titles:
    article_titles_list.append(article_title.text)

# Import the articles into Bookstack
for article_title in article_titles_list:
    print("Importing article:", article_title)

    # Get the article content
    url = url_root + article_title
    response = requests.get(url)

    # Parse the page with BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Get the article body
    article_body = soup.find("div", class_="mw-content-ltr")

    # Create a Bookstack article
    article = {
        "title": article_title,
        "body": article_body.text,
    }

    # Import the article into Bookstack
    bookstack.import_article(article, api_key="YOUR_API_KEY")

# Create a Bookstack object
bookstack_client = bookstack.Client(url="https://my-bookstack-url.com")

# Connect to Bookstack
bookstack_client.connect()

# Import the articles into Bookstack
for article in article_titles_list:
    print("Importing article:", article)

    # Get the article content
    url = url_root + article
    response = requests.get(url)

    # Parse the page with BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Get the article body
    article_body = soup.find("div", class_="mw-content-ltr")

    # Create a Bookstack article
    article = {
        "title": article_title,
        "body": article_body.text,
    }

    # Import the article into Bookstack
    bookstack_client.import_article(article)

# Disconnect from Bookstack
bookstack_client.disconnect()
