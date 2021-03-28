import queries.search_by_upc as search_by_upc
import queries.upc.query_upc as query_upc
import concurrent.futures
import json

vendors = ['ht', 'walmart', 'amazonfresh', 'stopshop', 'bj', 'heb']

def __price_thread(searcher, vendor, upc):
    to_return = {'price':searcher.get_price(vendor, upc), 'vendor':vendor}
    print('finished '+vendor)
    return to_return

def __get_prices(upc):
    threads = []
    returns = []

    searcher = search_by_upc.searcher()

    with concurrent.futures.ThreadPoolExecutor(max_workers=len(vendors)) as executor:
        for vendor in vendors:
            threads.append(executor.submit(__price_thread, searcher, vendor, upc))
            print('ran '+vendor)
        print('all vendor scans running')
        threads.append(executor.submit(__get_upc_data, upc))

        print('upc running')

    for thread in threads:
        returns.append(thread.result())
    
    print('all threads returned')

    to_return_dict = {}
    for return_val in returns:
        if 'price' in return_val:
            to_return_dict[return_val['vendor']] = return_val['price']
        else:
            to_return_dict['company'] = return_val['company']
            to_return_dict['description'] = return_val['description']
            to_return_dict['image_url'] = return_val['image_url']

    return to_return_dict

def __get_upc_data(upc):
    return query_upc.query(upc)

def get_product_data(upc):

    to_return_dict = __get_prices(upc)

    to_return_json = json.dumps(to_return_dict)

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