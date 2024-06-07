<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for
from database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'secret-key'
db.init_app(app)

# Import models after initializing db
with app.app_context():
    from models import ContentOffering, Cart, Transaction
    db.create_all()

@app.route('/')
def home():
    content_offerings = ContentOffering.query.all()
    return render_template('home.html', content_offerings=content_offerings)

@app.route('/add', methods=['GET', 'POST'])
def add_content():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        price = request.form['price']
        
        new_content = ContentOffering(title=title, description=description, price=price)
        db.session.add(new_content)
        db.session.commit()
        
        return redirect(url_for('home'))
    return render_template('add_content.html')

@app.route('/cart', methods=['POST'])
def add_to_cart():
    content_id = request.form['content_id']
    cart_item = Cart(content_id=content_id)
    db.session.add(cart_item)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/checkout')
def checkout():
    cart_items = Cart.query.all()
    total_price = sum(item.content.price for item in cart_items)
    return render_template('checkout.html', cart_items=cart_items, total_price=total_price)

@app.route('/complete_checkout', methods=['POST'])
def complete_checkout():
    cart_items = Cart.query.all()
    total_price = sum(item.content.price for item in cart_items)
    
    transaction = Transaction(total_price=total_price)
    db.session.add(transaction)
    db.session.commit()
    
    Cart.query.delete()
    db.session.commit()
    
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
=======
from flask import Flask, render_template, request, redirect, url_for
from database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'secret-key'
db.init_app(app)

# Import models after initializing db
with app.app_context():
    from models import ContentOffering, Cart, Transaction
    db.create_all()

@app.route('/')
def home():
    content_offerings = ContentOffering.query.all()
    return render_template('home.html', content_offerings=content_offerings)

@app.route('/add', methods=['GET', 'POST'])
def add_content():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        price = request.form['price']
        
        new_content = ContentOffering(title=title, description=description, price=price)
        db.session.add(new_content)
        db.session.commit()
        
        return redirect(url_for('home'))
    return render_template('add_content.html')

@app.route('/cart', methods=['POST'])
def add_to_cart():
    content_id = request.form['content_id']
    cart_item = Cart(content_id=content_id)
    db.session.add(cart_item)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/checkout')
def checkout():
    cart_items = Cart.query.all()
    total_price = sum(item.content.price for item in cart_items)
    return render_template('checkout.html', cart_items=cart_items, total_price=total_price)

@app.route('/complete_checkout', methods=['POST'])
def complete_checkout():
    cart_items = Cart.query.all()
    total_price = sum(item.content.price for item in cart_items)
    
    transaction = Transaction(total_price=total_price)
    db.session.add(transaction)
    db.session.commit()
    
    Cart.query.delete()
    db.session.commit()
    
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> 89900e3c157d554cd02bbe13312b712e97820d9b
