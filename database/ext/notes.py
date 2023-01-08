import typing as t
from database.session import session


from database.models import Note
from database.raw.notes import create_note_query, get_all_notes_query, get_note_by_id_query, \
    delete_notes_by_id_query, update_note_query


def get_note_by_id(note_id: int) -> t.Optional[Note]:
    q = get_note_by_id_query(note_id)
    with session() as s:
        r = s.execute(q).fetchone()
        if r:
            return Note(
                id=r[0],
                title=r[1],
                content=r[2]
            )


def create_note(**kwargs) -> t.Optional[Note]:
    q = create_note_query(**kwargs)
    with session() as s:
        r = s.execute(q).fetchone()
        if r:
            return Note(
                id=r[0],
                title=r[1],
                content=r[2]
            )

def update_note(**kwargs) -> t.Optional[Note]:
    q = update_note_query(**kwargs)
    with session() as s:
        r = s.execute(q).fetchone()
        if r:
            return Note(
                id=r[0],
                title=r[1],
                content=r[2]
            )

def get_all_notes() -> list[Note]:
    q = get_all_notes_query()
    notes = []
    with session() as s:
        for note in s.execute(q):
            notes.append(Note(
                id=note[0],
                title=note[1],
                content=note[2]
            ))
        return notes


def delete_note_by_id(note_id: int) -> int:
    q = delete_notes_by_id_query(note_id)
    with session() as s:
        r = s.execute(q).fetchone()
        if r:
            return r[0]
