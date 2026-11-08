[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.read_sql_query.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.read\_sql\_query[#](https://pandas.pydata.org/docs/reference/api/pandas.read_sql_query.html#pandas-read-sql-query "Link to this heading")

=================================================================================================================================================

pandas.read\_sql\_query(_sql_, _con_, _index\_col\=None_, _coerce\_float\=True_, _params\=None_, _parse\_dates\=None_, _chunksize\=None_, _dtype\=None_, _dtype\_backend\=<no\_default>_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/sql.py#L437-L548)
[#](https://pandas.pydata.org/docs/reference/api/pandas.read_sql_query.html#pandas.read_sql_query "Link to this definition")

Read SQL query into a DataFrame.

Returns a DataFrame corresponding to the result set of the query string. Optionally provide an index\_col parameter to use one of the columns as the index, otherwise default integer index will be used.

Parameters:

**sql**str SQL query or SQLAlchemy Selectable (select or text object)

SQL query to be executed.

**con**SQLAlchemy connectable, str, or sqlite3 connection

Using SQLAlchemy makes it possible to use any DB supported by that library. If a DBAPI2 object, only sqlite3 is supported.

**index\_col**str or list of str, optional, default: None

Column(s) to set as index(MultiIndex).

**coerce\_float**bool, default True

Attempts to convert values of non-string, non-numeric objects (like decimal.Decimal) to floating point. Useful for SQL result sets. This can lose precision: an integral `decimal.Decimal` larger than `2**53` has no exact `float64` representation, so a long identifier can be silently rounded. Pass `False` to leave such values as Python objects in an `object`\-dtype column.

**params**list, tuple or mapping, optional, default: None

List of parameters to pass to execute method. The syntax used to pass parameters is database driver dependent. Check your database driver documentation for which of the five syntax styles, described in PEP 249’s paramstyle, is supported. Eg. for psycopg2, uses %(name)s so use params={‘name’ : ‘value’}.

**parse\_dates**list or dict, default: None

*   List of column names to parse as dates.
    
*   Dict of `{column_name: format string}` where format string is strftime compatible in case of parsing string times, or is one of (D, s, ns, ms, us) in case of parsing integer timestamps.
    
*   Dict of `{column_name: arg dict}`, where the arg dict corresponds to the keyword arguments of [`pandas.to_datetime()`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas.to_datetime "pandas.to_datetime")
     Especially useful with databases without native Datetime support, such as SQLite.
    

**chunksize**int, default None

If specified, return an iterator where chunksize is the number of rows to include in each chunk. By itself this typically does not reduce peak memory usage, as most drivers buffer the full result set unless a server-side cursor is used; see the [user guide](https://pandas.pydata.org/docs/user_guide/io.html#io-sql-chunksize)
 on streaming results.

**dtype**Type name or dict of columns

Data type for data or columns. E.g. np.float64 or {‘a’: np.float64, ‘b’: np.int32, ‘c’: ‘Int64’}.

**dtype\_backend**{‘numpy\_nullable’, ‘pyarrow’}

Back-end data type applied to the resultant [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 (still experimental). If not specified, the default behavior is to not use nullable data types. If specified, the behavior is as follows:

*   `"numpy_nullable"`: returns nullable-dtype-backed [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
    
*   `"pyarrow"`: returns pyarrow-backed nullable [`ArrowDtype`](https://pandas.pydata.org/docs/reference/api/pandas.ArrowDtype.html#pandas.ArrowDtype "pandas.ArrowDtype")
     [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
    

Added in version 2.0.

Returns:

DataFrame or Iterator\[DataFrame\]

Returns a DataFrame object that contains the result set of the executed SQL query, in relation to the specified database connection.

See also

[`read_sql_table`](https://pandas.pydata.org/docs/reference/api/pandas.read_sql_table.html#pandas.read_sql_table "pandas.read_sql_table")

Read SQL database table into a DataFrame.

[`read_sql`](https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html#pandas.read_sql "pandas.read_sql")

Read SQL query or database table into a DataFrame.

Notes

Any datetime values with time zone information parsed via the parse\_dates parameter will be converted to UTC.

Examples

\>>> from sqlalchemy import create\_engine
\>>> engine \= create\_engine("sqlite:///database.db")
\>>> sql\_query \= "SELECT int\_column FROM test\_data"
\>>> with engine.connect() as conn, conn.begin():
...     data \= pd.read\_sql\_query(sql\_query, conn)

Copy to clipboard

On this page