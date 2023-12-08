import sqlite3
from typing import List
import datetime
from model import Note

connection = sqlite3.connect("notes.db")
cursor = connection.cursor()


def create_table():
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS notes (
            title text,
            content text,
            position integer
            )"""
    )


create_table()


def insert_note(note: Note):
    cursor.execute("select count(*) FROM notes")
    count = cursor.fetchone()[0]
    note.position = count if count else 0
    with connection:
        cursor.execute(
            "INSERT INTO notes VALUES (:title, :content, :position)",
            {"title": note.title, "content": note.content, "position": note.position},
        )


def get_all_notes() -> List[Note]:
    cursor.execute("select * from notes")
    results = cursor.fetchall()
    return [Note(*result) for result in results]


def delete_note(position):
    cursor.execute("select count(*) from notes")
    count = cursor.fetchone()[0]

    with connection:
        cursor.execute("DELETE from notes WHERE position=:position", {"position": position})
        for pos in range(position + 1, count):
            change_position(pos, pos - 1, False)


def change_position(old_position: int, new_position: int, commit=True):
    cursor.execute(
        "UPDATE notes SET position = :position_new WHERE position = :position_old",
        {"position_old": old_position, "position_new": new_position},
    )
    if commit:
        connection.commit()


def update_note(position: int, title: str, content: str):
    with connection:
        if title is not None and content is not None:
            cursor.execute(
                "UPDATE notes SET title = :title, content = :content WHERE position = :position",
                {"position": position, "title": title, "content": content},
            )
        elif title is not None:
            cursor.execute(
                "UPDATE notes SET title = :title WHERE position = :position",
                {"position": position, "title": title},
            )
        elif content is not None:
            cursor.execute(
                "UPDATE notes SET content = :content WHERE position = :position",
                {"position": position, "content": content},
            )

