[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.translate.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.str.translate.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.translate.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.str.translate.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.str.translate.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.str.translate.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.str.translate.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.str.translate.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.str.translate.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.str.translate.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.str.translate.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.str.translate.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.str.translate.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.str.translate.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.str.translate[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.translate.html#pandas-series-str-translate "Link to this heading")

=================================================================================================================================================================

Series.str.translate(_table_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/strings/accessor.py#L3077-L3119)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.translate.html#pandas.Series.str.translate "Link to this definition")

Map all characters in the string through the given mapping table.

This method is equivalent to the standard [`str.translate()`](https://docs.python.org/3/builtins/stdtypes.html#str.translate "(in Python v3.15)")
 method for strings. It maps each character in the string to a new character according to the translation table provided. Unmapped characters are left unchanged, while characters mapped to None are removed.

Parameters:

**table**dict

Table is a mapping of Unicode ordinals to Unicode ordinals, strings, or None. Unmapped characters are left untouched. Characters mapped to None are deleted. [`str.maketrans()`](https://docs.python.org/3/builtins/stdtypes.html#str.maketrans "(in Python v3.15)")
 is a helper function for making translation tables.

Returns:

Series or Index

A new Series or Index with translated strings.

See also

[`Series.str.replace`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.replace.html#pandas.Series.str.replace "pandas.Series.str.replace")

Replace occurrences of pattern/regex in the Series with some other string.

`Index.str.replace`

Replace occurrences of pattern/regex in the Index with some other string.

Examples

\>>> ser \= pd.Series(\["El niño", "Françoise"\])
\>>> mytable \= str.maketrans({"ñ": "n", "ç": "c"})
\>>> ser.str.translate(mytable)
0   El nino
1   Francoise
dtype: str

Copy to clipboard

On this page