from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import importlib

from selenium_firefox.firefox import Firefox as ffdriver

vendor_to_url = {
    'ht':'https://www.harristeeter.com/search?query=',
    'walmart':'https://www.walmart.com/search/?query=',
    'amazon-fresh':'https://www.amazon.com/s?k=',
    'stop-shop':'https://stopandshop.com/product-search/',
    'bj':'https://www.bjs.com/search/',
    'heb':'https://www.heb.com/search/?q='
}

url_addendum = {
    'amazon-fresh':'&i=amazonfresh',
    'bj':'/q'
}

def get_price(vendor, upc):
    html_doc = __sel_search(vendor, upc)

    if html_doc == False:
        return 'Price not found'

    soup = BeautifulSoup(html_doc, 'html.parser')

    soup_find = importlib.import_module('queries.%s' % vendor+'.soup_find')

    dollar_amount = soup_find.find(soup)

    return float(dollar_amount)



def __sel_search(vendor, upc):
    #print('open for ', vendor)
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.set_headless()

    #driver = ffdriver(executable_path='queries/geckodriver', firefox_options = firefox_options)
    driver = ffdriver()
    url = vendor_to_url[vendor] + upc
    if vendor in url_addendum:
        url = url + url_addendum[vendor]
    driver.get(url)

    search_chars = {}

    with open('queries/'+vendor+'/search_char.json') as f:
        search_chars = json.load(f)

    found_element = False
    html_doc = None
    
    while found_element == False:
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
