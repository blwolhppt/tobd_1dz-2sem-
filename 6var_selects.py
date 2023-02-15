import sqlite3

con = sqlite3.connect('db.sqlite')  # создание бд/соединение
cur = con.cursor()

# 1 селект
#cur.execute('''
#    SELECT * FROM students
#    WHERE year_birth > 1990;
#''')


# 2 селект
#cur.execute('''
#    SELECT * FROM attendance
#    WHERE cost BETWEEN 300.0000 AND 4000.0000
#    ORDER BY cost;
#''')


# 3 селект
#cur.execute('''
#    SELECT name_languages, group_of_lang FROM languages
#    WHERE group_of_lang IN ('Славянская', 'Романская');
#''')


# 4 селект
#cur.execute('''
#    SELECT * FROM attendance
#    WHERE start_time LIKE '%12:00%';
#''')


# 5 селект
#cur.execute('''
#    SELECT students.surname, SUM(attendance.cost) FROM attendance
#    JOIN students ON attendance.id_stud_a  = students.id_stud
#    JOIN languages ON attendance.id_lang_a  = languages.id_lang
#    GROUP BY students.surname
#    ORDER BY students.surname DESC;
#''')


# 6 селект
#cur.execute('''
#    SELECT students.surname, languages.name_languages, attendance.cost FROM attendance
#    JOIN students ON attendance.id_stud_a  = students.id_stud
#    JOIN languages ON attendance.id_lang_a  = languages.id_lang
#    GROUP BY students.surname
#    ORDER BY students.surname DESC;
#''')


# 7 селект
#cur.execute('''
#    SELECT students.surname, languages.name_languages  FROM attendance
#    JOIN students ON attendance.id_stud_a  = students.id_stud
#    JOIN languages ON attendance.id_lang_a  = languages.id_lang
#    ORDER BY students.surname;
#''')


# 8 селект
#cur.execute('''
#    SELECT languages.surname_teacher, languages.name_languages, attendance.duration FROM attendance
#    JOIN languages ON attendance.id_lang_a  = languages.id_lang
#    WHERE attendance.duration BETWEEN 2 AND 3
#    ORDER BY languages.surname_teacher;
#''')



for res in cur:
    print(res)

con.commit()
con.close()