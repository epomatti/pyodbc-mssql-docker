FROM python:3.8 as pyodbc

COPY . /app
WORKDIR /app

# Required for msodbcsql17 and mssql-tools
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys BA6932366A755776
RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update

RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17 mssql-tools
RUN apt-get install unixodbc-dev

RUN pip install pipenv
RUN pipenv install --system --deploy