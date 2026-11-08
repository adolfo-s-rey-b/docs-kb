[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.combine_first.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.combine_first.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.combine_first.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.combine_first.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.combine_first.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.combine_first.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.combine_first.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.combine_first.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.combine_first.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.combine_first.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.combine_first.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.combine_first.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.combine_first.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.combine_first.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.combine\_first[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.combine_first.html#pandas-dataframe-combine-first "Link to this heading")

===========================================================================================================================================================================

DataFrame.combine\_first(_other_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L13318-L13392)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.combine_first.html#pandas.DataFrame.combine_first "Link to this definition")

Update null elements with value in the same location in other.

Combine two DataFrame objects by filling null values in one DataFrame with non-null values from other DataFrame. The row and column indexes of the resulting DataFrame will be the union of the two. The resulting dataframe contains the ‘first’ dataframe values and overrides the second one values where both first.loc\[index, col\] and second.loc\[index, col\] are not missing values, upon calling first.combine\_first(second).

Parameters:

**other**DataFrame

Provided DataFrame to use to fill null values.

Returns:

DataFrame

The result of combining the provided DataFrame with the other object.

See also

[`DataFrame.combine`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.combine.html#pandas.DataFrame.combine "pandas.DataFrame.combine")

Perform series-wise operation on two DataFrames using a given function.

Examples

\>>> df1 \= pd.DataFrame({"A": \[None, 0\], "B": \[None, 4\]})
\>>> df2 \= pd.DataFrame({"A": \[1, 1\], "B": \[3, 3\]})
\>>> df1.combine\_first(df2)
     A    B
0  1.0  3.0
1  0.0  4.0

Copy to clipboard

Null values still persist if the location of that null value does not exist in other

\>>> df1 \= pd.DataFrame({"A": \[None, 0\], "B": \[4, None\]})
\>>> df2 \= pd.DataFrame({"B": \[3, 3\], "C": \[1, 1\]}, index\=\[1, 2\])
\>>> df1.combine\_first(df2)
     A    B    C
0  NaN  4.0  NaN
1  0.0  3.0  1.0
2  NaN  3.0  1.0

Copy to clipboard

On this page