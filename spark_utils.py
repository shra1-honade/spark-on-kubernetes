import pyspark
from pyspark.sql import SparkSession
from functools import lru_cache

@lru_cache(maxsize=None)
def get_spark(name=__name__) -> SparkSession:
    return SparkSession.builder.appName(name).getOrCreate()
