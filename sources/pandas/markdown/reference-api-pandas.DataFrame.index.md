[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.index.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.index.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.index.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.index.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.index.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.index.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.index.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.index.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.index.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.index.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.index.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.index.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.index.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.index.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.index[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.index.html#pandas-dataframe-index "Link to this heading")

==================================================================================================================================================

DataFrame.index[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.index.html#pandas.DataFrame.index "Link to this definition")

The index (row labels) of the DataFrame.

The index of a DataFrame is a series of labels that identify each row. The labels can be integers, strings, or any other hashable type. The index is used for label-based access and alignment, and can be accessed or modified using this attribute.

Returns:

pandas.Index

The index labels of the DataFrame.

See also

[`DataFrame.columns`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.columns.html#pandas.DataFrame.columns "pandas.DataFrame.columns")

The column labels of the DataFrame.

[`DataFrame.to_numpy`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_numpy.html#pandas.DataFrame.to_numpy "pandas.DataFrame.to_numpy")

Convert the DataFrame to a NumPy array.

Examples

\>>> df \= pd.DataFrame({'Name': \['Alice', 'Bob', 'Aritra'\],
...                    'Age': \[25, 30, 35\],
...                    'Location': \['Seattle', 'New York', 'Kona'\]},
...                   index\=(\[10, 20, 30\]))
\>>> df.index
Index(\[10, 20, 30\], dtype='int64')

Copy to clipboard

In this example, we create a DataFrame with 3 rows and 3 columns, including Name, Age, and Location information. We set the index labels to be the integers 10, 20, and 30. We then access the index attribute of the DataFrame, which returns an Index object containing the index labels.

\>>> df.index \= \[100, 200, 300\]
\>>> df
    Name  Age Location
100  Alice   25  Seattle
200    Bob   30 New York
300  Aritra  35    Kona

Copy to clipboard

In this example, we modify the index labels of the DataFrame by assigning a new list of labels to the index attribute. The DataFrame is then updated with the new labels, and the output shows the modified DataFrame.

On this page