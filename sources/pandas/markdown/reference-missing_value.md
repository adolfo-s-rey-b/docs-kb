[Skip to main content](https://pandas.pydata.org/docs/reference/missing_value.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

Missing values[#](https://pandas.pydata.org/docs/reference/missing_value.html#missing-values "Link to this heading")

=====================================================================================================================

Note

For an overview, see [Working with missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html#missing-data)
.

NA is the way to represent missing values for nullable dtypes (see below):

|     |     |
| --- | --- |
| [`NA`](https://pandas.pydata.org/docs/reference/api/pandas.NA.html#pandas.NA "pandas.NA") | NA ("not available") missing value indicator. |

NaT is the missing value for timedelta and datetime data (see below):

|     |     |
| --- | --- |
| [`NaT`](https://pandas.pydata.org/docs/reference/api/pandas.NaT.html#pandas.NaT "pandas.NaT") | (N)ot-(A)-(T)ime, the time equivalent of NaN. |