import bs4

def find(soup):
    dollar_amount = soup.find('span', {'class':'price-characteristic'}).text
    cent_amount = soup.find('span', {'class':'price-mantissa'}).text

    return dollar_amount+'.'+cent_amount