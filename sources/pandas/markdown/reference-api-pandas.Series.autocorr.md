[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.autocorr.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.autocorr.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.autocorr.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.autocorr.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.autocorr.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.autocorr.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.autocorr.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.autocorr.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.autocorr.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.autocorr.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.autocorr.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.autocorr.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.autocorr.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.autocorr.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.autocorr[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.autocorr.html#pandas-series-autocorr "Link to this heading")

==================================================================================================================================================

Series.autocorr(_lag\=1_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L3356-L3399)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.autocorr.html#pandas.Series.autocorr "Link to this definition")

Compute the lag-N autocorrelation.

This method computes the Pearson correlation between the Series and its shifted self.

Parameters:

**lag**int, default 1

Number of lags to apply before performing autocorrelation.

Returns:

float

The Pearson correlation between self and self.shift(lag).

See also

[`Series.corr`](https://pandas.pydata.org/docs/reference/api/pandas.Series.corr.html#pandas.Series.corr "pandas.Series.corr")

Compute the correlation between two Series.

[`Series.shift`](https://pandas.pydata.org/docs/reference/api/pandas.Series.shift.html#pandas.Series.shift "pandas.Series.shift")

Shift index by desired number of periods.

[`DataFrame.corr`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html#pandas.DataFrame.corr "pandas.DataFrame.corr")

Compute pairwise correlation of columns.

[`DataFrame.corrwith`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corrwith.html#pandas.DataFrame.corrwith "pandas.DataFrame.corrwith")

Compute pairwise correlation between rows or columns of two DataFrame objects.

Notes

If the Pearson correlation is not well defined return ‘NaN’.

Examples

\>>> s \= pd.Series(\[0.25, 0.5, 0.2, \-0.05\])
\>>> s.autocorr()
0.10355...
\>>> s.autocorr(lag\=2)
\-0.99999...

Copy to clipboard

If the Pearson correlation is not well defined, then ‘NaN’ is returned.

\>>> s \= pd.Series(\[1, 0, 0, 0\])
\>>> s.autocorr()
nan

Copy to clipboard

On this page