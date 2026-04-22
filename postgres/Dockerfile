FROM postgres:13

ENV POSTGRES_DB=bankdb
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=password

COPY init.sql /docker-entrypoint-initdb.d/