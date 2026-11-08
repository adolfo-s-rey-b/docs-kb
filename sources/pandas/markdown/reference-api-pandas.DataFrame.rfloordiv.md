[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rfloordiv.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.rfloordiv[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rfloordiv.html#pandas-dataframe-rfloordiv "Link to this heading")

==============================================================================================================================================================

DataFrame.rfloordiv(_other_, _axis\='columns'_, _level\=None_, _fill\_value\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L12505-L12596)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rfloordiv.html#pandas.DataFrame.rfloordiv "Link to this definition")

Get Integer division of dataframe and other, element-wise (binary operator rfloordiv).

Equivalent to `other // dataframe`, but with support to substitute a fill\_value for missing data in one of the inputs. With reverse version, floordiv.

Among flexible wrappers (add, sub, mul, div, floordiv, mod, pow) to arithmetic operators: +, \-, \*, /, //, %, \*\*.

Parameters:

**other**scalar, sequence, Series, dict or DataFrame

Any single or multiple element data structure, or list-like object.

**axis**{0 or ‘index’, 1 or ‘columns’}

Whether to compare by the index (0 or ‘index’) or columns. (1 or ‘columns’). For Series input, axis to match Series index on.

**level**int or label

Broadcast across a level, matching Index values on the passed MultiIndex level.

**fill\_value**scalar or None, default None

Fill NA values, whether present in the original data or introduced by alignment, with this value before computation. Positions where both inputs are NA are left unfilled and behave as NA does for the operation.

Returns:

DataFrame

Result of the arithmetic operation.

See also

[`DataFrame.add`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.add.html#pandas.DataFrame.add "pandas.DataFrame.add")

Add DataFrames.

[`DataFrame.sub`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sub.html#pandas.DataFrame.sub "pandas.DataFrame.sub")

Subtract DataFrames.

[`DataFrame.mul`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mul.html#pandas.DataFrame.mul "pandas.DataFrame.mul")

Multiply DataFrames.

[`DataFrame.div`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.div.html#pandas.DataFrame.div "pandas.DataFrame.div")

Divide DataFrames (float division).

[`DataFrame.truediv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.truediv.html#pandas.DataFrame.truediv "pandas.DataFrame.truediv")

Divide DataFrames (float division).

[`DataFrame.floordiv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.floordiv.html#pandas.DataFrame.floordiv "pandas.DataFrame.floordiv")

Divide DataFrames (integer division).

[`DataFrame.mod`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mod.html#pandas.DataFrame.mod "pandas.DataFrame.mod")

Calculate modulo (remainder after division).

[`DataFrame.pow`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pow.html#pandas.DataFrame.pow "pandas.DataFrame.pow")

Calculate exponential power.

Notes

Mismatched indices will be unioned together.

Examples

\>>> df \= pd.DataFrame({'angles': \[0, 3, 4\],
...                    'degrees': \[360, 180, 360\]},
...                   index\=\['circle', 'triangle', 'rectangle'\])
\>>> df
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

Copy to clipboard

Divide a scalar.

\>>> 10 // df
           angles  degrees
circle        inf      0.0
triangle      3.0      0.0
rectangle     2.0      0.0

Copy to clipboard

\>>> df.rfloordiv(10)
           angles  degrees
circle        inf      0.0
triangle      3.0      0.0
rectangle     2.0      0.0

Copy to clipboard

Divide a list.

\>>> \[10, 20\] // df
           angles  degrees
circle        inf      0.0
triangle      3.0      0.0
rectangle     2.0      0.0

Copy to clipboard

\>>> df.rfloordiv(\[10, 20\], axis\='columns')
           angles  degrees
circle        inf      0.0
triangle      3.0      0.0
rectangle     2.0      0.0

Copy to clipboard

On this page