[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.NaT.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.NaT[#](https://pandas.pydata.org/docs/reference/api/pandas.NaT.html#pandas-nat "Link to this heading")

==============================================================================================================

pandas.NaT \= NaT[#](https://pandas.pydata.org/docs/reference/api/pandas.NaT.html#pandas.NaT "Link to this definition")

(N)ot-(A)-(T)ime, the time equivalent of NaN.

NaT is used to denote missing or null values in datetime and timedelta objects in pandas. It functions similarly to how NaN is used for numerical data. Operations with NaT will generally propagate the NaT value, similar to NaN. NaT can be used in pandas data structures like Series and DataFrame to represent missing datetime values. It is useful in data analysis and time series analysis when working with incomplete or sparse time-based data. Pandas provides robust handling of NaT to ensure consistency and reliability in computations involving datetime objects.

See also

[`NA`](https://pandas.pydata.org/docs/reference/api/pandas.NA.html#pandas.NA "pandas.NA")

NA (“not available”) missing value indicator.

[`isna`](https://pandas.pydata.org/docs/reference/api/pandas.isna.html#pandas.isna "pandas.isna")

Detect missing values (NaN or NaT) in an array-like object.

[`notna`](https://pandas.pydata.org/docs/reference/api/pandas.notna.html#pandas.notna "pandas.notna")

Detect non-missing values.

[`numpy.nan`](https://numpy.org/doc/stable/reference/constants.html#numpy.nan "(in NumPy v2.5)")

Floating point representation of Not a Number (NaN) for numerical data.

Examples

\>>> pd.DataFrame(\[pd.Timestamp("2023"), np.nan\], columns\=\["col\_1"\])
        col\_1
0  2023-01-01
1         NaT

Copy to clipboard

On this page