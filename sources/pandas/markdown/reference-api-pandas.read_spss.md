[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.read_spss.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.read_spss.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.read_spss.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.read_spss.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.read_spss.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.read_spss.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.read_spss.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.read_spss.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.read_spss.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.read_spss.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.read_spss.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.read_spss.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.read_spss.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.read_spss.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.read\_spss[#](https://pandas.pydata.org/docs/reference/api/pandas.read_spss.html#pandas-read-spss "Link to this heading")

=================================================================================================================================

pandas.read\_spss(_path_, _usecols\=None_, _convert\_categoricals\=True_, _dtype\_backend\=<no\_default>_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/spss.py#L26-L98)
[#](https://pandas.pydata.org/docs/reference/api/pandas.read_spss.html#pandas.read_spss "Link to this definition")

Load an SPSS file from the file path, returning a DataFrame.

This function reads data saved in the SPSS `.sav` format using the `pyreadstat` library, which must be installed separately.

Parameters:

**path**str or Path

File path.

**usecols**list-like, optional

Return a subset of the columns. If None, return all columns.

**convert\_categoricals**bool, default is True

Convert categorical columns into pd.Categorical.

**dtype\_backend**{‘numpy\_nullable’, ‘pyarrow’}

Back-end data type applied to the resultant [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 (still experimental). If not specified, the default behavior is to not use nullable data types. If specified, the behavior is as follows:

*   `"numpy_nullable"`: returns nullable-dtype-backed [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
    
*   `"pyarrow"`: returns pyarrow-backed nullable [`ArrowDtype`](https://pandas.pydata.org/docs/reference/api/pandas.ArrowDtype.html#pandas.ArrowDtype "pandas.ArrowDtype")
     [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
    

Added in version 2.0.

**\*\*kwargs**

Additional keyword arguments that can be passed to `pyreadstat.read_sav()`.

Added in version 3.0.

Returns:

DataFrame

DataFrame based on the SPSS file.

See also

[`read_csv`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv "pandas.read_csv")

Read a comma-separated values (csv) file into a pandas DataFrame.

[`read_excel`](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html#pandas.read_excel "pandas.read_excel")

Read an Excel file into a pandas DataFrame.

[`read_sas`](https://pandas.pydata.org/docs/reference/api/pandas.read_sas.html#pandas.read_sas "pandas.read_sas")

Read an SAS file into a pandas DataFrame.

[`read_orc`](https://pandas.pydata.org/docs/reference/api/pandas.read_orc.html#pandas.read_orc "pandas.read_orc")

Load an ORC object into a pandas DataFrame.

[`read_feather`](https://pandas.pydata.org/docs/reference/api/pandas.read_feather.html#pandas.read_feather "pandas.read_feather")

Load a feather-format object into a pandas DataFrame.

Examples

\>>> df \= pd.read\_spss("spss\_data.sav")

Copy to clipboard

On this page