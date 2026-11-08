[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.NA.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.NA[#](https://pandas.pydata.org/docs/reference/api/pandas.NA.html#pandas-na "Link to this heading")

===========================================================================================================

pandas.NA \= <NA>[#](https://pandas.pydata.org/docs/reference/api/pandas.NA.html#pandas.NA "Link to this definition")

NA (“not available”) missing value indicator.

Warning

Experimental: the behaviour of NA can still change without warning.

The NA singleton is a missing value indicator defined by pandas. It is used in certain new extension dtypes (currently the “string” dtype).

See also

[`numpy.nan`](https://numpy.org/doc/stable/reference/constants.html#numpy.nan "(in NumPy v2.5)")

Floating point representation of Not a Number (NaN) for numerical data.

[`isna`](https://pandas.pydata.org/docs/reference/api/pandas.isna.html#pandas.isna "pandas.isna")

Detect missing values for an array-like object.

[`notna`](https://pandas.pydata.org/docs/reference/api/pandas.notna.html#pandas.notna "pandas.notna")

Detect non-missing values for an array-like object.

[`DataFrame.fillna`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html#pandas.DataFrame.fillna "pandas.DataFrame.fillna")

Fill missing values in a DataFrame.

[`Series.fillna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.fillna.html#pandas.Series.fillna "pandas.Series.fillna")

Fill missing values in a Series.

Examples

\>>> pd.NA
<NA>

Copy to clipboard

\>>> True | pd.NA
True

Copy to clipboard

\>>> True & pd.NA
<NA>

Copy to clipboard

\>>> pd.NA != pd.NA
<NA>

Copy to clipboard

\>>> pd.NA \== pd.NA
<NA>

Copy to clipboard

\>>> True | pd.NA
True

Copy to clipboard

On this page