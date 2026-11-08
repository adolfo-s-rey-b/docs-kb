[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.info[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html#pandas-dataframe-info "Link to this heading")

===============================================================================================================================================

DataFrame.info(_verbose\=None_, _buf\=None_, _max\_cols\=None_, _memory\_usage\=None_, _show\_counts\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L3756-L3916)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html#pandas.DataFrame.info "Link to this definition")

Print a concise summary of a DataFrame.

This method prints information about a DataFrame including the index dtype and columns, non-NA values and memory usage.

Parameters:

**verbose**bool, optional

Whether to print the full summary. By default, the setting in `pandas.options.display.max_info_columns` is followed.

**buf**writable buffer, defaults to sys.stdout

Where to send the output. By default, the output is printed to sys.stdout. Pass a writable buffer if you need to further process the output.

**max\_cols**int, optional

When to switch from the verbose to the truncated output. If the DataFrame has more than max\_cols columns, the truncated output is used. By default, the setting in `pandas.options.display.max_info_columns` is used.

**memory\_usage**bool, str, optional

Specifies whether total memory usage of the DataFrame elements (including the index) should be displayed. By default, this follows the `pandas.options.display.memory_usage` setting.

True always show memory usage. False never shows memory usage. A value of ‘deep’ is equivalent to “True with deep introspection”. Memory usage is shown in human-readable units (base-2 representation). Without deep introspection a memory estimation is made based in column dtype and number of rows assuming values consume the same memory amount for corresponding dtypes. With deep memory introspection, a real memory usage calculation is performed at the cost of computational resources. See the [Frequently Asked Questions](https://pandas.pydata.org/docs/user_guide/gotchas.html#df-memory-usage)
 for more details.

**show\_counts**bool, optional

Whether to show the non-null counts. By default, this is shown only if the DataFrame is smaller than `pandas.options.display.max_info_rows` and `pandas.options.display.max_info_columns`. A value of True always shows the counts, and False never shows the counts.

Returns:

None

This method prints a summary of a DataFrame and returns None.

See also

[`DataFrame.describe`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html#pandas.DataFrame.describe "pandas.DataFrame.describe")

Generate descriptive statistics of DataFrame columns.

[`DataFrame.memory_usage`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.memory_usage.html#pandas.DataFrame.memory_usage "pandas.DataFrame.memory_usage")

Memory usage of DataFrame columns.

Examples

\>>> int\_values \= \[1, 2, 3, 4, 5\]
\>>> text\_values \= \["alpha", "beta", "gamma", "delta", "epsilon"\]
\>>> float\_values \= \[0.0, 0.25, 0.5, 0.75, 1.0\]
\>>> df \= pd.DataFrame(
...     {
...         "int\_col": int\_values,
...         "text\_col": text\_values,
...         "float\_col": float\_values,
...     }
... )
\>>> df
    int\_col text\_col  float\_col
0        1    alpha       0.00
1        2     beta       0.25
2        3    gamma       0.50
3        4    delta       0.75
4        5  epsilon       1.00

Copy to clipboard

Prints information of all columns:

\>>> df.info(verbose\=True)
<class 'pandas.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 3 columns):
 #   Column     Non-Null Count  Dtype
\---  ------     --------------  -----
 0   int\_col    5 non-null      int64
 1   text\_col   5 non-null      str
 2   float\_col  5 non-null      float64
dtypes: float64(1), int64(1), str(1)
memory usage: 278.0 bytes

Copy to clipboard

Prints a summary of columns count and its dtypes but not per column information:

\>>> df.info(verbose\=False)
<class 'pandas.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Columns: 3 entries, int\_col to float\_col
dtypes: float64(1), int64(1), str(1)
memory usage: 278.0 bytes

Copy to clipboard

Pipe output of DataFrame.info to buffer instead of sys.stdout, get buffer content and writes to a text file:

\>>> import io
\>>> buffer \= io.StringIO()
\>>> df.info(buf\=buffer)
\>>> s \= buffer.getvalue()
\>>> with open("df\_info.txt", "w", encoding\="utf-8") as f:
...     f.write(s)
260

Copy to clipboard

The memory\_usage parameter allows deep introspection mode, specially useful for big DataFrames and fine-tune memory optimization:

\>>> random\_strings\_array \= np.random.choice(\["a", "b", "c"\], 10\*\*6)
\>>> df \= pd.DataFrame(
...     {
...         "column\_1": np.random.choice(\["a", "b", "c"\], 10\*\*6),
...         "column\_2": np.random.choice(\["a", "b", "c"\], 10\*\*6),
...         "column\_3": np.random.choice(\["a", "b", "c"\], 10\*\*6),
...     }
... )
\>>> df.info()
<class 'pandas.DataFrame'>
RangeIndex: 1000000 entries, 0 to 999999
Data columns (total 3 columns):
 #   Column    Non-Null Count    Dtype
\---  ------    --------------    -----
 0   column\_1  1000000 non-null  str
 1   column\_2  1000000 non-null  str
 2   column\_3  1000000 non-null  str
dtypes: str(3)
memory usage: 25.7 MB

Copy to clipboard

\>>> df.info(memory\_usage\="deep")
<class 'pandas.DataFrame'>
RangeIndex: 1000000 entries, 0 to 999999
Data columns (total 3 columns):
 #   Column    Non-Null Count    Dtype
\---  ------    --------------    -----
 0   column\_1  1000000 non-null  str
 1   column\_2  1000000 non-null  str
 2   column\_3  1000000 non-null  str
dtypes: str(3)
memory usage: 25.7 MB

Copy to clipboard

On this page