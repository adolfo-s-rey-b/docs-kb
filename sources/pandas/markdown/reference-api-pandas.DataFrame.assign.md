[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.assign.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.assign.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.assign.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.assign.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.assign.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.assign.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.assign.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.assign.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.assign.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.assign.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.assign.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.assign.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.assign.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.assign.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.assign[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.assign.html#pandas-dataframe-assign "Link to this heading")

=====================================================================================================================================================

DataFrame.assign(_\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L6273-L6380)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.assign.html#pandas.DataFrame.assign "Link to this definition")

Assign new columns to a DataFrame.

Returns a new object with all original columns in addition to new ones. Existing columns that are re-assigned will be overwritten.

Parameters:

**\*\*kwargs**callable, Series, scalar, array-like, or dict

The column names are keywords. If the values are callable, they are computed on the DataFrame and assigned to the new columns. The callable must not change input DataFrame (though pandas doesn’t check it). If the values are not callable (e.g. a Series, scalar, array, or dict), they are simply assigned. See the Notes section for details on alignment and broadcasting.

Returns:

DataFrame

A new DataFrame with the new columns in addition to all the existing columns.

See also

[`DataFrame.loc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html#pandas.DataFrame.loc "pandas.DataFrame.loc")

Select a subset of a DataFrame by labels.

[`DataFrame.iloc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html#pandas.DataFrame.iloc "pandas.DataFrame.iloc")

Select a subset of a DataFrame by positions.

Notes

Assigning multiple columns within the same `assign` is possible. Later items in ‘\*\*kwargs’ may refer to newly created or modified columns in ‘df’; items are computed and assigned into ‘df’ in order. Non-callable values (Series, arrays, scalars) follow the same alignment and broadcasting rules as `DataFrame.__setitem__()`. See that method’s documentation for details.

Examples

\>>> df \= pd.DataFrame({"temp\_c": \[17.0, 25.0\]}, index\=\["Portland", "Berkeley"\])
\>>> df
          temp\_c
Portland    17.0
Berkeley    25.0

Copy to clipboard

Where the value is a callable, evaluated on df:

\>>> df.assign(temp\_f\=lambda x: x.temp\_c \* 9 / 5 + 32)
          temp\_c  temp\_f
Portland    17.0    62.6
Berkeley    25.0    77.0

Copy to clipboard

Alternatively, the same behavior can be achieved by directly referencing an existing Series or sequence:

\>>> df.assign(temp\_f\=df\["temp\_c"\] \* 9 / 5 + 32)
          temp\_c  temp\_f
Portland    17.0    62.6
Berkeley    25.0    77.0

Copy to clipboard

or by using [`pandas.col()`](https://pandas.pydata.org/docs/reference/api/pandas.col.html#pandas.col "pandas.col")
:

\>>> df.assign(temp\_f\=pd.col("temp\_c") \* 9 / 5 + 32)
          temp\_c  temp\_f
Portland    17.0    62.6
Berkeley    25.0    77.0

Copy to clipboard

You can create multiple columns within the same assign where one of the columns depends on another one defined within the same assign:

\>>> df.assign(
...     temp\_f\=lambda x: x\["temp\_c"\] \* 9 / 5 + 32,
...     temp\_k\=lambda x: (x\["temp\_f"\] + 459.67) \* 5 / 9,
... )
          temp\_c  temp\_f  temp\_k
Portland    17.0    62.6  290.15
Berkeley    25.0    77.0  298.15

Copy to clipboard

A dict value is aligned to the DataFrame’s index by its keys, and index labels not present in the dict are filled with NaN:

\>>> df.assign(temp\_k\={"Portland": 290.15, "Berkeley": 298.15, "Seattle": 285.0})
          temp\_c  temp\_k
Portland    17.0  290.15
Berkeley    25.0  298.15

Copy to clipboard

On this page