[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.get.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.get.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.get.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.get.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.get.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.get.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.get.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.get.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.get.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.get.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.get.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.get.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.get.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.get.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.get[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.get.html#pandas-dataframe-get "Link to this heading")

============================================================================================================================================

DataFrame.get(_key_, _default\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L4411-L4488)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.get.html#pandas.DataFrame.get "Link to this definition")

Get item from object for given key (ex: DataFrame column).

Returns `default` value if not found.

Parameters:

**key**object

Key for which item should be returned.

**default**object, default None

Default value to return if key is not found.

Returns:

same type as items contained in object

Item for given key or `default` value, if key is not found.

See also

[`DataFrame.get`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.get.html#pandas.DataFrame.get "pandas.DataFrame.get")

Get item from object for given key (ex: DataFrame column).

[`Series.get`](https://pandas.pydata.org/docs/reference/api/pandas.Series.get.html#pandas.Series.get "pandas.Series.get")

Get item from object for given key (ex: DataFrame column).

Examples

\>>> df \= pd.DataFrame(
...     \[\
...         \[24.3, 75.7, "high"\],\
...         \[31, 87.8, "high"\],\
...         \[22, 71.6, "medium"\],\
...         \[35, 95, "medium"\],\
...     \],
...     columns\=\["temp\_celsius", "temp\_fahrenheit", "windspeed"\],
...     index\=pd.date\_range(start\="2014-02-12", end\="2014-02-15", freq\="D"),
... )

Copy to clipboard

\>>> df
            temp\_celsius  temp\_fahrenheit windspeed
2014-02-12          24.3             75.7      high
2014-02-13          31.0             87.8      high
2014-02-14          22.0             71.6    medium
2014-02-15          35.0             95.0    medium

Copy to clipboard

\>>> df.get(\["temp\_celsius", "windspeed"\])
            temp\_celsius windspeed
2014-02-12          24.3      high
2014-02-13          31.0      high
2014-02-14          22.0    medium
2014-02-15          35.0    medium

Copy to clipboard

\>>> ser \= df\["windspeed"\]
\>>> ser.get("2014-02-13")
'high'

Copy to clipboard

If the key isn’t found, the default value will be used.

\>>> df.get(\["temp\_celsius", "temp\_kelvin"\], default\="default\_value")
'default\_value'

Copy to clipboard

\>>> ser.get("2014-02-10", "\[unknown\]")
'\[unknown\]'

Copy to clipboard

When passing a list of keys, all keys must be present. If any key is missing, the `default` value is returned instead of a partial result.

\>>> ser \= pd.Series(\["a", "b", "c"\], index\=\[1, 2, 3\])
\>>> ser.get(\[1, 2\])
1    a
2    b
dtype: str
\>>> ser.get(\[1, 2, \-1\]) is None
True

Copy to clipboard

On this page