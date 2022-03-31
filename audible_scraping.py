from matplotlib import container
import pandas
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

options = Options()
options.headless = True
options.add_argument('window-size=1920x1080')

web = 'https://www.audible.com/search'
path = '/Users/maxmercury/Downloads/Web Scraping course/chromedriver'
driver = webdriver.Chrome(path, options=options)
driver.get(web)
driver.maximize_window()

container = driver.find_element_by_class_name('adbl-impression-container ')
products = container.find_elements_by_xpath('./li')

book_title = []
book_author = []
book_length = []

for product in products: 
    book_title.append(product.find_element_by_xpath('.//h3[contains(@class, "bc-heading")]').text)
    book_author.append(product.find_element_by_xpath('.//li[contains(@class, "authorLabel")]').text)
    book_length.append(product.find_element_by_xpath('.//li[contains(@class, "runtimeLabel")]').text)

driver.quit()

df_books = pd.DataFrame({'title': book_title, 'author': book_author, 'length': book_length})
df_books.to_csv('books.csv', index=False)
