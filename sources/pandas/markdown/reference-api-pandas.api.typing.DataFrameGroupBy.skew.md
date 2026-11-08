[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.skew.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.DataFrameGroupBy.skew.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.skew.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.DataFrameGroupBy.skew.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.DataFrameGroupBy.skew.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.DataFrameGroupBy.skew.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.DataFrameGroupBy.skew.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.DataFrameGroupBy.skew.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.DataFrameGroupBy.skew.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.DataFrameGroupBy.skew.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.DataFrameGroupBy.skew.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.DataFrameGroupBy.skew.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.DataFrameGroupBy.skew.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.DataFrameGroupBy.skew.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.DataFrameGroupBy.skew[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.skew.html#pandas-api-typing-dataframegroupby-skew "Link to this heading")

=====================================================================================================================================================================================================

DataFrameGroupBy.skew(_skipna\=True_, _numeric\_only\=False_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/generic.py#L3606-L3689)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.skew.html#pandas.api.typing.DataFrameGroupBy.skew "Link to this definition")

Return unbiased skew within groups.

Normalized by N-1.

Parameters:

**skipna**bool, default True

Exclude NA/null values when computing the result.

**numeric\_only**bool, default False

Include only float, int, boolean columns.

**\*\*kwargs**

Additional keyword arguments to be passed to the function.

Deprecated since version 3.1.0: Passing `**kwargs` to DataFrameGroupBy.skew is deprecated and will be removed in a future version of pandas.

Returns:

DataFrame

Unbiased skew within groups.

See also

`DataFrame.skew`

Return unbiased skew over requested axis.

Examples

\>>> arrays \= \[\
...     \["falcon", "parrot", "cockatoo", "kiwi", "lion", "monkey", "rabbit"\],\
...     \["bird", "bird", "bird", "bird", "mammal", "mammal", "mammal"\],\
... \]
\>>> index \= pd.MultiIndex.from\_arrays(arrays, names\=("name", "class"))
\>>> df \= pd.DataFrame(
...     {"max\_speed": \[389.0, 24.0, 70.0, np.nan, 80.5, 21.5, 15.0\]},
...     index\=index,
... )
\>>> df
                max\_speed
name     class
falcon   bird        389.0
parrot   bird         24.0
cockatoo bird         70.0
kiwi     bird          NaN
lion     mammal       80.5
monkey   mammal       21.5
rabbit   mammal       15.0
\>>> gb \= df.groupby(\["class"\])
\>>> gb.skew()
        max\_speed
class
bird     1.628296
mammal   1.669046
\>>> gb.skew(skipna\=False)
        max\_speed
class
bird          NaN
mammal   1.669046

Copy to clipboard

On this page