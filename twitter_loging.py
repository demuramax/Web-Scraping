from selenium import webdriver
import time

web = 'https://twitter.com/'
path = '/Users/maxmercury/Downloads/Web Scraping course/chromedriver'
driver = webdriver.Chrome(path)
driver.get(web)
driver.maximize_window()

twitter_email = "Demuramaxim@gmail.com"
twitter_pass = "Maximus22"

login = driver.find_element_by_xpath('//a[@href="/login"]')
time.sleep(7)
login.click()
time.sleep(5)

login_box = driver.find_element_by_xpath('//div[@class="css-1dbjc4n r-ywje51 r-nllxps r-jxj0sb r-16wqof r-1dye5f7"]')
username = login_box.find_element_by_xpath('//input[@autocomplete="username"]')
next_login_button = driver.find_element_by_xpath('//div[contains(@class, "css-901oao r-1awozwy r-jwli3a r-6koalj r-18u37i")]')


username.send_keys(twitter_email)
next_login_button.click()
time.sleep(2)
phone_log = driver.find_element_by_xpath('//input[@class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"]')
phone_log.send_keys('Turtle_breathe')
time.sleep(3)
next_login_button.click()
time.sleep(3)
password = driver.find_element_by_xpath('//input[@name="password"]')
password.send_keys(twitter_pass)
next_login_button.click()


