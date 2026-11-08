[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.hide.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.io.formats.style.Styler.hide.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.hide.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.io.formats.style.Styler.hide.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.io.formats.style.Styler.hide.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.io.formats.style.Styler.hide.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.io.formats.style.Styler.hide.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.io.formats.style.Styler.hide.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.io.formats.style.Styler.hide.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.io.formats.style.Styler.hide.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.io.formats.style.Styler.hide.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.io.formats.style.Styler.hide.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.io.formats.style.Styler.hide.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.io.formats.style.Styler.hide.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.formats.style.Styler.hide[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.hide.html#pandas-io-formats-style-styler-hide "Link to this heading")

=========================================================================================================================================================================================

Styler.hide(_subset\=None_, _axis\=0_, _level\=None_, _names\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/formats/style.py#L2904-L3109)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.hide.html#pandas.io.formats.style.Styler.hide "Link to this definition")

Hide the entire index / column headers, or specific rows / columns from display.

This method controls the visibility of rows, columns, and axis headers in the rendered output. It can hide the entire index or column headers, specific levels of a MultiIndex, individual data rows or columns, or just the axis-level names, depending on the combination of arguments provided.

Parameters:

**subset**label, array-like, IndexSlice, optional

A valid 1d input or single key along the axis within DataFrame.loc\[<subset>, :\] or DataFrame.loc\[:, <subset>\] depending upon `axis`, to limit `data` to select hidden rows / columns.

**axis**{“index”, 0, “columns”, 1}

Apply to the index or columns.

**level**int, str, list

The level(s) to hide in a MultiIndex if hiding the entire index / column headers. Cannot be used simultaneously with `subset`.

**names**bool

Whether to hide the level name(s) of the index / columns headers in the case it (or at least one the levels) remains visible.

Returns:

Styler

Instance of class with specified headers/rows/columns hidden from display.

See also

[`Styler.apply`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.apply.html#pandas.io.formats.style.Styler.apply "pandas.io.formats.style.Styler.apply")

Apply a CSS-styling function column-wise, row-wise, or table-wise.

[`Styler.map`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.map.html#pandas.io.formats.style.Styler.map "pandas.io.formats.style.Styler.map")

Apply a CSS-styling function elementwise.

Notes

Warning

This method only works with the output methods `to_html`, `to_string`, `to_latex` and `to_typst`.

Other output methods, including `to_excel`, ignore this hiding method and will display all data.

This method has multiple functionality depending upon the combination of the `subset`, `level` and `names` arguments (see examples). The `axis` argument is used only to control whether the method is applied to row or column headers:

|     |     |     |     |
| --- | --- | --- | --- |Argument combinations[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.hide.html#id1 "Link to this table")
    
| `subset` | `level` | `names` | Effect |
| --- | --- | --- | --- |
| None | None | False | The axis-Index is hidden entirely. |
| None | None | True | Only the axis-Index names are hidden. |
| None | Int, Str, List | False | Specified axis-MultiIndex levels are hidden entirely. |
| None | Int, Str, List | True | Specified axis-MultiIndex levels are hidden entirely and the names of remaining axis-MultiIndex levels. |
| Subset | None | False | The specified data rows/columns are hidden, but the axis-Index itself, and names, remain unchanged. |
| Subset | None | True | The specified data rows/columns and axis-Index names are hidden, but the axis-Index itself remains unchanged. |
| Subset | Int, Str, List | Boolean | ValueError: cannot supply `subset` and `level` simultaneously. |

Note this method only hides the identified elements so can be chained to hide multiple elements in sequence.

Examples

Simple application hiding specific rows:

\>>> df \= pd.DataFrame(\[\[1, 2\], \[3, 4\], \[5, 6\]\], index\=\["a", "b", "c"\])
\>>> df.style.hide(\["a", "b"\])
     0    1
c    5    6

Copy to clipboard

Hide the index and retain the data values:

\>>> midx \= pd.MultiIndex.from\_product(\[\["x", "y"\], \["a", "b", "c"\]\])
\>>> df \= pd.DataFrame(np.random.randn(6, 6), index\=midx, columns\=midx)
\>>> df.style.format("{:.1f}").hide()
                 x                    y
   a      b      c      a      b      c
 0.1    0.0    0.4    1.3    0.6   -1.4
 0.7    1.0    1.3    1.5   -0.0   -0.2
 1.4   -0.8    1.6   -0.2   -0.4   -0.3
 0.4    1.0   -0.2   -0.8   -1.2    1.1
\-0.6    1.2    1.8    1.9    0.3    0.3
 0.8    0.5   -0.3    1.2    2.2   -0.8

Copy to clipboard

Hide specific rows in a MultiIndex but retain the index:

\>>> df.style.format("{:.1f}").hide(subset\=(slice(None), \["a", "c"\]))
...
                         x                    y
           a      b      c      a      b      c
x   b    0.7    1.0    1.3    1.5   -0.0   -0.2
y   b   -0.6    1.2    1.8    1.9    0.3    0.3

Copy to clipboard

Hide specific rows and the index through chaining:

\>>> df.style.format("{:.1f}").hide(subset\=(slice(None), \["a", "c"\])).hide()
...
                 x                    y
   a      b      c      a      b      c
 0.7    1.0    1.3    1.5   -0.0   -0.2
\-0.6    1.2    1.8    1.9    0.3    0.3

Copy to clipboard

Hide a specific level:

\>>> df.style.format("{:,.1f}").hide(level\=1)
                     x                    y
       a      b      c      a      b      c
x    0.1    0.0    0.4    1.3    0.6   -1.4
     0.7    1.0    1.3    1.5   -0.0   -0.2
     1.4   -0.8    1.6   -0.2   -0.4   -0.3
y    0.4    1.0   -0.2   -0.8   -1.2    1.1
    -0.6    1.2    1.8    1.9    0.3    0.3
     0.8    0.5   -0.3    1.2    2.2   -0.8

Copy to clipboard

Hiding just the index level names:

\>>> df.index.names \= \["lev0", "lev1"\]
\>>> df.style.format("{:,.1f}").hide(names\=True)
                         x                    y
           a      b      c      a      b      c
x   a    0.1    0.0    0.4    1.3    0.6   -1.4
    b    0.7    1.0    1.3    1.5   -0.0   -0.2
    c    1.4   -0.8    1.6   -0.2   -0.4   -0.3
y   a    0.4    1.0   -0.2   -0.8   -1.2    1.1
    b   -0.6    1.2    1.8    1.9    0.3    0.3
    c    0.8    0.5   -0.3    1.2    2.2   -0.8

Copy to clipboard

Examples all produce equivalently transposed effects with `axis="columns"`.

On this page