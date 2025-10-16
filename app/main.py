from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.db.database import engine, Base, get_db
from app.routers import products, auth
from app.core.config import settings

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especifica los dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir los routers
app.include_router(auth.router, prefix=settings.API_PREFIX, tags=["auth"])
app.include_router(products.router, prefix=settings.API_PREFIX, tags=["products"])

@app.get("/")
async def read_root():
    return {
        "message": "Bienvenido a la API de NetSurex Shop",
        "version": settings.APP_VERSION,
        "documentation": "/docs"
    }

@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "version": settings.APP_VERSION}