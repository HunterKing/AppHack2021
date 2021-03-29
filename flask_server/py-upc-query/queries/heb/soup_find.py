import bs4

def find(soup):
    dollar_amount = soup.find('span', {'class':'cat-price-number'}).text
    while dollar_amount[0] != '$':
        dollar_amount = dollar_amount[1:]
    dollar_amount = dollar_amount[1:5]
    return dollar_amount