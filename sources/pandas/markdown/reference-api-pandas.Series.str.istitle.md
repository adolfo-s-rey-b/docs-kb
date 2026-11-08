[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.istitle.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.str.istitle.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.istitle.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.str.istitle.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.str.istitle.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.str.istitle.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.str.istitle.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.str.istitle.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.str.istitle.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.str.istitle.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.str.istitle.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.str.istitle.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.str.istitle.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.str.istitle.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.str.istitle[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.istitle.html#pandas-series-str-istitle "Link to this heading")

===========================================================================================================================================================

Series.str.istitle()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/strings/accessor.py#L4664-L4707)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.istitle.html#pandas.Series.str.istitle "Link to this definition")

Check whether all characters in each string are titlecase.

This is equivalent to running the Python string method [`str.istitle()`](https://docs.python.org/3/builtins/stdtypes.html#str.istitle "(in Python v3.15)")
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

[`Series.str.isascii`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.isascii.html#pandas.Series.str.isascii "pandas.Series.str.isascii")

Check whether all characters are ascii.

[`Series.str.isupper`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.isupper.html#pandas.Series.str.isupper "pandas.Series.str.isupper")

Check whether all characters are uppercase.

Examples

The `s5.str.istitle` method checks for whether all words are in title case (whether only the first letter of each word is capitalized). Words are assumed to be as any sequence of non-numeric characters separated by whitespace characters.

\>>> s5 \= pd.Series(\["leopard", "Golden Eagle", "SNAKE", ""\])
\>>> s5.str.istitle()
0    False
1     True
2    False
3    False
dtype: bool

Copy to clipboard

On this page