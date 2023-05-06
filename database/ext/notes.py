import typing as t
from sqlalchemy.orm import Session
from app.pydantic_models import NoteModel, NoteRequestModel
from database.raw.notes import (
    create_note_query,
    get_all_notes_query,
    get_note_by_id_query,
    delete_notes_by_id_query,
    update_note_query
)
from database.session import session_factory


def get_note_by_id(session: Session, note_id: int) -> t.Optional[NoteModel]:
    query = get_note_by_id_query(note_id)
    result = session.execute(query).scalars().one()
    if result:
        return NoteModel(
            id=result.id,
            title=result.title,
            content=result.content
        )


def create_note(session: Session, note_data: NoteRequestModel) -> t.Optional[int]:
    query = create_note_query(
        title=note_data.title,
        content=note_data.content
    )
    result = session.execute(query)
    if result:
        return result.scalars().one()


def update_note(session: Session, note_id: int, note_data: NoteRequestModel) -> t.Optional[int]:
    query = update_note_query(
        id_=note_id,
        title=note_data.title,
        content=note_data.content
    )
    result = session.execute(query)
    if result:
        return result.scalars().one()


def get_all_notes(session: Session) -> list[NoteModel]:
    query = get_all_notes_query()
    notes = []
    for note in session.execute(query).scalars().all():
        notes.append(NoteModel(
            id=note.id,
            title=note.title,
            content=note.content
        ))
    return notes


def delete_note_by_id(session: Session, note_id: int) -> t.Optional[int]:
    query = delete_notes_by_id_query(note_id)
    result = session.execute(query).scalars().one()
    if result:
        return result.scalars().one()


if __name__ == '__main__':
    session = session_factory()

    with session.begin():
        note_data = {
            "title": "Updated note in PG",
            "content": "I'm so happy to update my first note in PostgeSQL"
        }
        note_parsed = NoteRequestModel(**note_data)
        # result = create_note(session, note_parsed)
        #
        # result = get_note_by_id(session, 5)

        # result = get_all_notes(session)

        # result = delete_note_by_id(session, 2)

        result = update_note(session, note_id=2, note_data=note_parsed)

        print(result)


