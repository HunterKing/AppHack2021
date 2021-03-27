import bs4

def find(soup):
    dollar_amount = soup.find('div', {'class':'offer_tag'}).text
    dollar_amount = dollar_amount[1:]

    return dollar_amount