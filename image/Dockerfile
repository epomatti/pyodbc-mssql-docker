FROM python:3.10 as pyodbc

COPY . /app
WORKDIR /app

# pyodbc
RUN apt-get update
RUN apt-get install g++ unixodbc-dev -y
RUN pip install --user pyodbc

# mssql
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql18
# RUN ACCEPT_EULA=Y apt-get install -y mssql-tools18
RUN echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> ~/.bashrc
RUN . ~/.bashrc
# RUN apt-get install -y unixodbc-dev
# RUN apt-get install -y libgssapi-krb5-2