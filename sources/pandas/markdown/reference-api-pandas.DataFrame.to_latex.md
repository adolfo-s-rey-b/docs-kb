[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_latex.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.to_latex.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_latex.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.to_latex.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.to_latex.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.to_latex.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.to_latex.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.to_latex.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.to_latex.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.to_latex.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.to_latex.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.to_latex.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.to_latex.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.to_latex.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.to\_latex[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_latex.html#pandas-dataframe-to-latex "Link to this heading")

============================================================================================================================================================

DataFrame.to\_latex(_buf\=None_, _\*_, _columns\=None_, _header\=True_, _index\=True_, _na\_rep\='NaN'_, _formatters\=None_, _float\_format\=None_, _sparsify\=None_, _index\_names\=True_, _bold\_rows\=False_, _column\_format\=None_, _longtable\=None_, _escape\=None_, _encoding\=None_, _decimal\='.'_, _multicolumn\=None_, _multicolumn\_format\=None_, _multirow\=None_, _caption\=None_, _label\=None_, _position\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L3409-L3697)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_latex.html#pandas.DataFrame.to_latex "Link to this definition")

Render object to a LaTeX tabular, longtable, or nested table.

Requires `\usepackage{booktabs}`. The output can be copy/pasted into a main LaTeX document or read from an external file with `\input{table.tex}`.

Changed in version 2.0.0: Refactored to use the Styler implementation via jinja2 templating.

Parameters:

**buf**str, Path or StringIO-like, optional, default None

Buffer to write to. If None, the output is returned as a string.

**columns**list of label, optional

The subset of columns to write. Writes all columns by default.

**header**bool or list of str, default True

Write out the column names. If a list of strings is given, it is assumed to be aliases for the column names. Braces must be escaped.

**index**bool, default True

Write row names (index).

**na\_rep**str, default ‘NaN’

Missing data representation.

**formatters**list of functions or dict of {str: function}, optional

Formatter functions to apply to columns’ elements by position or name. The result of each function must be a unicode string. List must be of length equal to the number of columns.

**float\_format**one-parameter function or str, optional, default None

Formatter for floating point numbers. For example `float_format="%.2f"` and `float_format="{:0.2f}".format` will both result in 0.1234 being formatted as 0.12.

**sparsify**bool, optional

Set to False for a DataFrame with a hierarchical index to print every multiindex key at each row. By default, the value will be read from the config module.

**index\_names**bool, default True

Prints the names of the indexes.

**bold\_rows**bool, default False

Make the row labels bold in the output.

**column\_format**str, optional

The columns format as specified in [LaTeX table format](https://en.wikibooks.org/wiki/LaTeX/Tables)
 e.g. ‘rcl’ for 3 columns. By default, ‘l’ will be used for all columns except columns of numbers, which default to ‘r’.

**longtable**bool, optional

Use a longtable environment instead of tabular. Requires adding a usepackage{longtable} to your LaTeX preamble. By default, the value will be read from the pandas config module, and set to True if the option `styler.latex.environment` is “longtable”.

Changed in version 2.0.0: The pandas option affecting this argument has changed.

**escape**bool, optional

By default, the value will be read from the pandas config module and set to True if the option `styler.format.escape` is “latex”. When set to False prevents from escaping latex special characters in column names.

Changed in version 2.0.0: The pandas option affecting this argument has changed, as has the default value to False.

**encoding**str, optional

A string representing the encoding to use in the output file, defaults to ‘utf-8’.

**decimal**str, default ‘.’

Character recognized as decimal separator, e.g. ‘,’ in Europe.

**multicolumn**bool, default True

Use multicolumn to enhance MultiIndex columns. The default will be read from the config module, and is set as the option `styler.sparse.columns`.

Changed in version 2.0.0: The pandas option affecting this argument has changed.

**multicolumn\_format**str, default ‘r’

The alignment for multicolumns, similar to column\_format The default will be read from the config module, and is set as the option `styler.latex.multicol_align`.

Changed in version 2.0.0: The pandas option affecting this argument has changed, as has the default value to “r”.

**multirow**bool, default True

Use multirow to enhance MultiIndex rows. Requires adding a usepackage{multirow} to your LaTeX preamble. Will print centered labels (instead of top-aligned) across the contained rows, separating groups via clines. The default will be read from the pandas config module, and is set as the option `styler.sparse.index`.

Changed in version 2.0.0: The pandas option affecting this argument has changed, as has the default value to True.

**caption**str or tuple, optional

Tuple (full\_caption, short\_caption), which results in `\caption[short_caption]{full_caption}`; if a single string is passed, no short caption will be set.

**label**str, optional

The LaTeX label to be placed inside `\label{}` in the output. This is used with `\ref{}` in the main `.tex` file.

**position**str, optional

The LaTeX positional argument for tables, to be placed after `\begin{}` in the output.

Returns:

str or None

If buf is None, returns the result as a string. Otherwise returns None.

See also

[`io.formats.style.Styler.to_latex`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.to_latex.html#pandas.io.formats.style.Styler.to_latex "pandas.io.formats.style.Styler.to_latex")

Render a DataFrame to LaTeX with conditional formatting.

[`DataFrame.to_string`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_string.html#pandas.DataFrame.to_string "pandas.DataFrame.to_string")

Render a DataFrame to a console-friendly tabular output.

[`DataFrame.to_html`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_html.html#pandas.DataFrame.to_html "pandas.DataFrame.to_html")

Render a DataFrame as an HTML table.

Notes

As of v2.0.0 this method has changed to use the Styler implementation as part of [`Styler.to_latex()`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.to_latex.html#pandas.io.formats.style.Styler.to_latex "pandas.io.formats.style.Styler.to_latex")
 via `jinja2` templating. This means that `jinja2` is a requirement, and needs to be installed, for this method to function. It is advised that users switch to using Styler, since that implementation is more frequently updated and contains much more flexibility with the output.

Examples

Convert a general DataFrame to LaTeX with formatting:

\>>> df \= pd.DataFrame(dict(name\=\['Raphael', 'Donatello'\],
...                        age\=\[26, 45\],
...                        height\=\[181.23, 177.65\]))
\>>> print(df.to\_latex(index\=False,
...                   formatters\={"name": str.upper},
...                   float\_format\="{:.1f}".format,
...                   ))
\\begin{tabular}{lrr}
\\toprule
name & age & height \\\\
\\midrule
RAPHAEL & 26 & 181.2 \\\\
DONATELLO & 45 & 177.7 \\\\
\\bottomrule
\\end{tabular}

Copy to clipboard

On this page