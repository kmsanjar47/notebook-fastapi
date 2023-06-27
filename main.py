from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
from models.note import Note
from schemas.note import NoteSchema

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

conn = MongoClient("mongodb+srv://kmsanjar47:scdJrfjO2UmtVTJI@cluster0.ttg5k7y.mongodb.net/")


@app.get("/")
async def root(request: Request, response_class="HTML_response"):
    docs = conn.notebook.notes.find()
    doc = [doc for doc in docs]
    print(doc)
    return templates.TemplateResponse("index.html", {"request": request, "items": doc})


@app.post("/")
async def send_data(request: Request):
    form = await request.form()
    temp_note = Note(title= dict(form)["title"],description=dict(form)["description"])
    inserted_note = conn.notebook.notes.insert_one(dict(temp_note))
    return {"success":True}
