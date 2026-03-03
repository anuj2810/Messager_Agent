"""
Setup PostgreSQL initialization. Wait actually init.sql
Should be located under ./initdb. In Dockercompose we will map
"./ initdb: / docker - entrypoint - initdb.d :ro / " so Postgres natively
bootstrap the schema DB role.
"""