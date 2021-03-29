from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import importlib

vendor_to_url = {
    'ht':'https://www.harristeeter.com/search?query=',
    'walmart':'https://www.walmart.com/search/?query=',
    'amazonfresh':'https://www.amazon.com/s?k=',
    'stopshop':'https://stopandshop.com/product-search/',
    'bj':'https://www.bjs.com/search/',
    'heb':'https://www.heb.com/search/?q='
}

url_addendum = {
    'amazonfresh':'&i=amazonfresh',
    'bj':'/q'
}

class searcher():
    def __init__(self):
        self.current_driver = None

    def get_price(self, vendor, upc):
        html_doc = self.__sel_search(vendor, upc)

        if html_doc == False:
            return 'Price not found'

        soup = BeautifulSoup(html_doc, 'html.parser')

        soup_find = importlib.import_module('queries.%s' % vendor+'.soup_find')

        dollar_amount = soup_find.find(soup)

        if dollar_amount != 'Price not found':
            dollar_amount = '$'+dollar_amount
        return dollar_amount

    def __create_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        # options.add_argument("--disable-extensions")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")

        options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')

        self.current_driver = webdriver.Chrome(executable_path='/root/myproject/py-upc-query/queries/chromedriver', chrome_options=options)

    def __sel_search(self, vendor, upc):
        #print('open for ', vendor)
        #firefox_options = webdriver.FirefoxOptions()
        #firefox_options.set_headless()

        #driver = webdriver.Firefox(executable_path='/root/myproject/py-upc-query/queries/geckodriver', firefox_options = firefox_options)

        if not self.current_driver:
            self.__create_driver()

        driver = self.current_driver

        url = vendor_to_url[vendor] + upc
        if vendor in url_addendum:
            url = url + url_addendum[vendor]
        driver.get(url)

        search_chars = {}

        with open('/root/myproject/py-upc-query/queries/'+vendor+'/search_char.json') as f:
            search_chars = json.load(f)

        found_element = False
        html_doc = None
        
        counter = 0
        while found_element == False:
            counter += 1
            print(vendor, counter)
            if counter == 150:
                print(search_chars['not_found'])
                print(search_chars['found'])
                print(driver.page_source)
                break
            page = driver.page_source
            if search_chars['not_found'] in page:
                found_element = True
                #print('no products')
            elif search_chars['found'] in page:
                found_element = True
                html_doc = driver.page_source
                #print('found')

        #print('close for ', vendor)
        driver.close()

        if html_doc != None:
            return html_doc
        else:
            return False
