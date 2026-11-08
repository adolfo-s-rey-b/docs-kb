[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.equals.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.equals.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.equals.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.equals.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.equals.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.equals.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.equals.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.equals.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.equals.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.equals.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.equals.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.equals.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.equals.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.equals.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.equals[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.equals.html#pandas-dataframe-equals "Link to this heading")

=====================================================================================================================================================

DataFrame.equals(_other_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L1255-L1350)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.equals.html#pandas.DataFrame.equals "Link to this definition")

Test whether two objects contain the same elements.

This function allows two Series or DataFrames to be compared against each other to see if they have the same shape and elements. NaNs in the same location are considered equal.

The row/column index do not need to have the same type, as long as the values are considered equal. Corresponding columns and index must be of the same dtype.

Parameters:

**other**Series or DataFrame

The other Series or DataFrame to be compared with the first.

Returns:

bool

True if all elements are the same in both objects, False otherwise.

See also

[`Series.eq`](https://pandas.pydata.org/docs/reference/api/pandas.Series.eq.html#pandas.Series.eq "pandas.Series.eq")

Compare two Series objects of the same length and return a Series where each element is True if the element in each Series is equal, False otherwise.

[`DataFrame.eq`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.eq.html#pandas.DataFrame.eq "pandas.DataFrame.eq")

Compare two DataFrame objects of the same shape and return a DataFrame where each element is True if the respective element in each DataFrame is equal, False otherwise.

[`testing.assert_series_equal`](https://pandas.pydata.org/docs/reference/api/pandas.testing.assert_series_equal.html#pandas.testing.assert_series_equal "pandas.testing.assert_series_equal")

Raises an AssertionError if left and right are not equal. Provides an easy interface to ignore inequality in dtypes, indexes and precision among others.

[`testing.assert_frame_equal`](https://pandas.pydata.org/docs/reference/api/pandas.testing.assert_frame_equal.html#pandas.testing.assert_frame_equal "pandas.testing.assert_frame_equal")

Like assert\_series\_equal, but targets DataFrames.

[`numpy.array_equal`](https://numpy.org/doc/stable/reference/generated/numpy.array_equal.html#numpy.array_equal "(in NumPy v2.5)")

Return True if two arrays have the same shape and elements, False otherwise.

Examples

\>>> df \= pd.DataFrame({1: \[10\], 2: \[20\]})
\>>> df
    1   2
0  10  20

Copy to clipboard

DataFrames df and exactly\_equal have the same types and values for their elements and column labels, which will return True.

\>>> exactly\_equal \= pd.DataFrame({1: \[10\], 2: \[20\]})
\>>> exactly\_equal
    1   2
0  10  20
\>>> df.equals(exactly\_equal)
True

Copy to clipboard

DataFrames df and different\_column\_type have the same element types and values, but have different types for the column labels, which will still return True.

\>>> different\_column\_type \= pd.DataFrame({1.0: \[10\], 2.0: \[20\]})
\>>> different\_column\_type
   1.0  2.0
0   10   20
\>>> df.equals(different\_column\_type)
True

Copy to clipboard

DataFrames df and different\_data\_type have different types for the same values for their elements, and will return False even though their column labels are the same values and types.

\>>> different\_data\_type \= pd.DataFrame({1: \[10.0\], 2: \[20.0\]})
\>>> different\_data\_type
      1     2
0  10.0  20.0
\>>> df.equals(different\_data\_type)
False

Copy to clipboard

DataFrames with NaN in the same locations compare equal.

\>>> df\_nan1 \= pd.DataFrame({"a": \[1, np.nan\], "b": \[3, np.nan\]})
\>>> df\_nan2 \= pd.DataFrame({"a": \[1, np.nan\], "b": \[3, np.nan\]})
\>>> df\_nan1.equals(df\_nan2)
True

Copy to clipboard

If the NaN values are not in the same locations, they compare unequal.

\>>> df\_nan3 \= pd.DataFrame({"a": \[1, np.nan\], "b": \[3, 4\]})
\>>> df\_nan1.equals(df\_nan3)
False

Copy to clipboard

On this page