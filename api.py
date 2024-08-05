from flask import Flask,jsonify
import flask

app = Flask(__name__)

@app.route('/get-products')
def get_products():
    # Product entities= id,name, description, price and imageUrl
    # Sample data
    products = [
        {
            'id': 1,
            'name': 'Product 1',
            'description': 'This is product 1',
            'price': 10.99,
            'imageUrl': 'https://example.com/product1.jpg'
        },
        {
            'id': 2,
            'name': 'Product 2',
            'description': 'This is product 2',
            'price': 15.99,
            'imageUrl': 'https://example.com/product2.jpg'
        }
    ]
    return jsonify(products)
if '__main__' == __name__:
    app.run(debug=True)