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

def get_last_15_books():
    with Session(engine) as session:
        books = session.query(Book).order_by(Book.publication_date.desc()).limit(3).all()
        genres = {genre.id: genre.name for genre in session.query(Genre).all()}

        books_prepared = []
        for book in books:
            books_prepared.append({
                'title': book.title,
                'author': book.author,
                'publication date': book.publication_date,
                'annotation': book.annotation,
                'genre_id': genres.get(book.genre_id),
                'is_read': 'Да' if book.is_read else 'Нет'
            })
        return books_prepared