from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter
from config.db import conn
from models.note import Note

note = APIRouter()


templates = Jinja2Templates(directory="templates")


@note.get("/")
async def root(request: Request, response_class="HTML_response"):
    docs = conn.notebook.notes.find()
    doc = [doc for doc in docs]
    print(doc)
    return templates.TemplateResponse("index.html", {"request": request, "items": doc})


@note.post("/")
async def send_data(request: Request):
    form = await request.form()
    temp_note = Note(title=dict(form)["title"], description=dict(form)["description"])
    inserted_note = conn.notebook.notes.insert_one(dict(temp_note))
    return {"success": True}
