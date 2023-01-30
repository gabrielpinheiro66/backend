from typing import TYPE_CHECKING
import database
import schemas
import models
from uuid import UUID

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


def add_tables():
    return database.Base.metadata.create_all(bind=database.engine)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def postar_filme(
        filme: schemas.FilmeCriar, db: "Session"
) -> schemas.Filme:
    filme = models.Filme(**filme.dict())
    db.add(filme)
    db.commit()
    db.refresh(filme)
    return schemas.Filme.from_orm(filme)


def retornar_filmes(db: "Session"):
    return db.query(models.Filme).all()


def retornar_filme_id(db: "Session", id: int | str | UUID):
    return db.query(models.Filme).filter(models.Filme.id == id).first()


