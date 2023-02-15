import sqlite3

con = sqlite3.connect('db.sqlite')  # создание бд/соединение
cur = con.cursor()

cur.executescript('''
    CREATE TABLE IF NOT EXISTS languages(
        id_lang INTEGER PRIVATE KEY,
        name_languages TEXT,
        group_of_lang TEXT,
        surname_teacher TEXT 
    );


    CREATE TABLE IF NOT EXISTS students(
        id_stud INTEGER PRIVATE KEY,
        surname TEXT,
        year_birth INTEGER,
        telephone INTEGER
    );


    CREATE TABLE IF NOT EXISTS attendance(
        id_stud_a INTEGER,
        id_lang_a INTEGER,
        start_time TEXT,
        duration INTEGER,
        cost FLOAT,
        FOREIGN KEY(id_stud_a) REFERENCES students(id_stud),
        FOREIGN KEY(id_lang_a) REFERENCES languages(id_lang)  
    );


    INSERT INTO languages(id_lang, name_languages, group_of_lang, surname_teacher)
    VALUES (1, 'Английский', 'Западногерманская', 'Рюмин');

    INSERT INTO languages(id_lang, name_languages, group_of_lang, surname_teacher)
    VALUES (2, 'Польский', 'Славянская', 'Муравьев');

    INSERT INTO languages(id_lang, name_languages, group_of_lang, surname_teacher)
    VALUES (3, 'Испанский', 'Романская', 'Балабанов');

    INSERT INTO languages(id_lang, name_languages, group_of_lang, surname_teacher)
    VALUES (4, 'Русский', 'Славянская', 'Гасперт');

    INSERT INTO languages(id_lang, name_languages, group_of_lang, surname_teacher)
    VALUES (5, 'Итальянский', 'Романская', 'Муравьев');

    INSERT INTO languages(id_lang, name_languages, group_of_lang, surname_teacher)
    VALUES (6, 'Французский', 'Романская', 'Моле');

    INSERT INTO languages(id_lang, name_languages, group_of_lang, surname_teacher)
    VALUES (7, 'Немецкий', 'Западногерманская', 'Исаев');

    INSERT INTO languages(id_lang, name_languages, group_of_lang, surname_teacher)
    VALUES (8, 'Латинский', 'Италийская', 'Бродский');

    INSERT INTO languages(id_lang, name_languages, group_of_lang, surname_teacher)
    VALUES (9, 'Шведский', 'Скандинавская', 'Бергман');

    INSERT INTO languages(id_lang, name_languages, group_of_lang, surname_teacher)
    VALUES (10, 'Чешский', 'Славянская', 'Чудов');



    INSERT INTO students(id_stud, surname, year_birth, telephone)
    VALUES (1, 'Иванов', 1980, 112211);

    INSERT INTO students(id_stud, surname, year_birth, telephone)
    VALUES (2, 'Гришин', 1975, 554637);

    INSERT INTO students(id_stud, surname, year_birth, telephone)
    VALUES (3, 'Морозов', 1985, NULL);

    INSERT INTO students(id_stud, surname, year_birth, telephone)
    VALUES (4, 'Троцкий', 1992, 346712);

    INSERT INTO students(id_stud, surname, year_birth, telephone)
    VALUES (5, 'Медведев', 1983, 543321);

    INSERT INTO students(id_stud, surname, year_birth, telephone)
    VALUES (6, 'Гусев', 1988, 543622);

    INSERT INTO students(id_stud, surname, year_birth, telephone)
    VALUES (7, 'Кудрин', 1993, 234214);

    INSERT INTO students(id_stud, surname, year_birth, telephone)
    VALUES (8, 'Разин', 1979, 554325);

    INSERT INTO students(id_stud, surname, year_birth, telephone)
    VALUES (9, 'Пугачев', 1990, 367162);

    INSERT INTO students(id_stud, surname, year_birth, telephone)
    VALUES (10, 'Болотников', 1987, 123435);



    INSERT INTO attendance(id_stud_a, id_lang_a, start_time, duration, cost)
    VALUES (1, 7, '2020-02-25 15:00:00.00', 2, 200.0000);

    INSERT INTO attendance(id_stud_a, id_lang_a, start_time, duration, cost)
    VALUES (1, 7, '2020-04-02 12:00:00.00', 1, 100.0000);

    INSERT INTO attendance(id_stud_a, id_lang_a, start_time, duration, cost)
    VALUES (2, 2, '2020-02-05 11:00:00.00', 2, 300.0000);

    INSERT INTO attendance(id_stud_a, id_lang_a, start_time, duration, cost)
    VALUES (2, 2, '2020-05-12 09:00:00.00', 3, 450.0000);

    INSERT INTO attendance(id_stud_a, id_lang_a, start_time, duration, cost)
    VALUES (5, 6, '2020-05-01 10:00:00.00', 2, 450.0000);

    INSERT INTO attendance(id_stud_a, id_lang_a, start_time, duration, cost)
    VALUES (4, 9, '2020-02-05 14:00:00.00', 5, 5000.0000);

    INSERT INTO attendance(id_stud_a, id_lang_a, start_time, duration, cost)
    VALUES (4, 9, '2020-05-30 12:00:00.00', 5, 5000.0000);

    INSERT INTO attendance(id_stud_a, id_lang_a, start_time, duration, cost)
    VALUES (5, 8, '2020-04-05 14:00:00.00', 4, 4000.0000);

    INSERT INTO attendance(id_stud_a, id_lang_a, start_time, duration, cost)
    VALUES (5, 8, '2020-05-06 09:00:00.00', 2, 2000.0000);

    INSERT INTO attendance(id_stud_a, id_lang_a, start_time, duration, cost)
    VALUES (6, 10, '2020-01-28 20:00:00.00', 2, NULL);

    INSERT INTO attendance(id_stud_a, id_lang_a, start_time, duration, cost)
    VALUES (7, 4, '2020-02-20 15:00:00.00', 3, 250.0000);

    INSERT INTO attendance(id_stud_a, id_lang_a, start_time, duration, cost)
    VALUES (7, 3, '2020-05-10 13:00:00.00', 4, 2250.0000);

    INSERT INTO attendance(id_stud_a, id_lang_a, start_time, duration, cost)
    VALUES (7, 7, '2020-05-14 15:00:00.00', 3, 500.0000);

    INSERT INTO attendance(id_stud_a, id_lang_a, start_time, duration, cost)
    VALUES (7, 4, '2020-10-20 12:00:00.00', 2, NULL);

    INSERT INTO attendance(id_stud_a, id_lang_a, start_time, duration, cost)
    VALUES (8, 4, '2020-02-02 17:00:00.00', 1, 100.0000);

    INSERT INTO attendance(id_stud_a, id_lang_a, start_time, duration, cost)
    VALUES (8, 4, '2020-08-05 14:00:00.00', 3, 2000.0000);

    INSERT INTO attendance(id_stud_a, id_lang_a, start_time, duration, cost)
    VALUES (9, 5, '2020-08-22 14:00:00.00', 1, 300.0000);

    INSERT INTO attendance(id_stud_a, id_lang_a, start_time, duration, cost)
    VALUES (10, 4, '2020-02-01 11:00:00.00', 2, 500.0000);

    INSERT INTO attendance(id_stud_a, id_lang_a, start_time, duration, cost)
    VALUES (10, 5, '2020-02-01 15:00:00.00', 4, 2000.0000);

    INSERT INTO attendance(id_stud_a, id_lang_a, start_time, duration, cost)
    VALUES (10, 3, '2020-07-03 18:00:00.00', 3, 2000.0000);

''')

cur.execute("SELECT * FROM students;")
print(cur.fetchall())

cur.execute("SELECT * FROM languages;")
print(cur.fetchall())

cur.execute("SELECT * FROM attendance;")
print(cur.fetchall())

con.commit()
con.close()
