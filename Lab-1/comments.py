from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

# Set the path to the Chrome web driver
chrome_driver_path = 'C:/Users/Benyas/Downloads/chromedriver-win6/chromedriver-win64/chromedriver'

# Open the website in a Chrome browser
driver = webdriver.Chrome(chrome_driver_path)
driver.get('https://www.reddit.com/r/learnprogramming/top/?t=all')
time.sleep(20)

# Save the entire HTML content
html_content = driver.page_source

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find articles in the parsed HTML using the correct CSS selector
articles = soup.select('#main-content > div:nth-of-type(2) faceplate-batch article')
#create a dataframe 
df=pd.DataFrame(columns=['title', 'link','body','username','date','date_ago'])

for i, article in enumerate(articles, 1):
    # Extract information from the BeautifulSoup object
    title = article.select_one('shreddit-post a:nth-child(3)').get_text(strip=True)
    print(f"\nArticle {i}:")
    print("Title:", title)
    link = article.select_one('shreddit-post a:nth-child(2)').get('href')
    print("Link:", link)
    body = article.select_one('shreddit-post div a:nth-child(1) div:nth-child(1)').get_text(strip=True, separator='\n')
    #print("Body:", body.encode('utf-8', 'ignore').decode('utf-8'))

    #upvotes = article.select_one('shreddit-post div:nth-child(2) span span span').get_text(strip=True)
    #print("Upvotes:", upvotes)
    try:
        username = article.select_one('shreddit-post span:nth-child(1) span:nth-child(1) span div faceplate-hovercard faceplate-tracker a span:nth-child(2)').get_text(strip=True)
        #t3_i9vuhr > span > span.flex.flex-wrap.text-12.gap-2xs.items-center.w-\[calc\(100\%-32px\)\] > span.relative > span > div > faceplate-hovercard
        print("Username:", username)
    except:
        username="NA"
    date_ago = article.select_one('shreddit-post span span:nth-child(1) faceplate-timeago time').get_text(strip=True)
    print("Date Ago:", date_ago)
    Date = article.select_one('shreddit-post span span:nth-child(1) faceplate-timeago time').get('title')
    print("Date:", Date)
    df=df.append({'title':title, 'link':link,'body':body,'username':username,'date':Date,'date_ago':date_ago}, ignore_index=True)

print("hello")
import os
print("Current Working Directory:", os.getcwd())
print(df)
df.to_csv('reddit2.csv', index=False)
