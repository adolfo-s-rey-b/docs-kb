[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_xml.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.to_xml.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_xml.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.to_xml.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.to_xml.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.to_xml.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.to_xml.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.to_xml.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.to_xml.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.to_xml.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.to_xml.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.to_xml.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.to_xml.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.to_xml.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.to\_xml[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_xml.html#pandas-dataframe-to-xml "Link to this heading")

======================================================================================================================================================

DataFrame.to\_xml(_path\_or\_buffer\=None_, _\*_, _index\=True_, _root\_name\='data'_, _row\_name\='row'_, _na\_rep\=None_, _attr\_cols\=None_, _elem\_cols\=None_, _namespaces\=None_, _prefix\=None_, _encoding\='utf-8'_, _xml\_declaration\=True_, _pretty\_print\=True_, _parser\='lxml'_, _stylesheet\=None_, _compression\='infer'_, _storage\_options\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L3472-L3697)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_xml.html#pandas.DataFrame.to_xml "Link to this definition")

Render a DataFrame to an XML document.

Produces an XML representation of the DataFrame where each row becomes an XML element. Column values can be mapped to either XML element text or attributes, and the output supports namespaces, XSLT stylesheets, and custom root/row element names.

Parameters:

**path\_or\_buffer**str, path object, file-like object, or None, default None

String, path object (implementing `os.PathLike[str]`), or file-like object implementing a `write()` function. If None, the result is returned as a string.

**index**bool, default True

Whether to include index in XML document.

**root\_name**str, default ‘data’

The name of root element in XML document.

**row\_name**str, default ‘row’

The name of row element in XML document.

**na\_rep**str, optional

Missing data representation.

**attr\_cols**list-like, optional

List of columns to write as attributes in row element. Hierarchical columns will be flattened with underscore delimiting the different levels.

**elem\_cols**list-like, optional

List of columns to write as children in row element. By default, all columns output as children of row element. Hierarchical columns will be flattened with underscore delimiting the different levels.

**namespaces**dict, optional

All namespaces to be defined in root element. Keys of dict should be prefix names and values of dict corresponding URIs. Default namespaces should be given empty string key. For example,

namespaces \= {"": "https://example.com"}

Copy to clipboard

**prefix**str, optional

Namespace prefix to be used for every element and/or attribute in document. This should be one of the keys in `namespaces` dict.

**encoding**str, default ‘utf-8’

Encoding of the resulting document.

**xml\_declaration**bool, default True

Whether to include the XML declaration at start of document.

**pretty\_print**bool, default True

Whether output should be pretty printed with indentation and line breaks.

**parser**{‘lxml’,’etree’}, default ‘lxml’

Parser module to use for building of tree. Only ‘lxml’ and ‘etree’ are supported. With ‘lxml’, the ability to use XSLT stylesheet is supported.

**stylesheet**str, path object or file-like object, optional

A URL, file-like object, or a raw string containing an XSLT script used to transform the raw XML output. Script should use layout of elements and attributes from original output. This argument requires `lxml` to be installed. Only XSLT 1.0 scripts and not later versions is currently supported.

**compression**str or dict, default ‘infer’

For on-the-fly compression of the output data. If ‘infer’ and ‘path\_or\_buffer’ is path-like, then detect compression from the following extensions: ‘.gz’, ‘.bz2’, ‘.zip’, ‘.xz’, ‘.zst’, ‘.tar’, ‘.tar.gz’, ‘.tar.xz’ or ‘.tar.bz2’ (otherwise no compression). Set to `None` for no compression. Can also be a dict with key `'method'` set to one of {`'zip'`, `'gzip'`, `'bz2'`, `'zstd'`, `'xz'`, `'tar'`} and other key-value pairs are forwarded to `zipfile.ZipFile`, `gzip.GzipFile`, `bz2.BZ2File`, `zstandard.ZstdCompressor`, `lzma.LZMAFile` or `tarfile.TarFile`, respectively. As an example, the following could be passed for faster compression and to create a reproducible gzip archive: `compression={'method': 'gzip', 'compresslevel': 1, 'mtime': 1}`.

**storage\_options**dict, optional

Extra options that make sense for a particular storage connection, e.g. host, port, username, password, etc. For HTTP(S) URLs the key-value pairs are forwarded to `urllib.request.Request` as header options. For other URLs (e.g. starting with “s3://”, and “gcs://”) the key-value pairs are forwarded to `fsspec.open`. Please see `fsspec` and `urllib` for more details, and for more examples on storage options refer [here](https://pandas.pydata.org/docs/user_guide/io.html?highlight=storage_options#reading-writing-remote-files)
.

Returns:

None or str

If `io` is None, returns the resulting XML format as a string. Otherwise returns None.

See also

[`to_json`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_json.html#pandas.DataFrame.to_json "pandas.DataFrame.to_json")

Convert the pandas object to a JSON string.

[`to_html`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_html.html#pandas.DataFrame.to_html "pandas.DataFrame.to_html")

Convert DataFrame to a html.

Examples

\>>> df \= pd.DataFrame(
...     \[\["square", 360, 4\], \["circle", 360, np.nan\], \["triangle", 180, 3\]\],
...     columns\=\["shape", "degrees", "sides"\],
... )

Copy to clipboard

\>>> df.to\_xml()
<?xml version='1.0' encoding='utf-8'?>
<data>
  <row>
    <index>0</index>
    <shape>square</shape>
    <degrees>360</degrees>
    <sides>4.0</sides>
  </row>
  <row>
    <index>1</index>
    <shape>circle</shape>
    <degrees>360</degrees>
    <sides/>
  </row>
  <row>
    <index>2</index>
    <shape>triangle</shape>
    <degrees>180</degrees>
    <sides>3.0</sides>
  </row>
</data>

Copy to clipboard

\>>> df.to\_xml(
...     attr\_cols\=\["index", "shape", "degrees", "sides"\]
... )
<?xml version='1.0' encoding='utf-8'?>
<data>
  <row index="0" shape="square" degrees="360" sides="4.0"/>
  <row index="1" shape="circle" degrees="360"/>
  <row index="2" shape="triangle" degrees="180" sides="3.0"/>
</data>

Copy to clipboard

\>>> df.to\_xml(
...     namespaces\={"doc": "https://example.com"}, prefix\="doc"
... )
<?xml version='1.0' encoding='utf-8'?>
<doc:data xmlns:doc="https://example.com">
  <doc:row>
    <doc:index>0</doc:index>
    <doc:shape>square</doc:shape>
    <doc:degrees>360</doc:degrees>
    <doc:sides>4.0</doc:sides>
  </doc:row>
  <doc:row>
    <doc:index>1</doc:index>
    <doc:shape>circle</doc:shape>
    <doc:degrees>360</doc:degrees>
    <doc:sides/>
  </doc:row>
  <doc:row>
    <doc:index>2</doc:index>
    <doc:shape>triangle</doc:shape>
    <doc:degrees>180</doc:degrees>
    <doc:sides>3.0</doc:sides>
  </doc:row>
</doc:data>

Copy to clipboard

On this page