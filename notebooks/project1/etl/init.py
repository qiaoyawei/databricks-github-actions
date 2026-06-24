# Databricks notebook source
# 测试 CICD 流水线 - 初始化 ETL 任务
# tt

spark.conf.set("spark.sql.shuffle.partitions", "8")

raw_df = spark.read.json("/mnt/raw/sample_data")
raw_df.createOrReplaceTempView("raw_data")

# v4 - 测试 CLI v2 部署
df_count = spark.sql("SELECT COUNT(*) as cnt FROM raw_data").collect()[0]["cnt"]
print(f"✅ 初始化完成，共 {df_count} 条记录")
