# Databricks notebook source
# 测试 CICD 流水线 - 数据转换任务

df = spark.sql("SELECT * FROM raw_data")
transformed_df = df.filter("id IS NOT NULL").dropDuplicates()
transformed_df.write.mode("overwrite").saveAsTable("transformed_data")

print("✅ 转换完成")
