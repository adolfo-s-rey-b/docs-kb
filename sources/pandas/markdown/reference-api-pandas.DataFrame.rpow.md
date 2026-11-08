[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rpow.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.rpow.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rpow.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.rpow.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.rpow.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.rpow.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.rpow.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.rpow.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.rpow.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.rpow.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.rpow.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.rpow.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.rpow.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.rpow.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.rpow[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rpow.html#pandas-dataframe-rpow "Link to this heading")

===============================================================================================================================================

DataFrame.rpow(_other_, _axis\='columns'_, _level\=None_, _fill\_value\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L12877-L12968)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rpow.html#pandas.DataFrame.rpow "Link to this definition")

Get Exponential power of dataframe and other, element-wise (binary operator rpow).

Equivalent to `other ** dataframe`, but with support to substitute a fill\_value for missing data in one of the inputs. With reverse version, pow.

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
...                    'degrees': \[3, 1, 3\]},
...                   index\=\['circle', 'triangle', 'rectangle'\])
\>>> df
           angles  degrees
circle          0        3
triangle        3        1
rectangle       4        3

Copy to clipboard

Calculate exponential power with a scalar.

\>>> 2 \*\* df
           angles  degrees
circle          1        8
triangle        8        2
rectangle      16        8

Copy to clipboard

\>>> df.rpow(2)
           angles  degrees
circle          1        8
triangle        8        2
rectangle      16        8

Copy to clipboard

Calculate exponential power with a list.

\>>> \[2, 3\] \*\* df
           angles  degrees
circle          1       27
triangle        8        3
rectangle      16       27

Copy to clipboard

\>>> df.rpow(\[2, 3\], axis\='columns')
           angles  degrees
circle          1       27
triangle        8        3
rectangle      16       27

Copy to clipboard

On this page