[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_feather.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.to\_feather[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_feather.html#pandas-dataframe-to-feather "Link to this heading")

==================================================================================================================================================================

DataFrame.to\_feather(_path_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L2675-L2718)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_feather.html#pandas.DataFrame.to_feather "Link to this definition")

Write a DataFrame to the binary Feather format.

The Feather format is a lightweight, language-agnostic columnar file format based on Apache Arrow, designed for efficient read and write performance. This method requires the `pyarrow` library.

Parameters:

**path**str, path object, file-like object

String, path object (implementing `os.PathLike[str]`), or file-like object implementing a binary `write()` function. If a string or a path, it will be used as Root Directory path when writing a partitioned dataset.

**\*\*kwargs**

Additional keywords passed to [`pyarrow.feather.write_feather()`](https://arrow.apache.org/docs/python/generated/pyarrow.feather.write_feather.html#pyarrow.feather.write_feather "(in Apache Arrow v26.0.1)")
. This includes the compression, compression\_level, chunksize and version keywords.

See also

[`DataFrame.to_parquet`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_parquet.html#pandas.DataFrame.to_parquet "pandas.DataFrame.to_parquet")

Write a DataFrame to the binary parquet format.

[`DataFrame.to_excel`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html#pandas.DataFrame.to_excel "pandas.DataFrame.to_excel")

Write object to an Excel sheet.

[`DataFrame.to_sql`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html#pandas.DataFrame.to_sql "pandas.DataFrame.to_sql")

Write to a sql table.

[`DataFrame.to_csv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html#pandas.DataFrame.to_csv "pandas.DataFrame.to_csv")

Write a csv file.

[`DataFrame.to_json`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_json.html#pandas.DataFrame.to_json "pandas.DataFrame.to_json")

Convert the object to a JSON string.

[`DataFrame.to_html`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_html.html#pandas.DataFrame.to_html "pandas.DataFrame.to_html")

Render a DataFrame as an HTML table.

[`DataFrame.to_string`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_string.html#pandas.DataFrame.to_string "pandas.DataFrame.to_string")

Convert DataFrame to a string.

Notes

This function writes the dataframe as a [feather file](https://arrow.apache.org/docs/python/feather.html)
. Requires a default index. For saving the DataFrame with your custom index use a method that supports custom indices e.g. to\_parquet.

Examples

\>>> df \= pd.DataFrame(\[\[1, 2, 3\], \[4, 5, 6\]\])
\>>> df.to\_feather("file.feather")

Copy to clipboard

On this page