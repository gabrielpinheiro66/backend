import fastapi
from typing import TYPE_CHECKING, List
import sqlalchemy.orm as orm
import schemas
import services
from uuid import UUID

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

services.add_tables()
app = fastapi.FastAPI()


@app.post("/filmes", response_model=schemas.Filme)
async def postar_filme(
        dados_filme: schemas.FilmeCriar,
        db: orm.Session = fastapi.Depends(services.get_db)
):
    return await services.postar_filme(filme=dados_filme, db=db)


@app.get("/filmes", response_model=List)
def retornar_filmes(
        db: orm.Session = fastapi.Depends(services.get_db)
):
    return services.retornar_filmes(db=db)


@app.get("/filmes/{id}", response_model=schemas.Filme)
def retornar_filme_id(
        id: int | str | UUID,
        db: orm.Session = fastapi.Depends(services.get_db)
):
    return services.retornar_filme_id(id=id, db=db)