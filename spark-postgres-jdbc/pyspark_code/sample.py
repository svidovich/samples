from pyspark.context import SparkContext
from pyspark.sql import SparkSession

spark_context = SparkContext.getOrCreate()
spark_session = SparkSession.builder.getOrCreate()


def main():
    pass


if __name__ == '__main__':
    main()
