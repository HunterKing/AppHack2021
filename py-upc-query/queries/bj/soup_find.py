import bs4

def find(soup):
    dollar_amount = soup.find('span', {'class':'price-display'}).text
    dollar_amount = dollar_amount[2:]

    return dollar_amount