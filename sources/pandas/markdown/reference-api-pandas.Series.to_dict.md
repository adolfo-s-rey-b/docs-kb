[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_dict.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.to_dict.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_dict.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.to_dict.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.to_dict.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.to_dict.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.to_dict.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.to_dict.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.to_dict.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.to_dict.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.to_dict.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.to_dict.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.to_dict.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.to_dict.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.to\_dict[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_dict.html#pandas-series-to-dict "Link to this heading")

================================================================================================================================================

Series.to\_dict(_\*_, _into\=<class 'dict'>_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L1933-L1984)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_dict.html#pandas.Series.to_dict "Link to this definition")

Convert Series to {label -> value} dict or dict-like object.

The resulting dict-like object maps each index label to its corresponding value. A custom `MutableMapping` subclass can be specified via the `into` parameter.

Parameters:

**into**class, default dict

The collections.abc.MutableMapping subclass to use as the return object. Can be the actual class or an empty instance of the mapping type you want. If you want a collections.defaultdict, you must pass it initialized.

Returns:

collections.abc.MutableMapping

Key-value representation of Series.

See also

[`Series.to_list`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_list.html#pandas.Series.to_list "pandas.Series.to_list")

Converts Series to a list of the values.

[`Series.to_numpy`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_numpy.html#pandas.Series.to_numpy "pandas.Series.to_numpy")

Converts Series to NumPy ndarray.

[`Series.array`](https://pandas.pydata.org/docs/reference/api/pandas.Series.array.html#pandas.Series.array "pandas.Series.array")

ExtensionArray of the data backing this Series.

Examples

\>>> s \= pd.Series(\[1, 2, 3, 4\])
\>>> s.to\_dict()
{0: 1, 1: 2, 2: 3, 3: 4}
\>>> from collections import OrderedDict, defaultdict
\>>> s.to\_dict(into\=OrderedDict)
OrderedDict({0: 1, 1: 2, 2: 3, 3: 4})
\>>> dd \= defaultdict(list)
\>>> s.to\_dict(into\=dd)
defaultdict(<class 'list'>, {0: 1, 1: 2, 2: 3, 3: 4})

Copy to clipboard

On this page