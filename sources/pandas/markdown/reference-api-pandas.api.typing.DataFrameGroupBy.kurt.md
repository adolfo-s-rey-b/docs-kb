[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.kurt.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.DataFrameGroupBy.kurt.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.kurt.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.DataFrameGroupBy.kurt.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.DataFrameGroupBy.kurt.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.DataFrameGroupBy.kurt.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.DataFrameGroupBy.kurt.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.DataFrameGroupBy.kurt.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.DataFrameGroupBy.kurt.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.DataFrameGroupBy.kurt.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.DataFrameGroupBy.kurt.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.DataFrameGroupBy.kurt.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.DataFrameGroupBy.kurt.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.DataFrameGroupBy.kurt.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.DataFrameGroupBy.kurt[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.kurt.html#pandas-api-typing-dataframegroupby-kurt "Link to this heading")

=====================================================================================================================================================================================================

DataFrameGroupBy.kurt(_skipna\=True_, _numeric\_only\=False_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/generic.py#L3691-L3798)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.kurt.html#pandas.api.typing.DataFrameGroupBy.kurt "Link to this definition")

Return unbiased kurtosis within groups.

Kurtosis obtained using Fisher’s definition (kurtosis of normal == 0.0), normalized by N-1. Values are computed for each numeric column within each group.

Parameters:

**skipna**bool, default True

Exclude NA/null values when computing the result.

**numeric\_only**bool, default False

Include only float, int, boolean columns.

**\*\*kwargs**

Additional keyword arguments to be passed to the function.

Returns:

DataFrame

Unbiased kurtosis within groups.

See also

`DataFrame.kurt`

Return unbiased kurtosis over requested axis.

Examples

\>>> arrays \= \[\
...     \[\
...         "falcon",\
...         "parrot",\
...         "cockatoo",\
...         "kiwi",\
...         "eagle",\
...         "lion",\
...         "monkey",\
...         "rabbit",\
...         "dog",\
...         "wolf",\
...     \],\
...     \[\
...         "bird",\
...         "bird",\
...         "bird",\
...         "bird",\
...         "bird",\
...         "mammal",\
...         "mammal",\
...         "mammal",\
...         "mammal",\
...         "mammal",\
...     \],\
... \]
\>>> index \= pd.MultiIndex.from\_arrays(arrays, names\=("name", "class"))
\>>> df \= pd.DataFrame(
...     {
...         "max\_speed": \[\
...             389.0,\
...             24.0,\
...             70.0,\
...             np.nan,\
...             350.0,\
...             80.5,\
...             21.5,\
...             15.0,\
...             40.0,\
...             50.0,\
...         \]
...     },
...     index\=index,
... )
\>>> df
                 max\_speed
name     class
falcon   bird        389.0
parrot   bird         24.0
cockatoo bird         70.0
kiwi     bird          NaN
eagle    bird        350.0
lion     mammal       80.5
monkey   mammal       21.5
rabbit   mammal       15.0
dog      mammal       40.0
wolf     mammal       50.0
\>>> gb \= df.groupby(\["class"\])
\>>> gb.kurt()
        max\_speed
class
bird    -5.493277
mammal   0.204125
\>>> gb.kurt(skipna\=False)
        max\_speed
class
bird          NaN
mammal   0.204125

Copy to clipboard

On this page