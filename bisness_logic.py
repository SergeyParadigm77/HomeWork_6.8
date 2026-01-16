from sqlalchemy.orm import Session
from app import engine
from models import Book, Genre
from info import genres_to_add, books_to_add


def seed_data():
    with Session(engine) as session:
        # Очистка таблиц
        session.query(Genre).delete()
        session.query(Book).delete()

        session.add_all(genres_to_add)
        session.add_all(books_to_add)

        session.commit()
        session.close()


def books_prepared(books):
    with Session(engine) as session:
        genres = {genre.id: genre.name for genre in session.query(Genre).all()}

        books_data = []
        for book in books:
            books_data.append({
                'title': book.title,
                'author': book.author,
                'publication_date': book.publication_date,
                'annotation': book.annotation,
                'genre_name': genres.get(book.genre_id),
                'genre_id': book.genre_id,
                'is_read': 'Да' if book.is_read else 'Нет'
            })
    return books_data


def get_last_15_books():
    with Session(engine) as session:
        books = session.query(Book).order_by(Book.publication_date.desc()).limit(3).all()
        books_data = books_prepared(books)
        return books_data


def books_by_genre(genre_id):
    with Session(engine) as session:
        books = session.query(Book).filter(Book.genre_id == genre_id).order_by(Book.publication_date.desc()).all()
        books_data = books_prepared(books)
        return books_data

#