import sqlalchemy as sql
import sqlalchemy.orm as orm
from sqlalchemy.types import TypeDecorator, CHAR
import datetime as dt
import database
import uuid
from sqlalchemy.dialects.postgresql import UUID


class GUID(TypeDecorator):
    impl = CHAR

    def load_dialect_impl(self, dialect):
        if dialect.name == 'postgresql':
            return dialect.type_descriptor(UUID())
        else:
            return dialect.type_descriptor(CHAR(32))

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        elif dialect.name == 'postgresql':
            return str(value)
        else:
            if not isinstance(value, uuid.UUID):
                return "%.32x" % uuid.UUID(value).int
            else:
                # hexstring
                return "%.32x" % value.int

    def process_result_value(self, value, dialect):
        if value is None:
            return value
        else:
            if not isinstance(value, uuid.UUID):
                value = uuid.UUID(value)
            return value


class Filme(database.Base):
    __tablename__ = "filmes"
    id = sql.Column(GUID(), primary_key=True, default=lambda: str(uuid.uuid4()))
    titulo = sql.Column(sql.String, index=True)
    ano = sql.Column(sql.INTEGER)
    data_criacao = sql.Column(sql.DateTime, default=dt.datetime.utcnow)  # HORA UTC
