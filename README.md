# pyodbc image

An image with Python pyodbc for Microsoft SQL Server.

### Get 

```sh
docker pull epomatti/pyodbc:tagname
```

### Testing

SQL Server

```sh
docker pull mcr.microsoft.com/mssql/server
docker run -e 'ACCEPT_EULA=Y' -e 'MSSQL_SA_PASSWORD=<YourPassword>' -p 1433:1433 -d mcr.microsoft.com/mssql/server
```

Copy and edit the configuration file

```sh
cp config.dev.ini config.ini
```

Build and test

```sh
docker image build -t pyodbc:latest .
docker run -it pyodbc:latest sh
python3.8 test/connection_test.py
```
