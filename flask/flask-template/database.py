import os
from dotenv import load_dotenv
from os.path import join, dirname

from peewee import PostgresqlDatabase, Model, TextField, DateTimeField, IntegerField, ForeignKeyField, CharField

import datetime

dotenv_path = join(dirname(__file__), '.env.example')
load_dotenv(dotenv_path)

db = PostgresqlDatabase(
        os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT"),
        host=os.getenv("DB_HOST")
    )


class User(Model):  # Tables
    username = CharField()
    password = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
        db_table = "users"

    @classmethod
    def create_user(cls, _username, _password):
        _password = "cody_" + _password
        return User.create(username=_username, password=_password)


# Migrations
class Product(Model):  # Tables
    name = TextField()
    price = IntegerField()
    user = ForeignKeyField(User, backref="products")
    created_at = DateTimeField(default=datetime.datetime.now)

    @property
    def price_format(self):
        return f"$ {self.price} dollars"

    class Meta:
        database = db
        db_table = "products"


db.create_tables([User, Product])