from splinter import Browser
import time
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup
import pandas as pd

mars_data={}

def scrape():
    
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = "https://redplanetscience.com/"
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    news_title=soup.find("div", class_="content_title").get_text()
    news_p=soup.find("div", class_="article_teaser_body").get_text()
    browser.quit()

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    image_url="https://spaceimages-mars.com/"
    browser.visit(image_url)
    time.sleep(1)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    image=soup.find("div", class_="floating_text_area")
    image_url_1=image.find("a")["href"]
    featured_image_url=[image_url+image_url_1]
    browser.quit()

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    table_url="https://galaxyfacts-mars.com/"
    browser.visit(table_url)
    time.sleep(1)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    table_from_html=soup.find("table", class_="table table-striped")
    table_mars = pd.read_html('https://galaxyfacts-mars.com/')
    df = table_mars[0]
    mars_table = df.rename(columns={0: 'Mars-Earth Comparison', 1:'Mars', 2: 'Earth'})
    mars_table.set_index('Mars-Earth Comparison')
    mars_table_updated=mars_table.to_html(classes='table table-stripped')
    #mars_table_updated = mars_table.replace('\n', '')
    browser.quit()

    mars_data["news_title"]=news_title
    mars_data["excerpt"]=news_p
    mars_data["image_url"]=featured_image_url
    mars_data["mars_table"]=mars_table_updated

    return mars_data
    #astrology_url
#print("___________________")
#print(scrape())