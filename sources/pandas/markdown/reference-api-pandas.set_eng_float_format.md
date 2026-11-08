[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.set_eng_float_format.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.set\_eng\_float\_format[#](https://pandas.pydata.org/docs/reference/api/pandas.set_eng_float_format.html#pandas-set-eng-float-format "Link to this heading")

====================================================================================================================================================================

pandas.set\_eng\_float\_format(_accuracy\=3_, _use\_eng\_prefix\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/formats/format.py#L1975-L2028)
[#](https://pandas.pydata.org/docs/reference/api/pandas.set_eng_float_format.html#pandas.set_eng_float_format "Link to this definition")

Format float representation in DataFrame with SI notation.

Deprecated since version 3.1.0: Use `pd.set_option("display.precision", N)` to control decimal precision, or pass a custom callable to `pd.set_option("display.float_format", func)`.

Sets the floating-point display format for `DataFrame` objects using engineering notation (SI units), allowing easier readability of values across wide ranges.

Parameters:

**accuracy**int, default 3

Number of decimal digits after the floating point.

**use\_eng\_prefix**bool, default False

Whether to represent a value with SI prefixes.

Returns:

None

This method does not return a value. it updates the global display format for floats in DataFrames.

See also

[`set_option`](https://pandas.pydata.org/docs/reference/api/pandas.set_option.html#pandas.set_option "pandas.set_option")

Set the value of the specified option or options.

[`reset_option`](https://pandas.pydata.org/docs/reference/api/pandas.reset_option.html#pandas.reset_option "pandas.reset_option")

Reset one or more options to their default value.

Examples

Use `pd.set_option("display.precision", N)` to control decimal precision instead:

\>>> with pd.option\_context("display.precision", 3):
...     print(pd.DataFrame(\[1e-9, 1e-3, 1, 1e3, 1e6\]))
           0
0  1.000e-09
1  1.000e-03
2  1.000e+00
3  1.000e+03
4  1.000e+06

Copy to clipboard

On this page