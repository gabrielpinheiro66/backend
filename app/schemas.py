import pydantic
import datetime as dt
from uuid import UUID


class BaseFilme(pydantic.BaseModel):
    pass


class FilmeCriar(BaseFilme):
    titulo: str
    ano: int
    pass


class Filme(FilmeCriar):
    id: int | str | UUID
    data_criacao: dt.datetime
    class Config:
        orm_mode = True