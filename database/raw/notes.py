from database.db_models import Note
from sqlalchemy import insert, select, update, delete


def create_note_query(title: str, content: str):
    query = insert(Note).values(
        title=title,
        content=content
    ).returning(Note.id)
    return query


def update_note_query(id_: int, title: str, content: str):
    query = update(Note).where(Note.id == id_).values(
        title=title,
        content=content
    ).returning(Note.id)
    return query


def get_note_by_id_query(id_: int):
    query = select(Note).where(Note.id == id_)
    return query


def get_all_notes_query():
    query = select(Note)
    return query


def delete_notes_by_id_query(id_: int):
    query = update(Note).where(Note.id == id_).values(
        deleted=True
    ).returning(Note.id)
    return query
