from models import Genre, Book

genres_to_add = [Genre(name = "триллер", description = "нагнетает напряжённость через ощущение надвигающейся опасности и неопределённости"),
                 Genre(name = "детектив",description = "сюжет строится вокруг расследования загадочного происшествия, обычно преступления"),
                 Genre(name = "роман", description = "сюжет строится вокруг истории любовных отношений"),
                 Genre(name = "хоррор", description = "предназначен устрашить, напугать или шокировать"),
                 Genre(name = "фантастика", description = "основан на введении в произведение элемента, нарушающего законы реальности"),
    ]

books_to_add = [Book(title='Собака Баскервилей', author="Артур Конан Дойль", annotation="детективная повесть", genre_id=2),
                Book(title='Десять негритят', author="Агата Кристи", annotation="детективная повесть", genre_id=2),
                Book(title='Имя розы', author='Умберто Эко', annotation="", genre_id=2)
                ]



#
