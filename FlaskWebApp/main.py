from flask import Flask, render_template

# create an object of class Flask
app = Flask('Demo Web Application')


# @app.get('/')
def home():
    return '''
    <html>
        <head>
            <title>Welcome to Flask</title>
            <link href="https://bootswatch.com/5/yeti/bootstrap.min.css" rel="stylesheet">
        </head>
        <body>
        
        <div class="alert alert-primary">
            <div class="container">
                <h1>Hello, and welcome to Flask project</h1>
            </div>
        </div>
        <div class="container">
            <p>This is the homepage!</p>
        </div>
        </body>
    </html>
    '''


data = {'title': 'Product Manager Dashboard', 'subtitle': 'Developed by Vinod, powered by Flask.'}
products = [
    dict(id=1, name='Logitech optical mouse', category='computer accessories', price=899.0),
    dict(id=2, name='Apple magic mouse', category='computer accessories', price=8499.0),
    dict(id=3, name='Apple airpods', category='mobile accessories', price=12000.0),
    dict(id=4, name='Samsung 21" LCD monitor', category='computer accessories', price=6450.0)
]


@app.route('/')
def index():
    return render_template('index.html', data=data)


@app.route('/product-list')
def product_list():
    data['products'] = products
    return render_template('product_list.html', data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234, debug=True)
