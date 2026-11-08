[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.json_normalize.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.json_normalize.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.json_normalize.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.json_normalize.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.json_normalize.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.json_normalize.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.json_normalize.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.json_normalize.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.json_normalize.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.json_normalize.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.json_normalize.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.json_normalize.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.json\_normalize[#](https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html#pandas-json-normalize "Link to this heading")

================================================================================================================================================

pandas.json\_normalize(_data_, _record\_path\=None_, _meta\=None_, _meta\_prefix\=None_, _record\_prefix\=None_, _errors\='raise'_, _sep\='.'_, _max\_level\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/json/_normalize.py#L302-L670)
[#](https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html#pandas.json_normalize "Link to this definition")

Normalize semi-structured JSON data into a flat table.

This method is designed to transform semi-structured JSON data, such as nested dictionaries or lists, into a flat table. This is particularly useful when handling JSON-like data structures that contain deeply nested fields.

Parameters:

**data**dict, list of dicts, or Series of dicts

Unserialized JSON objects.

**record\_path**str or list of str, default None

Path in each object to list of records. If not passed, data will be assumed to be an array of records.

**meta**list of paths (str or list of str), default None

Fields to use as metadata for each record in resulting table.

**meta\_prefix**str, default None

If not None, prefix meta fields with this string.

**record\_prefix**str, default None

If not None, prefix record fields with this string.

**errors**{‘raise’, ‘ignore’}, default ‘raise’

Configures error handling.

*   ‘ignore’ : will ignore KeyError if keys listed in meta are not always present.
    
*   ‘raise’ : will raise KeyError if keys listed in meta are not always present.
    

**sep**str, default ‘.’

Nested records will generate names separated by sep. e.g., for sep=’.’, {‘foo’: {‘bar’: 0}} -> foo.bar.

**max\_level**int, default None

Max number of levels(depth of dict) to normalize. if None, normalizes all levels.

Returns:

DataFrame

The normalized data, represented as a pandas DataFrame.

See also

[`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")

Two-dimensional, size-mutable, potentially heterogeneous tabular data.

[`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")

One-dimensional ndarray with axis labels (including time series).

Examples

\>>> data \= \[\
...     {"id": 1, "name": {"first": "Coleen", "last": "Volk"}},\
...     {"name": {"given": "Mark", "family": "Regner"}},\
...     {"id": 2, "name": "Faye Raker"},\
... \]
\>>> pd.json\_normalize(data)
    id name.first name.last name.given name.family        name
0  1.0     Coleen      Volk        NaN         NaN         NaN
1  NaN        NaN       NaN       Mark      Regner         NaN
2  2.0        NaN       NaN        NaN         NaN  Faye Raker

Copy to clipboard

\>>> data \= \[\
...     {\
...         "id": 1,\
...         "name": "Cole Volk",\
...         "fitness": {"height": 130, "weight": 60},\
...     },\
...     {"name": "Mark Reg", "fitness": {"height": 130, "weight": 60}},\
...     {\
...         "id": 2,\
...         "name": "Faye Raker",\
...         "fitness": {"height": 130, "weight": 60},\
...     },\
... \]
\>>> pd.json\_normalize(data, max\_level\=0)
    id        name                        fitness
0  1.0   Cole Volk  {'height': 130, 'weight': 60}
1  NaN    Mark Reg  {'height': 130, 'weight': 60}
2  2.0  Faye Raker  {'height': 130, 'weight': 60}

Copy to clipboard

Normalizes nested data up to level 1.

\>>> data \= \[\
...     {\
...         "id": 1,\
...         "name": "Cole Volk",\
...         "fitness": {"height": 130, "weight": 60},\
...     },\
...     {"name": "Mark Reg", "fitness": {"height": 130, "weight": 60}},\
...     {\
...         "id": 2,\
...         "name": "Faye Raker",\
...         "fitness": {"height": 130, "weight": 60},\
...     },\
... \]
\>>> pd.json\_normalize(data, max\_level\=1)
    id        name  fitness.height  fitness.weight
0  1.0   Cole Volk             130              60
1  NaN    Mark Reg             130              60
2  2.0  Faye Raker             130              60

Copy to clipboard

\>>> data \= \[\
...     {\
...         "id": 1,\
...         "name": "Cole Volk",\
...         "fitness": {"height": 130, "weight": 60},\
...     },\
...     {"name": "Mark Reg", "fitness": {"height": 130, "weight": 60}},\
...     {\
...         "id": 2,\
...         "name": "Faye Raker",\
...         "fitness": {"height": 130, "weight": 60},\
...     },\
... \]
\>>> series \= pd.Series(data, index\=pd.Index(\["a", "b", "c"\]))
\>>> pd.json\_normalize(series)
    id        name  fitness.height  fitness.weight
a  1.0   Cole Volk             130              60
b  NaN    Mark Reg             130              60
c  2.0  Faye Raker             130              60

Copy to clipboard

\>>> data \= \[\
...     {\
...         "state": "Florida",\
...         "shortname": "FL",\
...         "info": {"governor": "Rick Scott"},\
...         "counties": \[\
...             {"name": "Dade", "population": 12345},\
...             {"name": "Broward", "population": 40000},\
...             {"name": "Palm Beach", "population": 60000},\
...         \],\
...     },\
...     {\
...         "state": "Ohio",\
...         "shortname": "OH",\
...         "info": {"governor": "John Kasich"},\
...         "counties": \[\
...             {"name": "Summit", "population": 1234},\
...             {"name": "Cuyahoga", "population": 1337},\
...         \],\
...     },\
... \]
\>>> result \= pd.json\_normalize(
...     data, "counties", \["state", "shortname", \["info", "governor"\]\]
... )
\>>> result
         name  population    state shortname info.governor
0        Dade       12345   Florida    FL    Rick Scott
1     Broward       40000   Florida    FL    Rick Scott
2  Palm Beach       60000   Florida    FL    Rick Scott
3      Summit        1234   Ohio       OH    John Kasich
4    Cuyahoga        1337   Ohio       OH    John Kasich

Copy to clipboard

\>>> data \= {"A": \[1, 2\]}
\>>> pd.json\_normalize(data, "A", record\_prefix\="Prefix.")
    Prefix.0
0          1
1          2

Copy to clipboard

Returns normalized data with columns prefixed with the given string.

\>>> data \= \[\
...     {\
...         "state": "Florida",\
...         "shortname": "FL",\
...         "info": {"governor": "Rick Scott"},\
...         "counties": \[{"name": "Dade", "population": 12345}\],\
...     },\
... \]
\>>> pd.json\_normalize(
...     data,
...     "counties",
...     \["state", "shortname", \["info", "governor"\]\],
...     meta\_prefix\="meta.",
... )
   name  population meta.state meta.shortname meta.info.governor
0  Dade       12345    Florida             FL         Rick Scott

Copy to clipboard

Meta fields are prefixed with the given string.

On this page