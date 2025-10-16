from sqlalchemy.orm import Session
from app.db.database import SessionLocal, engine, Base
from app.models import models
from app.services.auth_service import get_password_hash

# Crear las tablas
Base.metadata.create_all(bind=engine)

def init_db():
    db = SessionLocal()
    try:
        # Verificar si el usuario admin ya existe
        admin = db.query(models.User).filter(models.User.email == "netsurex.sistem@gmail.com").first()
        if not admin:
            # Crear el usuario admin
            admin_user = models.User(
                email="netsurex.sistem@gmail.com",
                hashed_password=get_password_hash("Netsurex4"),
                is_active=True,
                is_admin=True
            )
            db.add(admin_user)
            db.commit()
            print("Usuario administrador creado exitosamente")
        else:
            print("El usuario administrador ya existe")
    finally:
        db.close()

if __name__ == "__main__":
    print("Iniciando configuración de la base de datos...")
    init_db()
    print("Configuración completada")