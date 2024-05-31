# Phase one (Data Analysis):
* The Exploratory data analysis file could be found at both:
* `notebooks/exploratory_data_analysis.ipynb`
* Redundancy in case of problems with jupyter notebook:
* `notebooks/exploratory_data_analysis.py`

# Phase two (Data transformation):
* The second file respective to pipeline, could be found thought the following path:
* `etls/insert_data_into_bigquery.py`
* It's a classic extract, transform and load (ETL) pipeline.
* It takes data from Excel files and transform them with pandas to load out to BigQuery, the database system of my choice.
* There's a shell script to execute the pipeline that could be executed with the following:
* `bash scripts/execute_pipeline.sh`

# Phase three (Data visualization):
* I've used Looker studio as reporting tool, basically because of the integration with Google's BigQuery.
### Looker studio report link:
* `https://lookerstudio.google.com/u/0/reporting/7fdc99f6-41ed-425c-980f-705113b002f3/page/Dov1D`

# Phase Four (Database):
* You could find out the both queries respectively at:
* `queries/five_worst_days_in_sales.sql`
* This query had the goal to identify the worst days in sales, so we could take actions against them.
* `queries/top_5_days_with_more_clients.sql`
* This query had the goal to identify what days and periods were more effective in terms of marketing, to reuse the same strategies