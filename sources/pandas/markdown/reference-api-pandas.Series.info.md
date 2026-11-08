[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.info.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.info.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.info.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.info.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.info.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.info.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.info.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.info.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.info.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.info.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.info.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.info.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.info.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.info.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.info[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.info.html#pandas-series-info "Link to this heading")

======================================================================================================================================

Series.info(_verbose\=None_, _buf\=None_, _max\_cols\=None_, _memory\_usage\=None_, _show\_counts\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L6359-L6480)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.info.html#pandas.Series.info "Link to this definition")

Print a concise summary of a Series.

This method prints information about a Series including the index dtype, non-NA values and memory usage.

Parameters:

**verbose**bool, optional

Whether to print the full summary. By default, the setting in `pandas.options.display.max_info_columns` is followed.

**buf**writable buffer, defaults to sys.stdout

Where to send the output. By default, the output is printed to sys.stdout. Pass a writable buffer if you need to further process the output.

**max\_cols**int, optional

Unused, exists only for compatibility with DataFrame.info.

**memory\_usage**bool, str, optional

Specifies whether total memory usage of the Series elements (including the index) should be displayed. By default, this follows the `pandas.options.display.memory_usage` setting.

True always show memory usage. False never shows memory usage. A value of ‘deep’ is equivalent to “True with deep introspection”. Memory usage is shown in human-readable units (base-2 representation). Without deep introspection a memory estimation is made based in column dtype and number of rows assuming values consume the same memory amount for corresponding dtypes. With deep memory introspection, a real memory usage calculation is performed at the cost of computational resources. See the [Frequently Asked Questions](https://pandas.pydata.org/docs/user_guide/gotchas.html#df-memory-usage)
 for more details.

**show\_counts**bool, optional

Whether to show the non-null counts. By default, this is shown only if the DataFrame is smaller than `pandas.options.display.max_info_rows` and `pandas.options.display.max_info_columns`. A value of True always shows the counts, and False never shows the counts.

Returns:

None

This method prints a summary of a Series and returns None.

See also

[`Series.describe`](https://pandas.pydata.org/docs/reference/api/pandas.Series.describe.html#pandas.Series.describe "pandas.Series.describe")

Generate descriptive statistics of Series.

[`Series.memory_usage`](https://pandas.pydata.org/docs/reference/api/pandas.Series.memory_usage.html#pandas.Series.memory_usage "pandas.Series.memory_usage")

Memory usage of Series.

Examples

\>>> int\_values \= \[1, 2, 3, 4, 5\]
\>>> text\_values \= \["alpha", "beta", "gamma", "delta", "epsilon"\]
\>>> s \= pd.Series(text\_values, index\=int\_values)
\>>> s.info()
<class 'pandas.Series'>
Index: 5 entries, 1 to 5
Series name: None
Non-Null Count  Dtype
\--------------  -----
5 non-null      str
dtypes: str(1)
memory usage: 106.0 bytes

Copy to clipboard

Prints a summary excluding information about its values:

\>>> s.info(verbose\=False)
<class 'pandas.Series'>
Index: 5 entries, 1 to 5
dtypes: str(1)
memory usage: 106.0 bytes

Copy to clipboard

Pipe output of Series.info to buffer instead of sys.stdout, get buffer content and writes to a text file:

\>>> import io
\>>> buffer \= io.StringIO()
\>>> s.info(buf\=buffer)
\>>> s \= buffer.getvalue()
\>>> with open("df\_info.txt", "w", encoding\="utf-8") as f:
...     f.write(s)
260

Copy to clipboard

The memory\_usage parameter allows deep introspection mode, specially useful for big Series and fine-tune memory optimization:

\>>> random\_strings\_array \= np.random.choice(\["a", "b", "c"\], 10\*\*6)
\>>> s \= pd.Series(np.random.choice(\["a", "b", "c"\], 10\*\*6))
\>>> s.info()
<class 'pandas.Series'>
RangeIndex: 1000000 entries, 0 to 999999
Series name: None
Non-Null Count    Dtype
\--------------    -----
1000000 non-null  str
dtypes: str(1)
memory usage: 8.6 MB

Copy to clipboard

\>>> s.info(memory\_usage\="deep")
<class 'pandas.Series'>
RangeIndex: 1000000 entries, 0 to 999999
Series name: None
Non-Null Count    Dtype
\--------------    -----
1000000 non-null  str
dtypes: str(1)
memory usage: 8.6 MB

Copy to clipboard

On this page