[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.format_index_names.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.formats.style.Styler.format\_index\_names[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.format_index_names.html#pandas-io-formats-style-styler-format-index-names "Link to this heading")

=====================================================================================================================================================================================================================================

Styler.format\_index\_names(_formatter\=None_, _axis\=0_, _level\=None_, _na\_rep\=None_, _precision\=None_, _decimal\='.'_, _thousands\=None_, _escape\=None_, _hyperlinks\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/formats/style_render.py#L1635-L1767)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.format_index_names.html#pandas.io.formats.style.Styler.format_index_names "Link to this definition")

Format the text display value of index names or column names.

Added in version 3.0.

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

Raises:

ValueError

If the formatter is a string and the dtypes are incompatible.

See also

[`Styler.format_index`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.format_index.html#pandas.io.formats.style.Styler.format_index "pandas.io.formats.style.Styler.format_index")

Format the text display value of index labels or column headers.

Notes

This method has a similar signature to [`Styler.format_index()`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.format_index.html#pandas.io.formats.style.Styler.format_index "pandas.io.formats.style.Styler.format_index")
. Since names are generally label based, and often not numeric, the typical features expected to be more frequently used here are `escape` and `hyperlinks`.

Warning

Styler.format\_index\_names is ignored when using the output format Styler.to\_excel, since Excel and Python have inherently different formatting structures.

Examples

\>>> df \= pd.DataFrame(
...     \[\[1, 2\], \[3, 4\]\],
...     index\=pd.Index(\["a", "b"\], name\="idx"),
... )
\>>> df
     0  1
idx
a    1  2
b    3  4
\>>> df.style.format\_index\_names(lambda x: x.upper(), axis\=0)
     0  1
IDX
a    1  2
b    3  4

Copy to clipboard

On this page