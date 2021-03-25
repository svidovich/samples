FROM bitnami/spark
RUN curl -4 https://jdbc.postgresql.org/download/postgresql-42.2.19.jar --output /opt/bitnami/spark/jars/postgresql.jar