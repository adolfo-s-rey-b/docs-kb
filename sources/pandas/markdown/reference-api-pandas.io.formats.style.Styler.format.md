[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.format.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.io.formats.style.Styler.format.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.format.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.io.formats.style.Styler.format.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.io.formats.style.Styler.format.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.io.formats.style.Styler.format.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.io.formats.style.Styler.format.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.io.formats.style.Styler.format.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.io.formats.style.Styler.format.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.io.formats.style.Styler.format.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.io.formats.style.Styler.format.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.io.formats.style.Styler.format.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.io.formats.style.Styler.format.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.io.formats.style.Styler.format.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.formats.style.Styler.format[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.format.html#pandas-io-formats-style-styler-format "Link to this heading")

===============================================================================================================================================================================================

Styler.format(_formatter\=None_, _subset\=None_, _na\_rep\=None_, _precision\=None_, _decimal\='.'_, _thousands\=None_, _escape\=None_, _hyperlinks\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/formats/style_render.py#L1013-L1274)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.format.html#pandas.io.formats.style.Styler.format "Link to this definition")

Format the text display value of cells.

This method allows control over how each data cell is displayed by assigning a formatter function or format string. It is particularly useful for adjusting floating point precision, handling missing values, escaping special characters in HTML or LaTeX output, and adding hyperlinks.

Parameters:

**formatter**str, callable, dict or None

Object to define how values are displayed. See notes.

**subset**label, array-like, IndexSlice, optional

A valid 2d input to DataFrame.loc\[<subset>\], or, in the case of a 1d input or single key, to DataFrame.loc\[:, <subset>\] where the columns are prioritised, to limit `data` to _before_ applying the function.

**na\_rep**str, optional

Representation for missing values. If `na_rep` is None, no special formatting is applied.

**precision**int, optional

Floating point precision to use for display purposes, if not determined by the specified `formatter`.

**decimal**str, default “.”

Character used as decimal separator for floats, complex and integers.

**thousands**str, optional, default None

Character used as thousands separator for floats, complex and integers.

**escape**str, optional

Use ‘html’ to replace the characters `&`, `<`, `>`, `'`, and `"` in cell display string with HTML-safe sequences. Use ‘latex’ to replace the characters `&`, `%`, `$`, `#`, `_`, `{`, `}`, `~`, `^`, and `\` in the cell display string with LaTeX-safe sequences. Use ‘latex-math’ to replace the characters the same way as in ‘latex’ mode, except for math substrings, which either are surrounded by two characters `$` or start with the character `\(` and end with `\)`. Escaping is done before `formatter`.

**hyperlinks**{“html”, “latex”}, optional

Convert string patterns containing [https://](https://)
, [http://](http://)
, [ftp://](ftp://)
 or www. to HTML <a> tags as clickable URL hyperlinks if “html”, or LaTeX href commands if “latex”.

Returns:

Styler

Returns itself for chaining.

See also

[`Styler.format_index`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.format_index.html#pandas.io.formats.style.Styler.format_index "pandas.io.formats.style.Styler.format_index")

Format the text display value of index labels.

Notes

This method assigns a formatting function, `formatter`, to each cell in the DataFrame. If `formatter` is `None`, then the default formatter is used. If a callable then that function should take a data value as input and return a displayable representation, such as a string. If `formatter` is given as a string this is assumed to be a valid Python format specification and is wrapped to a callable as `string.format(x)`. If a `dict` is given, keys should correspond to column names, and values should be string or callable, as above.

The default formatter currently expresses floats and complex numbers with the pandas display precision unless using the `precision` argument here. The default formatter does not adjust the representation of missing values unless the `na_rep` argument is used.

The `subset` argument defines which region to apply the formatting function to. If the `formatter` argument is given in dict form but does not include all columns within the subset then these columns will have the default formatter applied. Any columns in the formatter dict excluded from the subset will be ignored.

When using a `formatter` string the dtypes must be compatible, otherwise a ValueError will be raised.

When instantiating a Styler, default formatting can be applied by setting the `pandas.options`:

> *   `styler.format.formatter`: default None.
>     
> *   `styler.format.na_rep`: default None.
>     
> *   `styler.format.precision`: default 6.
>     
> *   `styler.format.decimal`: default “.”.
>     
> *   `styler.format.thousands`: default None.
>     
> *   `styler.format.escape`: default None.
>     

Warning

Styler.format is ignored when using the output format Styler.to\_excel, since Excel and Python have inherently different formatting structures. However, it is possible to use the number-format pseudo CSS attribute to force Excel permissible formatting. See examples.

Examples

Using `na_rep` and `precision` with the default `formatter`

\>>> df \= pd.DataFrame(\[\[np.nan, 1.0, 'A'\], \[2.0, np.nan, 3.0\]\])
\>>> df.style.format(na\_rep\='MISS', precision\=3)
        0       1       2
0    MISS   1.000       A
1   2.000    MISS   3.000

Copy to clipboard

Using a `formatter` specification on consistent column dtypes

\>>> df.style.format('{:.2f}', na\_rep\='MISS', subset\=\[0, 1\])
        0      1          2
0    MISS   1.00          A
1    2.00   MISS   3.000000

Copy to clipboard

Using the default `formatter` for unspecified columns

\>>> df.style.format({0: '{:.2f}', 1: '£ {:.1f}'},
...                 na\_rep\='MISS', precision\=1)
         0      1     2
0    MISS   £ 1.0     A
1    2.00    MISS   3.0

Copy to clipboard

Multiple `na_rep` or `precision` specifications under the default `formatter`.

\>>> (df.style.format(na\_rep\='MISS', precision\=1, subset\=\[0\]).format(
...     na\_rep\='PASS', precision\=2, subset\=\[1, 2\]))
        0      1      2
0    MISS   1.00      A
1     2.0   PASS   3.00

Copy to clipboard

Using a callable `formatter` function.

\>>> func \= lambda s: 'STRING' if isinstance(s, str) else 'FLOAT'
\>>> df.style.format({0: '{:.1f}', 2: func},
...                 precision\=4, na\_rep\='MISS')
        0        1        2
0    MISS   1.0000   STRING
1     2.0     MISS    FLOAT

Copy to clipboard

Using a `formatter` with HTML `escape` and `na_rep`.

\>>> df \= pd.DataFrame(\[\['<div></div>', '"A&B"', None\]\])
\>>> s \= df.style.format(
...     '<a href="a.com/{0}">{0}</a>', escape\="html", na\_rep\="NA")
\>>> s.to\_html()
...
<td .. ><a href="a.com/&lt;div&gt;&lt;/div&gt;">&lt;div&gt;&lt;/div&gt;</a></td>
<td .. ><a href="a.com/&#34;A&amp;B&#34;">&#34;A&amp;B&#34;</a></td>
<td .. >NA</td>
...

Copy to clipboard

Using a `formatter` with `escape` in ‘latex’ mode.

\>>> df \= pd.DataFrame(\[\["123"\], \["~ ^"\], \["$%#"\]\])
\>>> df.style.format("\\\\textbf{{{}}}",
...                 escape\="latex").to\_latex()
\\begin{tabular}{ll}
 & 0 \\\\
0 & \\textbf{123} \\\\
1 & \\textbf{\\textasciitilde \\space \\textasciicircum } \\\\
2 & \\textbf{\\$\\%\\#} \\\\
\\end{tabular}

Copy to clipboard

Applying `escape` in ‘latex-math’ mode. In the example below we enter math mode using the character `$`.

\>>> df \= pd.DataFrame(\[\
...     \[r"$\\sum\_{i=1}^{10} a\_i$ a~b $\\alpha = \\frac{\\beta}{\\zeta^2}$"\],\
...     \[r"%#^ $ \\$x^2 $"\]\])
\>>> df.style.format(escape\="latex-math").to\_latex()
\\begin{tabular}{ll}
 & 0 \\\\
0 & $\\sum\_{i=1}^{10} a\_i$ a\\textasciitilde b $\\alpha = \\frac{\\beta}{\\zeta^2}$ \\\\
1 & \\%\\#\\textasciicircum \\space $ \\$x^2 $ \\\\
\\end{tabular}

Copy to clipboard

We can use the character `\(` to enter math mode and the character `\)` to close math mode.

\>>> df \= pd.DataFrame(\[\
...     \[r"\\(\\sum\_{i=1}^{10} a\_i\\) a~b \\(\\alpha = \\frac{\\beta}{\\zeta^2}\\)"\],\
...     \[r"%#^ \\( \\$x^2 \\)"\]\])
\>>> df.style.format(escape\="latex-math").to\_latex()
\\begin{tabular}{ll}
 & 0 \\\\
0 & \\(\\sum\_{i=1}^{10} a\_i\\) a\\textasciitilde b \\(\\alpha
\= \\frac{\\beta}{\\zeta^2}\\) \\\\
1 & \\%\\#\\textasciicircum \\space \\( \\$x^2 \\) \\\\
\\end{tabular}

Copy to clipboard

If we have in one DataFrame cell a combination of both shorthands for math formulas, the shorthand with the sign `$` will be applied.

\>>> df \= pd.DataFrame(\[\
...     \[r"\\( x^2 \\)  $x^2$"\],\
...     \[r"$\\frac{\\beta}{\\zeta}$ \\(\\frac{\\beta}{\\zeta}\\)"\]\])
\>>> df.style.format(escape\="latex-math").to\_latex()
\\begin{tabular}{ll}
 & 0 \\\\
0 & \\textbackslash ( x\\textasciicircum 2 \\textbackslash )  $x^2$ \\\\
1 & $\\frac{\\beta}{\\zeta}$ \\textbackslash (\\textbackslash
frac\\{\\textbackslash beta\\}\\{\\textbackslash zeta\\}\\textbackslash ) \\\\
\\end{tabular}

Copy to clipboard

Pandas defines a number-format pseudo CSS attribute instead of the .format method to create to\_excel permissible formatting. Note that semi-colons are CSS protected characters but used as separators in Excel’s format string. Replace semi-colons with the section separator character (ASCII-245) when defining the formatting here.

\>>> df \= pd.DataFrame({"A": \[1, 0, \-1\]})
\>>> pseudo\_css \= "number-format: 0§\[Red\](0)§-§@;"
\>>> filename \= "formatted\_file.xlsx"
\>>> df.style.map(lambda v: pseudo\_css).to\_excel(filename)

Copy to clipboard

![../../_images/format_excel_css.png](https://pandas.pydata.org/docs/_images/format_excel_css.png)

On this page