from datetime import datetime
from sqlalchemy import String, ForeignKey, func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
     pass

class Genre(Base):
    __tablename__ = 'genres'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    description: Mapped[str] = mapped_column(String(100))
    books = relationship('Book', back_populates='genre', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Genre(id={self.id}, name={self.name}, description={self.description}>"


class Book(Base):
    __tablename__ = 'books'
    id: Mapped[int] = mapped_column(primary_key=True)
    publication_date: Mapped[datetime] = mapped_column(default=func.now())
    title: Mapped[str] = mapped_column(String(50))
    author: Mapped[str] = mapped_column(String(30))
    annotation: Mapped[str] = mapped_column(String(100), nullable=True)
    is_read: Mapped[bool] = mapped_column(default=False)
    genre_id: Mapped[int] = mapped_column(ForeignKey('genres.id'))
    genre = relationship('Genre', back_populates='books')

    def __repr__(self):
        return f"<Book(id={self.id}, publication date={self.publication_date}, title={self.title}, author={self.author}, annotation={self.annotation}, genre id={self.genre_id}"

