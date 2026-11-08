[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.read_html.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.read_html.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.read_html.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.read_html.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.read_html.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.read_html.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.read_html.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.read_html.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.read_html.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.read_html.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.read_html.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.read_html.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.read_html.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.read_html.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.read\_html[#](https://pandas.pydata.org/docs/reference/api/pandas.read_html.html#pandas-read-html "Link to this heading")

=================================================================================================================================

pandas.read\_html(_io_, _\*_, _match\='.+'_, _flavor\=None_, _header\=None_, _index\_col\=None_, _skiprows\=None_, _attrs\=None_, _parse\_dates\=False_, _thousands\='_, _'_, _encoding\=None_, _decimal\='.'_, _converters\=None_, _na\_values\=None_, _keep\_default\_na\=True_, _displayed\_only\=True_, _extract\_links\=None_, _dtype\_backend\=<no\_default>_, _storage\_options\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/html.py#L1021-L1253)
[#](https://pandas.pydata.org/docs/reference/api/pandas.read_html.html#pandas.read_html "Link to this definition")

Read HTML tables into a `list` of `DataFrame` objects.

This function requires one of the following libraries: [lxml](https://lxml.de/)
, [html5lib](https://github.com/html5lib/html5lib-python)
, or [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/)
.

This function searches for `<table>` elements within an HTML document and parses their rows and columns into DataFrames. It can read from a URL, a file path, or a raw HTML string, and supports filtering tables by matching text content via a regular expression.

Parameters:

**io**str, path object, or file-like object

String path, path object (implementing `os.PathLike[str]`), or file-like object implementing a string `read()` function. The string can represent a URL. Note that lxml only accepts the http, ftp and file url protocols. If you have a URL that starts with `'https'` you might try removing the `'s'`.

**match**str or compiled regular expression, optional

The set of tables containing text matching this regex or string will be returned. Unless the HTML is extremely simple you will probably need to pass a non-empty string here. Defaults to ‘.+’ (match any non-empty string). The default value will return all tables contained on a page. This value is converted to a regular expression so that there is consistent behavior between Beautiful Soup and lxml.

**flavor**{“lxml”, “html5lib”, “bs4”} or list-like, optional

The parsing engine (or list of parsing engines) to use. ‘bs4’ and ‘html5lib’ are synonymous with each other, they are both there for backwards compatibility. The default of `None` tries to use `lxml` to parse and if that fails it falls back on `bs4` + `html5lib`.

**header**int or list-like, optional

The row (or list of rows for a [`MultiIndex`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.html#pandas.MultiIndex "pandas.MultiIndex")
) to use to make the columns headers.

**index\_col**int or list-like, optional

The column (or list of columns) to use to create the index.

**skiprows**int, list-like or slice, optional

Number of rows to skip after parsing the header. 0-based. If a sequence of integers or a slice is given, will skip the rows indexed by that sequence. Note that a single element sequence means ‘skip the nth row’ whereas an integer means ‘skip n rows’.

**attrs**dict, optional

This is a dictionary of attributes that you can pass to use to identify the table in the HTML. These are not checked for validity before being passed to lxml or Beautiful Soup. However, these attributes must be valid HTML table attributes to work correctly. For example,

attrs \= {"id": "table"}

Copy to clipboard

is a valid attribute dictionary because the ‘id’ HTML tag attribute is a valid HTML attribute for _any_ HTML tag as per [this document](https://html.spec.whatwg.org/multipage/dom.html#global-attributes)
.

attrs \= {"asdf": "table"}

Copy to clipboard

is _not_ a valid attribute dictionary because ‘asdf’ is not a valid HTML attribute even if it is a valid XML attribute. Valid HTML 4.01 table attributes can be found [here](http://www.w3.org/TR/REC-html40/struct/tables.html#h-11.2)
. A working draft of the HTML 5 spec can be found [here](https://html.spec.whatwg.org/multipage/tables.html)
. It contains the latest information on table attributes for the modern web.

**parse\_dates**bool, optional

See [`read_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv "pandas.read_csv")
 for more details.

**thousands**str, optional

Separator to use to parse thousands. Defaults to `','`.

**encoding**str, optional

The encoding used to decode the web page. Defaults to `None`.\`\`None\`\` preserves the previous encoding behavior, which depends on the underlying parser library (e.g., the parser library will try to use the encoding provided by the document).

**decimal**str, default ‘.’

Character to recognize as decimal point (e.g. use ‘,’ for European data).

**converters**dict, default None

Dict of functions for converting values in certain columns. Keys can either be integers or column labels, values are functions that take one input argument, the cell (not column) content, and return the transformed content.

**na\_values**iterable, default None

Custom NA values.

**keep\_default\_na**bool, default True

If na\_values are specified and keep\_default\_na is False the default NaN values are overridden, otherwise they’re appended to.

**displayed\_only**bool, default True

Whether elements with “display: none” should be parsed.

**extract\_links**{None, “all”, “header”, “body”, “footer”}

Table elements in the specified section(s) with <a> tags will have their href extracted.

**dtype\_backend**{‘numpy\_nullable’, ‘pyarrow’}

Back-end data type applied to the resultant [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 (still experimental). If not specified, the default behavior is to not use nullable data types. If specified, the behavior is as follows:

*   `"numpy_nullable"`: returns nullable-dtype-backed [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
    
*   `"pyarrow"`: returns pyarrow-backed nullable [`ArrowDtype`](https://pandas.pydata.org/docs/reference/api/pandas.ArrowDtype.html#pandas.ArrowDtype "pandas.ArrowDtype")
     [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
    

Added in version 2.0.

**storage\_options**dict, optional

Extra options that make sense for a particular storage connection, e.g. host, port, username, password, etc. For HTTP(S) URLs the key-value pairs are forwarded to `urllib.request.Request` as header options. For other URLs (e.g. starting with “s3://”, and “gcs://”) the key-value pairs are forwarded to `fsspec.open`. Please see `fsspec` and `urllib` for more details, and for more examples on storage options refer [here](https://pandas.pydata.org/docs/user_guide/io.html?highlight=storage_options#reading-writing-remote-files)
.

Added in version 2.1.0.

Returns:

dfs

A list of DataFrames.

See also

[`read_csv`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv "pandas.read_csv")

Read a comma-separated values (csv) file into DataFrame.

Notes

Before using this function you should read the [gotchas about the HTML parsing libraries](https://pandas.pydata.org/docs/user_guide/io.html#io-html-gotchas)
.

Expect to do some cleanup after you call this function. For example, you might need to manually assign column names if the column names are converted to NaN when you pass the header=0 argument. We try to assume as little as possible about the structure of the table and push the idiosyncrasies of the HTML contained in the table to the user.

This function searches for `<table>` elements and only for `<tr>` and `<th>` rows and `<td>` elements within each `<tr>` or `<th>` element in the table. `<td>` stands for “table data”. This function attempts to properly handle `colspan` and `rowspan` attributes. If the function has a `<thead>` argument, it is used to construct the header, otherwise the function attempts to find the header within the body (by putting rows with only `<th>` elements into the header).

Similar to [`read_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv "pandas.read_csv")
 the header argument is applied **after** skiprows is applied.

This function will _always_ return a list of [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 _or_ it will fail, i.e., it will _not_ return an empty list, save for some rare cases. It might return an empty list in case of inputs with single row and `<td>` containing only whitespaces.

Examples

See the [read\_html documentation in the IO section of the docs](https://pandas.pydata.org/docs/user_guide/io.html#io-read-html)
 for some examples of reading in HTML tables.

On this page