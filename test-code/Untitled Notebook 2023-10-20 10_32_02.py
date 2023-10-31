# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE tableA
# MAGIC (date STRING, label STRING, id INT)
# MAGIC USING DELTA
# MAGIC TBLPROPERTIES (delta.enableChangeDataFeed = true)
