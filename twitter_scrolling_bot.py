from selenium import webdriver

web = 'https://twitter.com/search?q=python&src=typed_query'
path = '/Users/maxmercury/Downloads/Web Scraping course/chromedriver'
driver = webdriver.Chrome(path)
driver.get(web)
driver.maximize_window()

