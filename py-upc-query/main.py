import queries.search_by_upc as search_by_upc
import queries.upc.query_upc as query_upc
import concurrent.futures
import json

vendors = ['ht', 'walmart', 'amazonfresh', 'stopshop', 'bj', 'heb']

def __price_thread(vendor, upc):
    return {'price-float':search_by_upc.get_price(vendor, upc), 'vendor':vendor}

# in: upc = string
# out: json string {string vendor = float price}
def __get_prices(upc):
    threads = []
    returns = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=len(vendors)) as executor:
        for vendor in vendors:
            threads.append(executor.submit(__price_thread, vendor, upc))
    for thread in threads:
        returns.append(thread.result())
    
    to_return_dict = {}
    for return_val in returns:
        to_return_dict[return_val['vendor']] = return_val['price-float']
    
    #to_return_json = json.dumps(to_return_dict)

    return to_return_dict

#in: upc = string
#out: json string = {
#   'class': String,        #class of barcode
#   'code': String,         #UPC code
#   'company': String,      #manufacturer
#   'description': String   #item name, 
#   'image_url': String     #url of generic image for item, 
#   'size': String          #unknown - size of item?, 
#   'status': String        #unknown - is the code currently used?
# }
def __get_upc_data(upc):
    return query_upc.query(upc)

def get_product_data(upc):

    product_data = __get_prices(upc)
    upc_data = __get_upc_data(upc)

    to_return_dict = {
        'amazonfresh':product_data['amazonfresh'],
        'bj':product_data['bj'],
        'company': upc_data['company'],
        'description': upc_data['description'],
        'heb': product_data['heb'],
        'ht': product_data['ht'],
        'image_url': upc_data['image_url'],
        'stopshop': product_data['stopshop'],
        'walmart': product_data['walmart']
    }

    to_return_json = json.dumps(to_return_dict)
    print(to_return_json)

    return to_return_json

# sample_upc = {
#     'cape_cod':'020685000294',
#     'coke':'049000050103',
#     'lays_sconion':'028400310444',
#     'veggie_broth':'051000198792',
#     'sabra_rrp_hum':'040822017503',
#     'aw_rootbeer':'078000053463',
#     'baba_hum':'17215927611',
#     'liquid_death':'860000023924',
#     'kind_bars':'602652186196',
#     'big_reeses':'034000666621',
#     'pasta':'072036725608'
# }