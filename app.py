from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")


templates = Jinja2Templates(directory=BASE_DIR / "templates")

context = {}
nomes = {
    "Nome_1": "Ana",
    "Nome_2": "Carlos",
    "Nome_3": "Daniel",
    "Nome_4": "Pedro",
    "Nome_5": "Renato",
    "Nome_6": "Sandro",
}


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="item.html", context={"id": id}
    )

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"context": context},
    )


@app.post("/add")
async def adicionar(request: Request):
    form = await request.form()
    context[f"{len(context)+1}"] = form.get("nome")

    return RedirectResponse(url="/", status_code= 303)