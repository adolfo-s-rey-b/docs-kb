[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.format_index.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.io.formats.style.Styler.format_index.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.format_index.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.io.formats.style.Styler.format_index.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.io.formats.style.Styler.format_index.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.io.formats.style.Styler.format_index.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.io.formats.style.Styler.format_index.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.io.formats.style.Styler.format_index.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.io.formats.style.Styler.format_index.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.io.formats.style.Styler.format_index.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.io.formats.style.Styler.format_index.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.io.formats.style.Styler.format_index.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.io.formats.style.Styler.format_index.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.io.formats.style.Styler.format_index.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.formats.style.Styler.format\_index[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.format_index.html#pandas-io-formats-style-styler-format-index "Link to this heading")

==================================================================================================================================================================================================================

Styler.format\_index(_formatter\=None_, _axis\=0_, _level\=None_, _na\_rep\=None_, _precision\=None_, _decimal\='.'_, _thousands\=None_, _escape\=None_, _hyperlinks\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/formats/style_render.py#L1276-L1468)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.format_index.html#pandas.io.formats.style.Styler.format_index "Link to this definition")

Format the text display value of index labels or column headers.

This method assigns a formatting function to the index or column header labels of the DataFrame, similar to [`Styler.format()`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.format.html#pandas.io.formats.style.Styler.format "pandas.io.formats.style.Styler.format")
 but applied to the axis labels rather than the data cells. It supports the same formatter types: callables, format strings, and dicts keyed by MultiIndex level.

Parameters:

**formatter**str, callable, dict or None

Object to define how values are displayed. See notes.

**axis**{0, “index”, 1, “columns”}

Whether to apply the formatter to the index or column headers.

**level**int, str, list

The level(s) over which to apply the generic formatter.

**na\_rep**str, optional

Representation for missing values. If `na_rep` is None, no special formatting is applied.

**precision**int, optional

Floating point precision to use for display purposes, if not determined by the specified `formatter`.

**decimal**str, default “.”

Character used as decimal separator for floats, complex and integers.

**thousands**str, optional, default None

Character used as thousands separator for floats, complex and integers.

**escape**str, optional

Use ‘html’ to replace the characters `&`, `<`, `>`, `'`, and `"` in cell display string with HTML-safe sequences. Use ‘latex’ to replace the characters `&`, `%`, `$`, `#`, `_`, `{`, `}`, `~`, `^`, and `\` in the cell display string with LaTeX-safe sequences. Escaping is done before `formatter`.

**hyperlinks**{“html”, “latex”}, optional

Convert string patterns containing [https://](https://)
, [http://](http://)
, [ftp://](ftp://)
 or www. to HTML <a> tags as clickable URL hyperlinks if “html”, or LaTeX href commands if “latex”.

Returns:

Styler

Returns itself for chaining.

See also

[`Styler.format`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.format.html#pandas.io.formats.style.Styler.format "pandas.io.formats.style.Styler.format")

Format the text display value of data cells.

Notes

This method assigns a formatting function, `formatter`, to each level label in the DataFrame’s index or column headers. If `formatter` is `None`, then the default formatter is used. If a callable then that function should take a label value as input and return a displayable representation, such as a string. If `formatter` is given as a string this is assumed to be a valid Python format specification and is wrapped to a callable as `string.format(x)`. If a `dict` is given, keys should correspond to MultiIndex level numbers or names, and values should be string or callable, as above.

The default formatter currently expresses floats and complex numbers with the pandas display precision unless using the `precision` argument here. The default formatter does not adjust the representation of missing values unless the `na_rep` argument is used.

The `level` argument defines which levels of a MultiIndex to apply the method to. If the `formatter` argument is given in dict form but does not include all levels within the level argument then these unspecified levels will have the default formatter applied. Any levels in the formatter dict specifically excluded from the level argument will be ignored.

When using a `formatter` string the dtypes must be compatible, otherwise a ValueError will be raised.

Warning

Styler.format\_index is ignored when using the output format Styler.to\_excel, since Excel and Python have inherently different formatting structures. However, it is possible to use the number-format pseudo CSS attribute to force Excel permissible formatting. See documentation for Styler.format.

Examples

Using `na_rep` and `precision` with the default `formatter`

\>>> df \= pd.DataFrame(\[\[1, 2, 3\]\], columns\=\[2.0, np.nan, 4.0\])
\>>> df.style.format\_index(axis\=1, na\_rep\='MISS', precision\=3)
    2.000    MISS   4.000
0       1       2       3

Copy to clipboard

Using a `formatter` specification on consistent dtypes in a level

\>>> df.style.format\_index('{:.2f}', axis\=1, na\_rep\='MISS')
     2.00   MISS    4.00
0       1      2       3

Copy to clipboard

Using the default `formatter` for unspecified levels

\>>> df \= pd.DataFrame(\[\[1, 2, 3\]\],
...                   columns\=pd.MultiIndex.from\_arrays(
...                   \[\["a", "a", "b"\], \[2, np.nan, 4\]\]))
\>>> df.style.format\_index({0: lambda v: v.upper()}, axis\=1, precision\=1)
...
               A       B
      2.0    nan     4.0
0       1      2       3

Copy to clipboard

Using a callable `formatter` function.

\>>> func \= lambda s: 'STRING' if isinstance(s, str) else 'FLOAT'
\>>> df.style.format\_index(func, axis\=1, na\_rep\='MISS')
...
          STRING  STRING
    FLOAT   MISS   FLOAT
0       1      2       3

Copy to clipboard

Using a `formatter` with HTML `escape` and `na_rep`.

\>>> df \= pd.DataFrame(\[\[1, 2, 3\]\], columns\=\['"A"', 'A&B', None\])
\>>> s \= df.style.format\_index('$ {0}', axis\=1, escape\="html", na\_rep\="NA")
...
<th .. >$ &#34;A&#34;</th>
<th .. >$ A&amp;B</th>
<th .. >NA</td>
...

Copy to clipboard

Using a `formatter` with LaTeX `escape`.

\>>> df \= pd.DataFrame(\[\[1, 2, 3\]\], columns\=\["123", "~", "$%#"\])
\>>> df.style.format\_index("\\\\textbf{{{}}}", escape\="latex", axis\=1).to\_latex()
...
\\begin{tabular}{lrrr}
{} & {\\textbf{123}} & {\\textbf{\\textasciitilde }} & {\\textbf{\\$\\%\\#}} \\\\
0 & 1 & 2 & 3 \\\\
\\end{tabular}

Copy to clipboard

On this page