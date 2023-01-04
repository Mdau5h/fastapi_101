import typing as t
from database.session import session


from database.models import Note
from database.raw.notes import create_or_update_note_query, get_all_notes_query, get_note_by_id_query, \
    delete_notes_by_id_query


def get_note_by_id(user_id: int) -> t.Optional[Note]:
    q = get_note_by_id_query(user_id)
    with session() as s:
        r = s.execute(q).fetchone()
        if r:
            return Note(*r)


def save_note(**kwargs) -> None:
    q = create_or_update_note_query(**kwargs)
    with session() as s:
        s.execute(q).fetchone()


def get_all_notes() -> list[Note]:
    q = get_all_notes_query()
    notes = []
    with session() as s:
        for note in s.execute(q):
            notes.append(Note(*note))
        return notes


def delete_note_by_id(user_id: int) -> t.Optional[Note]:
    q = delete_notes_by_id_query(user_id)
    with session() as s:
        r = s.execute(q).fetchone()
        if r:
            return Note(*r)
