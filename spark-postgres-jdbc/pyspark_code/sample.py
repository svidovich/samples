from pyspark.context import SparkContext
from pyspark.sql import SparkSession

spark_context = SparkContext.getOrCreate()
spark_session = SparkSession.builder.getOrCreate()


def main():
    sample_dataframe = spark_context.parallelize(
        [
            {
                'first_name': 'Jeff',
                'last_name': 'Lebowski',
                'nickname': 'The Dude',
            }
        ]
    ).toDF()

    sample_dataframe.show()


if __name__ == '__main__':
    main()
