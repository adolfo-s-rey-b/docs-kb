[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.isascii.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.str.isascii.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.isascii.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.str.isascii.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.str.isascii.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.str.isascii.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.str.isascii.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.str.isascii.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.str.isascii.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.str.isascii.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.str.isascii.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.str.isascii.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.str.isascii.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.str.isascii.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.str.isascii[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.isascii.html#pandas-series-str-isascii "Link to this heading")

===========================================================================================================================================================

Series.str.isascii()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/strings/accessor.py#L4579-L4621)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.isascii.html#pandas.Series.str.isascii "Link to this definition")

Check whether all characters in each string are ascii.

This is equivalent to running the Python string method [`str.isascii()`](https://docs.python.org/3/builtins/stdtypes.html#str.isascii "(in Python v3.15)")
 for each element of the Series/Index. If a string has zero characters, `False` is returned for that check.

Returns:

Series or Index of bool

Series or Index of boolean values with the same length as the original Series/Index.

See also

[`Series.str.isalpha`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.isalpha.html#pandas.Series.str.isalpha "pandas.Series.str.isalpha")

Check whether all characters are alphabetic.

[`Series.str.isnumeric`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.isnumeric.html#pandas.Series.str.isnumeric "pandas.Series.str.isnumeric")

Check whether all characters are numeric.

[`Series.str.isalnum`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.isalnum.html#pandas.Series.str.isalnum "pandas.Series.str.isalnum")

Check whether all characters are alphanumeric.

[`Series.str.isdigit`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.isdigit.html#pandas.Series.str.isdigit "pandas.Series.str.isdigit")

Check whether all characters are digits.

[`Series.str.isdecimal`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.isdecimal.html#pandas.Series.str.isdecimal "pandas.Series.str.isdecimal")

Check whether all characters are decimal.

[`Series.str.isspace`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.isspace.html#pandas.Series.str.isspace "pandas.Series.str.isspace")

Check whether all characters are whitespace.

[`Series.str.islower`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.islower.html#pandas.Series.str.islower "pandas.Series.str.islower")

Check whether all characters are lowercase.

[`Series.str.isupper`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.isupper.html#pandas.Series.str.isupper "pandas.Series.str.isupper")

Check whether all characters are uppercase.

[`Series.str.istitle`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.istitle.html#pandas.Series.str.istitle "pandas.Series.str.istitle")

Check whether all characters are titlecase.

Examples

The `s5.str.isascii` method checks for whether all characters are ascii characters, which includes digits 0-9, capital and lowercase letters A-Z, and some other special characters.

\>>> s5 \= pd.Series(\["ö", "see123", "hello world", ""\])
\>>> s5.str.isascii()
0    False
1     True
2     True
3     True
dtype: bool

Copy to clipboard

On this page