import queries.search_by_upc as search_by_upc
import queries.upc.query_upc as query_upc
import concurrent.futures
import json

vendors = ['ht', 'walmart', 'amazon-fresh', 'stop-shop', 'bj', 'heb']

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
    
    to_return_json = json.dumps(to_return_dict)

    return to_return_json

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
    return json.dumps(query_upc.query(upc))

def get_product_data(upc):
    return __get_prices(upc) + '|' + __get_upc_data(upc)

sample_upc = {
    'cape_cod':'020685000294',
    'coke':'049000050103',
    'lays_sconion':'028400310444',
    'veggie_broth':'051000198792',
    'sabra_rrp_hum':'040822017503',
    'aw_rootbeer':'078000053463',
    'baba_hum':'17215927611',
    'liquid_death':'860000023924',
    'kind_bars':'602652186196',
    'big_reeses':'034000666621',
    'pasta':'072036725608'
}

print(get_product_data(sample_upc['pasta']))