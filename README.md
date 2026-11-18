# Data Insights

Summarize a CSV from the command line. The JSON report includes the row count and each column's inferred type, missing values and distinct non-empty values.

Install with `python -m pip install .`, then run `data-insights sales.csv`. The first row must contain column names. A header-only file returns zero rows.
