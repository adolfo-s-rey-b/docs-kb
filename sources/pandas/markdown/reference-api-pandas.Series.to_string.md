[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_string.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.to_string.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_string.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.to_string.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.to_string.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.to_string.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.to_string.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.to_string.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.to_string.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.to_string.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.to_string.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.to_string.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.to_string.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.to_string.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.to\_string[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_string.html#pandas-series-to-string "Link to this heading")

======================================================================================================================================================

Series.to\_string(_buf\=None_, _\*_, _na\_rep\='NaN'_, _float\_format\=None_, _header\=True_, _index\=True_, _length\=False_, _dtype\=False_, _name\=False_, _max\_rows\=None_, _min\_rows\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L1650-L1745)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_string.html#pandas.Series.to_string "Link to this definition")

Render a string representation of the Series.

Produces a human-readable text format of the Series, including optional display of the index, data types, name, and length. The output can be written to a buffer or returned as a string.

Parameters:

**buf**StringIO-like, optional

Buffer to write to.

**na\_rep**str, default ‘NaN’

String representation of NaN to use.

**float\_format**one-parameter function, optional

Formatter function to apply to columns’ elements if they are floats, default None.

**header**bool, default True

Add the Series header (index name).

**index**bool, default True

Add index (row) labels.

**length**bool, default False

Add the Series length.

**dtype**bool, default False

Add the Series dtype.

**name**bool, default False

Add the Series name if not None.

**max\_rows**int, optional

Maximum number of rows to show before truncating. If None, show all.

**min\_rows**int, optional

The number of rows to display in a truncated repr (when number of rows is above max\_rows).

Returns:

str or None

String representation of Series if `buf=None`, otherwise None.

See also

[`Series.to_dict`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_dict.html#pandas.Series.to_dict "pandas.Series.to_dict")

Convert Series to dict object.

[`Series.to_frame`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_frame.html#pandas.Series.to_frame "pandas.Series.to_frame")

Convert Series to DataFrame object.

[`Series.to_markdown`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_markdown.html#pandas.Series.to_markdown "pandas.Series.to_markdown")

Print Series in Markdown-friendly format.

[`Series.to_timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_timestamp.html#pandas.Series.to_timestamp "pandas.Series.to_timestamp")

Cast to DatetimeIndex of Timestamps.

Examples

\>>> ser \= pd.Series(\[1, 2, 3\]).to\_string()
\>>> ser
'0    1\\n1    2\\n2    3'

Copy to clipboard

On this page