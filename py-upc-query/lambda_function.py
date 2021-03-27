import main

def lambda_handler(event, context):
    upc = event['upc']
    return main.get_product_data(upc)