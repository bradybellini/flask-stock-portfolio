from flask import (
    Flask,
    escape,
    render_template,
    request,
    session,
    redirect,
    url_for
) 

app = Flask(__name__)

app.secret_key = 'BAD_SECRET_KEY'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html', company_name='TestDriven.io')

@app.route('/stocks/')
def stocks():
    return render_template('stocks.html')

@app.route('/hello/<message>')
def hello_message(message):
    return f'<h1>Welcome {escape(message)}!</h1>'

@app.route('/blog_posts/<int:post_id>')
def display_blog_post(post_id):
    return f'<h1>Blog Post #{post_id}...</h1>'

@app.route('/add_stock', methods=['GET', 'POST'])
def add_stock():
    if request.method == 'POST':
        for key, value in request.form.items():
            print(f'{key}: {value}')
        
        session['stock_symbol'] = request.form['stock_symbol']
        session['number_of_shares'] = request.form['number_of_shares']
        session['purchase_price'] = request.form['purchase_price']
        return redirect(url_for('stocks'))

    return render_template('add_stock.html')