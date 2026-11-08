[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.isnumeric.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.str.isnumeric.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.isnumeric.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.str.isnumeric.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.str.isnumeric.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.str.isnumeric.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.str.isnumeric.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.str.isnumeric.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.str.isnumeric.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.str.isnumeric.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.str.isnumeric.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.str.isnumeric.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.str.isnumeric.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.str.isnumeric.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.str.isnumeric[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.isnumeric.html#pandas-series-str-isnumeric "Link to this heading")

=================================================================================================================================================================

Series.str.isnumeric()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/strings/accessor.py#L4709-L4768)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.isnumeric.html#pandas.Series.str.isnumeric "Link to this definition")

Check whether all characters in each string are numeric.

This is equivalent to running the Python string method [`str.isnumeric()`](https://docs.python.org/3/builtins/stdtypes.html#str.isnumeric "(in Python v3.15)")
 for each element of the Series/Index. If a string has zero characters, `False` is returned for that check.

Returns:

Series or Index of bool

Series or Index of boolean values with the same length as the original Series/Index.

See also

[`Series.str.isalpha`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.isalpha.html#pandas.Series.str.isalpha "pandas.Series.str.isalpha")

Check whether all characters are alphabetic.

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

[`Series.str.istitle`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.istitle.html#pandas.Series.str.istitle "pandas.Series.str.istitle")

Check whether all characters are titlecase.

Examples

The `s.str.isnumeric` method is the same as `s3.str.isdigit` but also includes other characters that can represent quantities such as unicode fractions.

\>>> s1 \= pd.Series(\["one", "one1", "1", "", "³", "⅕"\])
\>>> s1.str.isnumeric()
0    False
1    False
2     True
3    False
4     True
5     True
dtype: bool

Copy to clipboard

For a string to be considered numeric, all its characters must have a Unicode numeric property matching `str.is_numeric()`. As a consequence, the following cases are **not** recognized as numeric:

*   **Decimal numbers** (e.g., “1.1”): due to period `"."`
    
*   **Negative numbers** (e.g., “-5”): due to minus sign `"-"`
    
*   **Scientific notation** (e.g., “1e3”): due to characters like `"e"`
    

\>>> s2 \= pd.Series(\["1.1", "-5", "1e3"\])
\>>> s2.str.isnumeric()
0    False
1    False
2    False
dtype: bool

Copy to clipboard

On this page