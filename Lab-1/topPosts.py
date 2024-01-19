from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

# Set the path to the Chrome web driver
chrome_driver_path = 'C:/Users/Benyas/Downloads/chromedriver-win6/chromedriver-win64/chromedriver'

# Open the website in a Chrome browser
driver = webdriver.Chrome(chrome_driver_path)

#read csv
df=pd.read_csv('reddit2.csv')
ino=0
dg=pd.DataFrame(columns=['title','body','username','date','date_ago','comment_1','comment_2','comment_3','comment_4','comment_5','comment_6','comment_7','comment_8','comment_9','comment_10'])
#select row by row

for index, row in df.iterrows():
    try:
        ino=ino+1
        title=row['title']
        body=row['body']
        username=row['username']
        date=row['date']
        date_ago=row['date_ago']


        link=row['link']
        link="https://www.reddit.com"+link
        print(link)
        driver.get(link)
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(1)
        # Save the entire HTML content
        html_content = driver.page_source

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find articles in the parsed HTML using the correct CSS selector
        comments = soup.select('#comment-tree shreddit-comment')
        print(len(comments))
        com=[]
        op=0
        for i in comments:
            op=op+1
            comment = i.select_one(' div:nth-child(3)').get_text(strip=True, separator='\n')
            print("Comment: ",comment)
            com.append(comment)
            
        c2=com[1]
        c3=com[2]
        c4=com[3]
        c5=com[4]
        c6=com[5]
        c7=com[6]
        c8=com[7]
        c9=com[8]
        c10=com[9]
        dg=dg.append({'title':title,'body':body,'username':username,'date':date,'date_ago':date_ago,'comment_1':com[0],'comment_2':c2,'comment_3':c3,'comment_4':c4,'comment_5':c5,'comment_6':c6,'comment_7':c7,'comment_8':c8,'comment_9':c9,'comment_10':c10}, ignore_index=True)
        dg.to_csv('reddit4.csv', index=False)
    except:
        hu=0
    if ino>=100:
        break
print(dg)
dg.to_csv('reddit4.csv', index=False)