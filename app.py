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
    return render_template("book_list.html", books=books_data)


@app.route('/print_book_by_genre/<int:genre_id>', methods=['GET'])
def print_books_by_genre(genre_id):
    books_data = bisness_logic.books_by_genre(genre_id)
    return render_template("book_list.html", books=books_data)


if __name__ == '__main__':
    bisness_logic.seed_data()
    app.run(port=5000)
