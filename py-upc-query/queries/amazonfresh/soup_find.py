import bs4

def find(soup):
    dollar_amount = soup.find('span', {'class':'a-price-whole'}).text
    cent_amount = soup.find('span', {'class':'a-price-fraction'}).text

    return dollar_amount+cent_amount