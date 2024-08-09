"""
Exercise 9: Web Scraping
Task:
1.	Use the requests and BeautifulSoup libraries to scrape the titles of the
    latest articles from a news website.
2.	Write a Python program that prints these titles.
"""

import requests
from bs4 import BeautifulSoup


def scrape_latest_article_titles(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all elements containing article titles (specific to BBC News HTML structure)
        article_titles = soup.find_all('h3', class_='gs-c-promo-heading__title gel-paragon-bold nw-o-link-split__text')

        # Extract and return the titles
        titles = [title.text.strip() for title in article_titles]
        return titles
    else:
        # Print an error message if the request was not successful
        print(f"Error: Failed to retrieve content from {url}")
        return None


# URL of BBC News to scrape
url = 'https://www.bbc.com/news'

# Call the function to scrape and print the latest article titles
latest_titles = scrape_latest_article_titles(url)
print("Latest Article:")
if latest_titles:
    print("Latest Article Titles:")
    for title in latest_titles:
        print(title)

