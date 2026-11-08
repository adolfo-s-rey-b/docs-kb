[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.errors.DatabaseError.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.errors.DatabaseError.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.errors.DatabaseError.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.errors.DatabaseError.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.errors.DatabaseError.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.errors.DatabaseError.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.errors.DatabaseError.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.errors.DatabaseError.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.errors.DatabaseError.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.errors.DatabaseError.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.errors.DatabaseError.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.errors.DatabaseError.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.errors.DatabaseError.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.errors.DatabaseError.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.errors.DatabaseError[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.DatabaseError.html#pandas-errors-databaseerror "Link to this heading")

=================================================================================================================================================================

exception pandas.errors.DatabaseError[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/errors/__init__.py#L936-L951)
[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.DatabaseError.html#pandas.errors.DatabaseError "Link to this definition")

Error is raised when executing SQL with bad syntax or SQL that throws an error.

Raised by [`pandas.read_sql()`](https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html#pandas.read_sql "pandas.read_sql")
 when a bad SQL statement is passed in.

See also

`read_sql`

Read SQL query or database table into a DataFrame.

Examples

\>>> from sqlite3 import connect
\>>> conn \= connect(":memory:")
\>>> pd.read\_sql("select \* test", conn)

Copy to clipboard

On this page