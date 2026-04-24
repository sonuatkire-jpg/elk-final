FROM docker.elastic.co/logstash/logstash:9.3.3

RUN curl -L -o /usr/share/logstash/logstash-core/lib/jars/postgresql-42.2.18.jar \
    https://jdbc.postgresql.org/download/postgresql-42.6.0.jar \
  && chmod 644 /usr/share/logstash/logstash-core/lib/jars/postgresql-42.2.18.jar
