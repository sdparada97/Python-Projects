import os
from dotenv import load_dotenv
from os.path import join, dirname

from flask import Flask, render_template, request, session, redirect, url_for

from database import User, Product

dotenv_path = join(dirname(__file__), '.env.example')
load_dotenv(dotenv_path)

# blueprint
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")

# GET = Obtener un recurso
# POST = Crear un recurso


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        print(request.form)  # Dic

        username = request.form.get("username")  # None
        password = request.form.get("password")

        if username and password:
            user = User.create_user(username, password)  # INSERT
            session["user_id"] = user.id  # ID del usuario en la base de datos

            return redirect(url_for("products"))

    return render_template("register.html")


@app.route("/products")
def products():
    user = User.get(session["user_id"])

    # _products = Product.select().where(Product.user == user) # 1
    _products = user.products

    return render_template("products/index.html", products=_products)


@app.route("/products/create", methods=["GET", "POST"])
def products_create():
    if request.method == "POST":
        name = request.form.get("name")
        price = request.form.get("price")

        if name and price:
            # SELECT * FROM users WHERE id = <id>
            user = User.get(session["user_id"])

            # INSERT INTO products(name, price, user_id) VALUES (name, price, user_id)
            Product.create(name=name, price=price, user=user)
            return redirect(url_for("products"))

    return render_template("products/create.html")


@app.route("/products/update/<id>", methods=["GET", "POST"])
def products_update(id:int):
    _product = Product.select().where(Product.id == id).first()

    if request.method == "POST":
        _product.name = request.form.get("name")
        _product.price = request.form.get("price")
        _product.save()  # UPDATE products SET name="" 

        return redirect(url_for("products"))

    return render_template("products/update.html", product=_product)


if __name__ == "__main__":
    app.run(debug=True, load_dotenv=True)