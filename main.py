from flask import *


app = Flask(__name__)
# app.secret_key= "Ropi"
# login_manager=LoginManager(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register",methods=['POST','GET'])
def register():
    return render_template("register.html")
@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/blog")
def blog():
    return render_template("blog.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/shop-grid")
def shopgrid():
    return render_template("shop-grid.html")
@app.route("/shop-details")
def shopdetails():
    return render_template("shop-details.html")
@app.route("/shoping-cart")
def shopingcart():
    return render_template("shoping-cart.html")
@app.route("/checkout")
def checkout():
    return render_template("checkout.html")
@app.route("/blog-details")
def blogdetails():
    return render_template("blog-details.html")

if __name__ == '__main__':
    app.run()