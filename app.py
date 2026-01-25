from flask import Flask, render_template
from sqlalchemy import create_engine

from models import Base

import bisness_logic

app = Flask(__name__)

engine = create_engine("sqlite:///database.db", echo=True)
Base.metadata.create_all(engine)


@app.route("/")
def print_all_books():
    books_data = bisness_logic.get_all_books()
    return render_template("all_books_list.html", books=books_data)


@app.route("/print_last_15_books", methods=['GET'])
def print_last_15_books():
    books_data = bisness_logic.get_last_15_books()
    return render_template("last_15_books_list.html", books=books_data)


@app.route('/print_book_by_genre/<int:genre_id>', methods=['GET'])
def print_books_by_genre(genre_id):
    books_data = bisness_logic.books_by_genre(genre_id)
    return render_template("genre_books_list.html", books=books_data)


if __name__ == '__main__':
    bisness_logic.seed_data()
    app.run(port=5000)