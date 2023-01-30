FROM python:3

COPY /requirements.txt /app/requirements.txt

COPY /app /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host=0.0.0.0"]

EXPOSE 8000
