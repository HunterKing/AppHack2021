import bs4

def find(soup):
    dollar_amount = soup.find('span', {'class':'product-grid-cell_main-price product-grid-cell_main-price--on-sale'})
    
    if not dollar_amount:
        dollar_amount = dollar_amount = soup.find('span', {'class':'product-grid-cell_main-price'})

    dollar_amount = dollar_amount.text
    dollar_amount = dollar_amount[2:]

    return dollar_amount