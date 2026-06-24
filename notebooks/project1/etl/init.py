# Databricks notebook source
# 测试 CICD 流水线 - 初始化 ETL 任务

spark.conf.set("spark.sql.shuffle.partitions", "8")

raw_df = spark.read.json("/mnt/raw/sample_data")
raw_df.createOrReplaceTempView("raw_data")

print("✅ 初始化完成")
