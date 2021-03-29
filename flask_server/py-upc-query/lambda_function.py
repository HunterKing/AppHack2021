import main
import sys

def run(upc):
    mystring = main.get_product_data(upc)
    print(mystring)
    return mystring

run(sys.argv[1])