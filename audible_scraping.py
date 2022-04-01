from matplotlib import container
import pandas
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

# options = Options()
# options.headless = True
# options.add_argument('window-size=1920x1080')

web = 'https://www.audible.com/adblbestsellers?ref=a_search_t1_navTop_pl0cg1c0r0&pf_rd_p=adc4b13b-d074-4e1c-ac46-9f54aa53072b&pf_rd_r=SD8KB6YRST0H8RWQPQ77'
path = '/Users/maxmercury/Downloads/Web Scraping course/chromedriver'
driver = webdriver.Chrome(path, options=options)
driver.get(web)
driver.maximize_window()

# pagination:
pagination = driver.find_element_by_xpath('//ul[contains(@class, "pagingElements")]')
pages = pagination.find_elements_by_tag_name('li')
last_page = int(pages[-2].text)

current_page = 1
book_title = []
book_author = []
book_length = []
    
while current_page <= last_page:
    time.sleep(2)
    container = driver.find_element_by_class_name('adbl-impression-container ')
    products = container.find_elements_by_xpath('./li')

    for product in products: 
        book_title.append(product.find_element_by_xpath('.//h3[contains(@class, "bc-heading")]').text)
        book_author.append(product.find_element_by_xpath('.//li[contains(@class, "authorLabel")]').text)
        book_length.append(product.find_element_by_xpath('.//li[contains(@class, "runtimeLabel")]').text)
        
    current_page += 1
    try:
        next_page = driver.find_element_by_xpath('//span[contains(@class, "nextButton")]')
        next_page.click()
    except:
        pass
    
driver.quit()

df_books = pd.DataFrame({'title': book_title, 'author': book_author, 'length': book_length})
df_books.to_csv('books.csv', index=False)
