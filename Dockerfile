FROM python:3

RUN mkdir /app

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

COPY /app /app

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host=0.0.0.0"]

EXPOSE 8000
