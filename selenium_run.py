from asyncio.base_subprocess import WriteSubprocessPipeProto
from selenium import webdriver

website = 'https://www.adamchoi.co.uk/overs/detailed'
path = '/Users/maxmercury/Downloads/Web Scraping course/chromedriver'
driver = webdriver.Chrome(path)
driver.get(website)

driver.quit()