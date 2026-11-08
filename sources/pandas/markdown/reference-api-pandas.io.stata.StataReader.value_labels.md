[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.stata.StataReader.value_labels.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.io.stata.StataReader.value_labels.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.io.stata.StataReader.value_labels.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.io.stata.StataReader.value_labels.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.io.stata.StataReader.value_labels.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.io.stata.StataReader.value_labels.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.io.stata.StataReader.value_labels.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.io.stata.StataReader.value_labels.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.io.stata.StataReader.value_labels.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.io.stata.StataReader.value_labels.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.io.stata.StataReader.value_labels.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.io.stata.StataReader.value_labels.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.io.stata.StataReader.value_labels.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.io.stata.StataReader.value_labels.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.stata.StataReader.value\_labels[#](https://pandas.pydata.org/docs/reference/api/pandas.io.stata.StataReader.value_labels.html#pandas-io-stata-statareader-value-labels "Link to this heading")

=========================================================================================================================================================================================================

StataReader.value\_labels()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/stata.py#L2105-L2147)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.stata.StataReader.value_labels.html#pandas.io.stata.StataReader.value_labels "Link to this definition")

Return a nested dict mapping each value label name to its values and labels.

This method retrieves the value labels from a Stata file. Value labels are mappings between the coded values and their corresponding descriptive labels in a Stata dataset.

Returns:

dict

A python dictionary keyed by value label name, which need not match a variable name. Several variables can share one value label set.

See also

`read_stata`

Read Stata file into DataFrame.

`DataFrame.to_stata`

Export DataFrame object to Stata dta format.

Examples

\>>> df \= pd.DataFrame(\[\[1, 2\], \[3, 4\]\], columns\=\["col\_1", "col\_2"\])
\>>> time\_stamp \= pd.Timestamp(2000, 2, 29, 14, 21)
\>>> path \= "/My\_path/filename.dta"
\>>> value\_labels \= {"col\_1": {3: "x"}}
\>>> df.to\_stata(
...     path,
...     time\_stamp\=time\_stamp,
...     value\_labels\=value\_labels,
...     version\=None,
... )
\>>> with pd.io.stata.StataReader(path) as reader:
...     print(reader.value\_labels())
{'col\_1': {3: 'x'}}
\>>> pd.read\_stata(path)
    index col\_1 col\_2
0       0    1    2
1       1    x    4

Copy to clipboard

On this page