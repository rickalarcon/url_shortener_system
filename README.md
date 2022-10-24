## Project: URL Shortener server

- Author : Rick Alarcon
- Completion Time : 4 hours
- Functional Requeriments:
  1. Users will be able to add their original URL and get back a tiny URL
  1. Users can request their Original URL with their tiny URL
  1. Server redirects to Original URL when putting the tiny URL in the Browser
  1. Implemented URL validator to make sure user original URL is valid

## This application demonstrates the following technologies:

- [Flask](https://flask.palletsprojects.com/en/2.2.x/) - Web framework for python
- [PostgreSQL](https://www.postgresql.org/) - a popular relational database
- [PostgresSQL GUI](https://www.pgadmin.org/) - a popular GUI for PostgresSQL
- [Psycopg2 ](https://www.psycopg.org/docs/) - popular postgresSQL database driver for python

## Install and Configuration

1. Clone or download source files
1. Run `pipenv install` and `pipenv shell` to active virtual enviroment
1. Create a PostgreSQL database and create a table using `Flask shell` then `db.create_all()`
