from models import Genre, Book

genres_to_add = [Genre(name = "триллер", description = "нагнетает напряжённость через ощущение надвигающейся опасности и неопределённости"),
                 Genre(name = "детектив",description = "сюжет строится вокруг расследования загадочного происшествия, обычно преступления"),
                 Genre(name = "роман", description = "сюжет строится вокруг истории любовных отношений"),
                 Genre(name = "хоррор", description = "предназначен устрашить, напугать или шокировать"),
                 Genre(name = "фантастика", description = "основан на введении в произведение элемента, нарушающего законы реальности"),
    ]

books_to_add = [Book(title='Собака Баскервилей', author="Артур Конан Дойль", annotation="детективная повесть", genre_id=2, is_read=True),
                Book(title='Десять негритят', author="Агата Кристи", annotation="детективная повесть", genre_id=2),
                Book(title='Имя розы', author='Умберто Эко', annotation="", genre_id=2),
                Book(title='Мисс Марпл', author='Агата Кристи', annotation='детективный роман', genre_id=2),
                Book(title='Молчание ягнят', author='Томас Харрис', annotation='психологический триллер', genre_id=1),
                Book(title='Девушка с татуировкой дракона', author='Стиг Ларссон', annotation='детективный триллер', genre_id=1),
                Book(title='Сияние', author='Стивен Кинг', annotation='психологический триллер', genre_id=1),
                Book(title='Сто лет одиночества', author='Габриэль Гарсия Маркес', annotation='магический роман', genre_id=3),
                Book(title='Гордость и предубеждение', author='Джейн Остин', annotation='классический роман о любви', genre_id=3),
                Book(title='Мастер и Маргарита', author='Михаил Булгаков', annotation='сатирический и мистический роман', genre_id=3, is_read=True),
                Book(title='Война и Мир', author='Лев Толстой', annotation='роман о русской жизни во время наполеоновских войн', genre_id=3),
                Book(title='Унесенные ветром', author='Маргарет Митчелл', annotation='классический роман', genre_id=3),
                Book(title='Дракула', author='Брэм Стокер', annotation='классический вампирский хоррор', genre_id=4),
                Book(title='Франкенштейн, или Современный Прометей', author='Мэри Шелли', annotation='научно-фантастический хоррор', genre_id=4),
                Book(title='Властелин колец', author='Джон Рональд Руэл Толкин', annotation='эпический фэнтезийный роман', genre_id=5),
                Book(title='Изгоняющий дьявола', author='Уильям Питер Блэтти', annotation='история об одержимости', genre_id=4)
                ]
