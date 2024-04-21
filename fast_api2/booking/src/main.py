from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from src.auth.routers.base import router as auth_router
from src.book_app.routers.base import router as book_router
from flask import Flask, render_template
from auth.routers.user_router import user_router
from booking.src.auth.routers import base

app = Flask(__name__)

# Настройка пути для шаблонов
app.template_folder = 'templates'

# Настройка пути для статики
app.static_folder = 'static'

# Регистрация роутера
app.register_blueprint(user_router)

users = [
    {"id": 1, "first_name": "John", "last_name": "Doe", "age": 30, "email": "john@example.com"},
    {"id": 2, "first_name": "Jane", "last_name": "Doe", "age": 25, "email": "jane@example.com"},
    # Другие пользователи
]


@app.route('/users')
def users():
    return render_template('users.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)
app = FastAPI()

app.include_router(base.router)
app.include_router(auth_router.router, prefix="/auth")
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(auth_router)
app.include_router(book_router)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/users')
def users():
    users = [
        {"id": 1, "first_name": "John", "last_name": "Doe", "age": 30, "email": "john@example.com"},
        {"id": 2, "first_name": "Jane", "last_name": "Doe", "age": 25, "email": "jane@example.com"},
    ]
    return render_template(render_template(), users=users)


@app.get("/get_template", response_class=HTMLResponse)
def get_html_template(request: Request):
    users = [
        {"username": "Peter", "age": 24},
        {"username": "Max", "age": 21},
        {"username": "Ann", "age": 18},
        {"username": "Volodya", "age": 30},
        {"username": "Elena", "age": 32},
    ]

    return templates.TemplateResponse(
        request=request,
        name="item.html",
        context={
            "data": 2132.2,
            "users": users
        }
    )
