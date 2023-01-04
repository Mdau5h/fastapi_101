from database.query import Query


def create_or_update_note_query(id_: int, title: str, content: str) -> Query:
    bound_params = {
        'id': id_,
        'title': title,
        'content': content,
    }

    query = Query(
        '''
        INSERT INTO notes(id, title, content)
        VALUES(:id, :title, :content)
        ON CONFLICT(id) DO UPDATE SET title=:title, content=:content;
        ''',
        bound_params,
    )

    return query


def get_note_by_id_query(id_: int) -> Query:
    bound_params = {
        'id': id_
    }
    query = Query(
        '''
        SELECT id, title, content, FROM notes WHERE id=:id;
        ''',
        bound_params,
    )

    return query


def get_all_notes_query() -> Query:
    query = Query(
        '''
        SELECT id, title FROM notes;
        '''
    )

    return query


def delete_notes_by_id_query(id_: int) -> Query:
    bound_params = {
        'id': id_
    }
    query = Query(
        '''
        DELETE FROM notes WHERE id=:id;
        ''',
        bound_params,
    )

    return query
