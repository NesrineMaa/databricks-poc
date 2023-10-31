# Databricks notebook source
# MAGIC %md
# MAGIC This notebook is created to perform Change Data Capture

# COMMAND ----------

# MAGIC %md
# MAGIC Step 1 : Enable CDF

# COMMAND ----------

# MAGIC %sql
# MAGIC Alter TABLE `hive_metastore`.`default`.`claim`
# MAGIC SET TBLPROPERTIES (delta.enableChangeDataFeed = true)

# COMMAND ----------

# MAGIC %md
# MAGIC Step 2 : Update data 

# COMMAND ----------

# MAGIC %sql
# MAGIC UPDATE `hive_metastore`.`default`.`claim`
# MAGIC SET description = 'Research edge second game of' WHERE Id = '2501'
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Step 3 : Check table changes 

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM table_changes('claim',1)
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Enable CDF while creating a table
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE student (id INT, name STRING, age INT) TBLPROPERTIES (delta.enableChangeDataFeed = true)
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Enable CDF for all new tables (will be created in the future)

# COMMAND ----------

# MAGIC %sql
# MAGIC set spark.databricks.delta.properties.defaults.enableChangeDataFeed = true;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE student (id INT, name STRING, age INT)
# MAGIC
