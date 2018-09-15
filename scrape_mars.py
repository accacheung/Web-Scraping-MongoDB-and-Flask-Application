# Dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import requests
import pymongo
import pandas as pd


# Initialize browser
def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


# Function to scrape all scraping code
def scrape():

    # Initialize browser
    browser = init_browser()

    #Dictionary to store all scraping data
    scraped_data = {}


    # URL of page to be scraped (NASA Mars News)
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)

    # Scrape page into soup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # Collect the latest News Title and Paragraph Text
    result = soup.find("div", class_="list_text")
    news_title = result.find("div", class_="content_title").text
    news_p = result.find("div", class_="article_teaser_body").text

    # Store in dictionary
    scraped_data["news_title"] = news_title
    scraped_data["news_p"] = news_p


    # URL of page to be scraped (JPL Mars Space Images - Featured Image)
    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2)

    # Scrape page into soup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # Featured Image
    featured_image_url = soup.find("img", class_="thumb")["src"]

    # Store in dictionary
    scraped_data["featured_image_url"] = featured_image_url



    # URL of page to be scraped (Mars Weather)
    url3 = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url3)

    # Scrape page into soup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # Latest Mars weather tweet
    mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text

    # Store in dictionary
    scraped_data["mars_weather"] = mars_weather


    # URL of page to be scraped (Mars Facts¶)
    url4 = 'https://space-facts.com/mars/'
    browser.visit(url4)

    # Using 'read_html' function in Pandas to automatically scrape any tabular data from a page
    tables = pd.read_html(url4)

    # Forming DataFrame
    df = tables[0]
    df.columns = ['Facts', 'Values']

    # Using 'to_html' to generate HTML tables from DataFrames
    html_table = df.to_html()

    # Clean up
    html_table = html_table.replace('\n', '')

    # Store in dictionary
    scraped_data["html_table"] = html_table


    # Mars Hemispheres
    hemisphere_image_urls = []

    # URL of page to be scraped for cerberus
    url5_1 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(url5_1)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Featured Image
    image_url_1 = soup.find("img", class_="wide-image")["src"]
    title_1 = soup.find("h2",class_="title").text

    cerberus = {"title": title_1, "image_url": "https://astrogeology.usgs.gov/"+image_url_1}
    hemisphere_image_urls.append(cerberus)

    # URL of page to be scraped for schiaparelli
    url5_2 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(url5_2)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Featured Image
    image_url_2 = soup.find("img", class_="wide-image")["src"]
    title_2 = soup.find("h2",class_="title").text

    schiaparelli = {"title": title_2, "image_url": "https://astrogeology.usgs.gov/"+image_url_2}
    hemisphere_image_urls.append(schiaparelli)

    # URL of page to be scraped for syrtis_major
    url5_3 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(url5_3)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Featured Image
    image_url_3 = soup.find("img", class_="wide-image")["src"]
    title_3 = soup.find("h2",class_="title").text

    syrtis_major = {"title": title_3, "image_url": "https://astrogeology.usgs.gov/"+image_url_3}
    hemisphere_image_urls.append(syrtis_major)

    # URL of page to be scraped for valles_marineris
    url5_4 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(url5_4)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Featured Image
    image_url_4 = soup.find("img", class_="wide-image")["src"]
    title_4 = soup.find("h2",class_="title").text

    valles_marineris = {"title": title_4, "image_url": "https://astrogeology.usgs.gov/"+image_url_4}
    hemisphere_image_urls.append(valles_marineris)


    scraped_data["hemisphere_image_urls"] = hemisphere_image_urls


    # Return results
    return scraped_data
