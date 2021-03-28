from flask import Flask
import main
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def get_product_data():
    return 'test