from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

web = 'https://twitter.com/search?q=python&src=typed_query'
path = '/Users/maxmercury/Downloads/Web Scraping course/chromedriver'
driver = webdriver.Chrome(path)
driver.get(web)
driver.maximize_window()

def get_tweet(element):
    try:
        user = element.find_element_by_xpath('.//span[contains(text(), "@")]').text
        text = element.find_element_by_xpath('.//div[@lang="en"]').text 
        tweets_data = [user, text]  
    except:
        tweets_data = ['user', 'text']  
    return tweets_data

user_data = []
text_data = []
tweets = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//article[@role="article"]')))

for tweet in tweets:
    tweet_list = get_tweet(tweet)
    user_data.append(tweet_list[0])
    text_data.append(" ".join(tweet_list[1].split()))
    
driver.quit()
df_tweets = pd.DataFrame({'user': user_data, 'text': text_data})
df_tweets.to_csv('tweets.csv', index=False)