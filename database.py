import sqlite3
from sqlite3.dbapi2 import connect
connection = sqlite3.connect("data.db")

def create_table_student():
    connection.execute(
        "CREATE TABLE IF NOT EXISTS entries (first_name TEXT, middle_name TEXT, last_name TEXT)")
    connection.commit()

def create_table_subject():
    connection.execute(
        "CREATE TABLE IF NOT EXISTS entries (subject_code TEXT, subject_name TEXT)")
    connection.commit()

def create_table_teacher():
    connection.execute(
        "CREATE TABLE IF NOT EXISTS entries (given_name TEXT, name_last TEXT)")
    connection.commit()

def close_database():
    connection.close()

def add_student(first_name, middle_name, last_name):
    connection.execute(
        f"INSERT INTO entries VALUES('{first_name}','{middle_name}', '{last_name}');")
    connection.commit()

def add_subject(subject_code, subject_name):
    connection.executes(
        f"INSERT INTO entries VALUES('{subject_code}','{subject_name}');")
    connection.commit()

def add_teacher(given_name, name_last):
    connection.executes(
        f"INSERT INTO entries VALUES('{given_name}','{name_last}');")
    connection.commit()

def get_students():
    return connection.execute("SELECT * FROM entries;")

def get_subjects():
    return connection.execute("SELECT * FROM entries;")

def get_teachers():
    return connection.execute("SELECT * FROM entries;")

def delete_entry(student,subject,teacher):
    connection.execute('DELETE FROM entries where last_name = ? OR subject = ? OR teacher = ?' , (student, subject, teacher))
    connection.commit()