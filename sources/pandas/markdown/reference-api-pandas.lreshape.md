[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.lreshape.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.lreshape.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.lreshape.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.lreshape.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.lreshape.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.lreshape.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.lreshape.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.lreshape.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.lreshape.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.lreshape.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.lreshape.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.lreshape.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.lreshape.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.lreshape.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.lreshape[#](https://pandas.pydata.org/docs/reference/api/pandas.lreshape.html#pandas-lreshape "Link to this heading")

=============================================================================================================================

pandas.lreshape(_data_, _groups_, _dropna\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/reshape/melt.py#L289-L375)
[#](https://pandas.pydata.org/docs/reference/api/pandas.lreshape.html#pandas.lreshape "Link to this definition")

Reshape wide-format data to long. Generalized inverse of DataFrame.pivot.

Accepts a dictionary, `groups`, in which each key is a new column name and each value is a list of old column names that will be “melted” under the new column name as part of the reshape.

Parameters:

**data**DataFrame

The wide-format DataFrame.

**groups**dict

{new\_name : list\_of\_columns}.

**dropna**bool, default True

Do not include columns whose entries are all NaN.

Returns:

DataFrame

Reshaped DataFrame.

See also

[`melt`](https://pandas.pydata.org/docs/reference/api/pandas.melt.html#pandas.melt "pandas.melt")

Unpivot a DataFrame from wide to long format, optionally leaving identifiers set.

[`pivot`](https://pandas.pydata.org/docs/reference/api/pandas.pivot.html#pandas.pivot "pandas.pivot")

Create a spreadsheet-style pivot table as a DataFrame.

[`DataFrame.pivot`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot.html#pandas.DataFrame.pivot "pandas.DataFrame.pivot")

Pivot without aggregation that can handle non-numeric data.

[`DataFrame.pivot_table`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot_table.html#pandas.DataFrame.pivot_table "pandas.DataFrame.pivot_table")

Generalization of pivot that can handle duplicate values for one index/column pair.

[`DataFrame.unstack`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.unstack.html#pandas.DataFrame.unstack "pandas.DataFrame.unstack")

Pivot based on the index values instead of a column.

[`wide_to_long`](https://pandas.pydata.org/docs/reference/api/pandas.wide_to_long.html#pandas.wide_to_long "pandas.wide_to_long")

Wide panel to long format. Less flexible but more user-friendly than melt.

Examples

\>>> data \= pd.DataFrame(
...     {
...         "hr1": \[514, 573\],
...         "hr2": \[545, 526\],
...         "team": \["Red Sox", "Yankees"\],
...         "year1": \[2007, 2007\],
...         "year2": \[2008, 2008\],
...     }
... )
\>>> data
   hr1  hr2     team  year1  year2
0  514  545  Red Sox   2007   2008
1  573  526  Yankees   2007   2008

Copy to clipboard

\>>> pd.lreshape(data, {"year": \["year1", "year2"\], "hr": \["hr1", "hr2"\]})
      team  year   hr
0  Red Sox  2007  514
1  Yankees  2007  573
2  Red Sox  2008  545
3  Yankees  2008  526

Copy to clipboard

On this page