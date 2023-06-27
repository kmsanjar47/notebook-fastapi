
def NoteSchema(item) -> dict:
    return {
        "id": str(item["_id"]),
        "title": item["title"],
        "description": item["description"],
        "date": item["date"]

    }


def Notes(items: dict) -> list:
    return [NoteSchema(item) for item in items]
