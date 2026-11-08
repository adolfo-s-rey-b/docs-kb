[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.normalize.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.str.normalize[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.normalize.html#pandas-series-str-normalize "Link to this heading")

=================================================================================================================================================================

Series.str.normalize(_form_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/strings/accessor.py#L3722-L3760)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.normalize.html#pandas.Series.str.normalize "Link to this definition")

Return the Unicode normal form for the strings in the Series/Index.

For more information on the forms, see the [`unicodedata.normalize()`](https://docs.python.org/3/library/unicodedata.html#unicodedata.normalize "(in Python v3.15)")
.

Parameters:

**form**{‘NFC’, ‘NFKC’, ‘NFD’, ‘NFKD’}

Unicode form.

Returns:

Series/Index of objects

A Series or Index of strings in the same Unicode form specified by form. The returned object retains the same type as the input (Series or Index), and contains the normalized strings.

See also

[`Series.str.upper`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.upper.html#pandas.Series.str.upper "pandas.Series.str.upper")

Convert all characters in each string to uppercase.

[`Series.str.lower`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.lower.html#pandas.Series.str.lower "pandas.Series.str.lower")

Convert all characters in each string to lowercase.

[`Series.str.title`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.title.html#pandas.Series.str.title "pandas.Series.str.title")

Convert each string to title case (capitalizing the first letter of each word).

[`Series.str.strip`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.strip.html#pandas.Series.str.strip "pandas.Series.str.strip")

Remove leading and trailing whitespace from each string.

[`Series.str.replace`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.replace.html#pandas.Series.str.replace "pandas.Series.str.replace")

Replace occurrences of a substring with another substring in each string.

Examples

\>>> ser \= pd.Series(\["ñ"\])
\>>> ser.str.normalize("NFC") \== ser.str.normalize("NFD")
0   False
dtype: bool

Copy to clipboard

On this page