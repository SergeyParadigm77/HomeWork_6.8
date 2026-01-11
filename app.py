from flask import Flask, jsonify, render_template
from sqlalchemy import create_engine

from models import Base

import bisness_logic

app = Flask(__name__)

engine = create_engine("sqlite:///database.db", echo=True)
Base.metadata.create_all(engine)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/print_last_15_books", methods=['GET'])
def print_last_15_books():
    books_data = bisness_logic.get_last_15_books()
    return render_template("last_15_books.html", books = books_data)



if __name__ == '__main__':
    bisness_logic.seed_data()
    app.run(port=5000)



