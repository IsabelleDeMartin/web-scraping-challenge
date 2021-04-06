from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


# ## title paragraph

def scrape_img():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)
    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url)
    button_click = browser.find_by_tag("button")[1]
    button_click.click()
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    featured_image_url = soup.find('img', class_='fancybox-image').get('src')
    image_url = f"https://spaceimages-mars.com/{featured_image_url}"
    browser.quit()
    return image_url


def scrape_facts():
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)
    df = tables[0]
    return df.to_html(classes="table table-striped")


def scrape_hemi():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    browser.quit()
    return


def scrape_all():
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(2)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    news = soup.select_one('div.list_text')
    news_title = news.find('div', class_='content_title').get_text()
    news_p = news.find('div', class_='article_teaser_body').get_text()
    data_dict = {
        "news_title": news_title,
        "news_p": news_p,
        "f_img": scrape_img(),
        "facts": scrape_facts()
    }
    browser.quit()
    return data_dict


# ## featured image
if __name__ == "__main__":
    print(scrape_all())
