from flask import Flask
import main
import json
app = Flask(__name__)

@app.route('/q/<upc>', methods=['GET', 'POST'])
def get_product_data(upc):
    return main.get_product_data(upc)


@app.route('/', methods=['GET', 'POST'])
def check_running():
    return 'running'