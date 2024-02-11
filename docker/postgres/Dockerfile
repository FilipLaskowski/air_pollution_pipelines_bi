FROM postgres:alpine

ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DB=airflow_db
ENV POSTGRES_USER=postgres
ENV POSTGRES_PORT=5432

COPY init.sql /docker-entrypoint-initdb.d/