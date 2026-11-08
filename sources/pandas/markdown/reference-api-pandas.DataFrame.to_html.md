[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_html.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.to\_html[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_html.html#pandas-dataframe-to-html "Link to this heading")

=========================================================================================================================================================

DataFrame.to\_html(_buf\=None_, _\*_, _columns\=None_, _col\_space\=None_, _header\=True_, _index\=True_, _na\_rep\='NaN'_, _formatters\=None_, _float\_format\=None_, _sparsify\=None_, _index\_names\=True_, _justify\=None_, _max\_rows\=None_, _max\_cols\=None_, _show\_dimensions\=False_, _decimal\='.'_, _bold\_rows\=True_, _classes\=None_, _escape\=True_, _notebook\=False_, _border\=None_, _table\_id\=None_, _render\_links\=False_, _encoding\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L3205-L3426)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_html.html#pandas.DataFrame.to_html "Link to this definition")

Render a DataFrame as an HTML table.

Converts the DataFrame into an HTML `<table>` element. The resulting HTML can be written to a file or returned as a string. This is useful for embedding tabular data in web pages or HTML-based reports.

Parameters:

**buf**str, Path or StringIO-like, optional, default None

Buffer to write to. If None, the output is returned as a string.

**columns**array-like, optional, default None

The subset of columns to write. Writes all columns by default.

**col\_space**str or int, list or dict of int or str, optional

The minimum width of each column in CSS length units. An int is assumed to be px units.

**header**bool, optional

Whether to print column labels, default True.

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

**bold\_rows**bool, default True

Make the row labels bold in the output.

**classes**str or list or tuple, default None

CSS class(es) to apply to the resulting html table.

**escape**bool, default True

Convert the characters <, >, and & to HTML-safe sequences.

**notebook**{True, False}, default False

Whether the generated HTML is for IPython Notebook.

**border**int or bool

When an integer value is provided, it sets the border attribute in the opening tag, specifying the thickness of the border. If `False` or `0` is passed, the border attribute will not be present in the `<table>` tag. The default value for this parameter is governed by `pd.options.display.html.border`.

**table\_id**str, optional

A css id is included in the opening <table> tag if specified.

**render\_links**bool, default False

Convert URLs to HTML links.

**encoding**str, default “utf-8”

Set character encoding.

Returns:

str or None

If buf is None, returns the result as a string. Otherwise returns None.

See also

[`to_string`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_string.html#pandas.DataFrame.to_string "pandas.DataFrame.to_string")

Convert DataFrame to a string.

Examples

\>>> df \= pd.DataFrame(data\={"col1": \[1, 2\], "col2": \[4, 3\]})
\>>> html\_string \= df.to\_html()
\>>> print(html\_string)
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col1</th>
      <th>col2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>3</td>
    </tr>
  </tbody>
</table>

Copy to clipboard

HTML output

|     | col1 | col2 |
| --- | --- | --- |
| 0   | 1   | 4   |
| 1   | 2   | 3   |

\>>> df \= pd.DataFrame(data\={"col1": \[1, 2\], "col2": \[4, 3\]})
\>>> html\_string \= df.to\_html(index\=False)
\>>> print(html\_string)
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>col1</th>
      <th>col2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <td>2</td>
      <td>3</td>
    </tr>
  </tbody>
</table>

Copy to clipboard

HTML output

| col1 | col2 |
| --- | --- |
| 1   | 4   |
| 2   | 3   |

On this page