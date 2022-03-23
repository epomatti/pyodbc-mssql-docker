FROM pyodbc-mssql:latest as pyodbc-mssql-test

COPY . /app
WORKDIR /app

RUN pip install pipenv
RUN pipenv install --system --deploy
