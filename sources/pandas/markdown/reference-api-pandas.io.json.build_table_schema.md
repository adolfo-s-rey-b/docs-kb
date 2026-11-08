[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.json.build_table_schema.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.io.json.build_table_schema.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.io.json.build_table_schema.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.io.json.build_table_schema.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.io.json.build_table_schema.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.io.json.build_table_schema.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.io.json.build_table_schema.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.io.json.build_table_schema.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.io.json.build_table_schema.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.io.json.build_table_schema.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.io.json.build_table_schema.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.io.json.build_table_schema.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.io.json.build_table_schema.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.io.json.build_table_schema.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.json.build\_table\_schema[#](https://pandas.pydata.org/docs/reference/api/pandas.io.json.build_table_schema.html#pandas-io-json-build-table-schema "Link to this heading")

=====================================================================================================================================================================================

pandas.io.json.build\_table\_schema(_data_, _index\=True_, _primary\_key\=None_, _version\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/json/_table_schema.py#L238-L340)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.json.build_table_schema.html#pandas.io.json.build_table_schema "Link to this definition")

Create a Table schema from `data`.

This method is a utility to generate a JSON-serializable schema representation of a pandas Series or DataFrame, compatible with the Table Schema specification. It enables structured data to be shared and validated in various applications, ensuring consistency and interoperability.

Parameters:

**data**Series or DataFrame

The input data for which the table schema is to be created.

**index**bool, default True

Whether to include `data.index` in the schema.

**primary\_key**bool or None, default True

Column names to designate as the primary key. The default None will set ‘primaryKey’ to the index level or levels if the index is unique.

**version**bool, default True

Whether to include a field pandas\_version with the version of pandas that last revised the table schema. This version can be different from the installed pandas version.

Returns:

dict

A dictionary representing the Table schema.

See also

`DataFrame.to_json`

Convert the object to a JSON string.

`read_json`

Convert a JSON string to pandas object.

Notes

See [Table Schema](https://pandas.pydata.org/docs/user_guide/io.html#table-schema)
 for conversion types. Timedeltas as converted to ISO8601 duration format with 9 decimal places after the seconds field for nanosecond precision.

Categoricals are converted to the any dtype, and use the enum field constraint to list the allowed values. The ordered attribute is included in an ordered field.

Examples

\>>> from pandas.io.json.\_table\_schema import build\_table\_schema
\>>> df \= pd.DataFrame(
...     {'A': \[1, 2, 3\],
...      'B': \['a', 'b', 'c'\],
...      'C': pd.date\_range('2016-01-01', freq\='D', periods\=3),
...      }, index\=pd.Index(range(3), name\='idx'))
\>>> build\_table\_schema(df)
{'fields': \[{'name': 'idx', 'type': 'integer'}, {'name': 'A', 'type': 'integer'}, {'name': 'B', 'type': 'string', 'extDtype': 'str'}, {'name': 'C', 'type': 'datetime'}\], 'primaryKey': \['idx'\], 'pandas\_version': '1.4.0'}

Copy to clipboard

On this page