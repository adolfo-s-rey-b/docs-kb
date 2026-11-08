[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.isin.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.isin[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.isin.html#pandas-series-isin "Link to this heading")

======================================================================================================================================

Series.isin(_values_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L6538-L6615)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.isin.html#pandas.Series.isin "Link to this definition")

Whether elements in Series are contained in values.

Return a boolean Series showing whether each element in the Series matches an element in the passed sequence of values exactly.

Parameters:

**values**set or list-like

The sequence of values to test. Passing in a single string will raise a `TypeError`. Instead, turn a single string into a list of one element.

Returns:

Series

Series of booleans indicating if each element is in values.

Raises:

TypeError

*   If values is a string
    

See also

[`DataFrame.isin`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isin.html#pandas.DataFrame.isin "pandas.DataFrame.isin")

Equivalent method on DataFrame.

Examples

\>>> s \= pd.Series(
...     \["llama", "cow", "llama", "beetle", "llama", "hippo"\], name\="animal"
... )
\>>> s.isin(\["cow", "llama"\])
0     True
1     True
2     True
3    False
4     True
5    False
Name: animal, dtype: bool

Copy to clipboard

To invert the boolean values, use the `~` operator:

\>>> ~s.isin(\["cow", "llama"\])
0    False
1    False
2    False
3     True
4    False
5     True
Name: animal, dtype: bool

Copy to clipboard

Passing a single string as `s.isin('llama')` will raise an error. Use a list of one element instead:

\>>> s.isin(\["llama"\])
0     True
1    False
2     True
3    False
4     True
5    False
Name: animal, dtype: bool

Copy to clipboard

Strings and integers are distinct and are therefore not comparable:

\>>> pd.Series(\[1\]).isin(\["1"\])
0    False
dtype: bool
\>>> pd.Series(\[1.1\]).isin(\["1.1"\])
0    False
dtype: bool

Copy to clipboard

On this page