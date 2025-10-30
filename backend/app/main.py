from __future__ import annotations

from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .config import settings
from .database import SessionLocal, init_db
from .models.product import Product
from .routers import cart_router, categories_router, products_router
from .seed_data import seed


def _resolve_under_app(path_str: str) -> Path:
    """Делаем путь относительно каталога с этим файлом, если он относительный."""
    base = Path(__file__).resolve().parent
    p = Path(path_str)
    return p if p.is_absolute() else base / p


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()

    session = SessionLocal()
    try:
        has_products = session.query(Product.id).limit(1).first() is not None
    finally:
        session.close()

    if not has_products:
        seed()

    try:
        yield
    finally:
        pass


app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подготовка статических директорий (создадим, если их нет)
static_dir = _resolve_under_app(settings.static_dir)
images_dir = _resolve_under_app(settings.images_dir)
static_dir.mkdir(parents=True, exist_ok=True)
images_dir.mkdir(parents=True, exist_ok=True)

app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

# Роутеры
app.include_router(products_router)
app.include_router(categories_router)
app.include_router(cart_router)  # <— вместо повторного products_router

@app.get("/")
def root():
    return {
        "message": "Welcome to the API!",
        "docs": "/api/docs",  # лучше с ведущим слэшем
    }

@app.get("/health")
def health():
    return {"status": "ok"}
