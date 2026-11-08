[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_string.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.to\_string[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_string.html#pandas-dataframe-to-string "Link to this heading")

===============================================================================================================================================================

DataFrame.to\_string(_buf\=None_, _\*_, _columns\=None_, _col\_space\=None_, _header\=True_, _index\=True_, _na\_rep\='NaN'_, _formatters\=None_, _float\_format\=None_, _sparsify\=None_, _index\_names\=True_, _justify\=None_, _max\_rows\=None_, _max\_cols\=None_, _show\_dimensions\=False_, _decimal\='.'_, _line\_width\=None_, _min\_rows\=None_, _max\_colwidth\=None_, _encoding\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L1072-L1212)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_string.html#pandas.DataFrame.to_string "Link to this definition")

Render a DataFrame to a console-friendly tabular output.

This method converts the DataFrame to a string representation suitable for printing or writing to a file.

Parameters:

**buf**str, Path or StringIO-like, optional, default None

Buffer to write to. If None, the output is returned as a string.

**columns**array-like, optional, default None

The subset of columns to write. Writes all columns by default.

**col\_space**int, list or dict of int, optional

The minimum width of each column. If a list of ints is given every integers corresponds with one column. If a dict is given, the key references the column, while the value defines the space to use.

**header**bool or list of str, optional

Write out the column names. If a list of columns is given, it is assumed to be aliases for the column names.

**index**bool, optional, default True

Whether to print index (row) labels.

**na\_rep**str, optional, default ‘NaN’

String representation of `NaN` to use.

**formatters**list, tuple or dict of one-param. functions, optional

Formatter functions to apply to columns’ elements by position or name. The result of each function must be a unicode string. List/tuple must be of length equal to the number of columns.

**float\_format**one-parameter function, optional, default None

Formatter function to apply to columns’ elements if they are floats. This function must return a unicode string and will be applied only to the non-`NaN` elements, with `NaN` being handled by `na_rep`.

**sparsify**bool, optional, default True

Set to False for a DataFrame with a hierarchical index to print every multiindex key at each row.

**index\_names**bool, optional, default True

Prints the names of the indexes.

**justify**str, default None

How to justify the column labels. If None uses the option from the print configuration (controlled by set\_option), ‘right’ out of the box. Valid values are

*   left
    
*   right
    
*   center
    
*   justify
    
*   justify-all
    
*   start
    
*   end
    
*   inherit
    
*   match-parent
    
*   initial
    
*   unset.
    

**max\_rows**int, optional

Maximum number of rows to display in the console.

**max\_cols**int, optional

Maximum number of columns to display in the console.

**show\_dimensions**bool, default False

Display DataFrame dimensions (number of rows by number of columns).

**decimal**str, default ‘.’

Character recognized as decimal separator, e.g. ‘,’ in Europe.

**line\_width**int, optional

Width to wrap a line in characters.

**min\_rows**int, optional

The number of rows to display in the console in a truncated repr (when number of rows is above max\_rows).

**max\_colwidth**int, optional

Max width to truncate each column in characters. By default, no limit.

**encoding**str, default “utf-8”

Set character encoding.

Returns:

str or None

If buf is None, returns the result as a string. Otherwise returns None.

See also

[`to_html`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_html.html#pandas.DataFrame.to_html "pandas.DataFrame.to_html")

Convert DataFrame to HTML.

Examples

\>>> d \= {"col1": \[1, 2, 3\], "col2": \[4, 5, 6\]}
\>>> df \= pd.DataFrame(d)
\>>> print(df.to\_string())
   col1  col2
0     1     4
1     2     5
2     3     6

Copy to clipboard

On this page