import os

from pyspark.context import SparkContext
from pyspark.sql import SparkSession

spark_context = SparkContext.getOrCreate()
spark_session = SparkSession.builder.getOrCreate()


def main():
    database = 'spark_test'
    database_user = os.environ['SPARK_DATABASE_USER']
    database_password = os.environ['SPARK_DATABASE_PASSWORD']

    jdbc_dataframe = spark_session.read.format(
        'jdbc'
    ).option(
        'url', f'jdbc:postgresql://database:5432/{database}'
    ).option(
        'dbtable', 'public.test_table'
    ).option(
        'user', database_user
    ).option(
        'password', database_password
    ).load()

    jdbc_dataframe.show()


if __name__ == '__main__':
    main()
