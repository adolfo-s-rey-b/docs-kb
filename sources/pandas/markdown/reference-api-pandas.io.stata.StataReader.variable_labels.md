[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.stata.StataReader.variable_labels.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.io.stata.StataReader.variable_labels.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.io.stata.StataReader.variable_labels.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.io.stata.StataReader.variable_labels.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.io.stata.StataReader.variable_labels.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.io.stata.StataReader.variable_labels.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.io.stata.StataReader.variable_labels.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.io.stata.StataReader.variable_labels.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.io.stata.StataReader.variable_labels.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.io.stata.StataReader.variable_labels.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.io.stata.StataReader.variable_labels.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.io.stata.StataReader.variable_labels.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.io.stata.StataReader.variable_labels.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.io.stata.StataReader.variable_labels.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.stata.StataReader.variable\_labels[#](https://pandas.pydata.org/docs/reference/api/pandas.io.stata.StataReader.variable_labels.html#pandas-io-stata-statareader-variable-labels "Link to this heading")

==================================================================================================================================================================================================================

StataReader.variable\_labels()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/stata.py#L2064-L2103)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.stata.StataReader.variable_labels.html#pandas.io.stata.StataReader.variable_labels "Link to this definition")

Return a dict associating each variable name with corresponding label.

This method retrieves variable labels from a Stata file. Variable labels are mappings between variable names and their corresponding descriptive labels in a Stata dataset.

Returns:

dict

A python dictionary.

See also

`read_stata`

Read Stata file into DataFrame.

`DataFrame.to_stata`

Export DataFrame object to Stata dta format.

Examples

\>>> df \= pd.DataFrame(\[\[1, 2\], \[3, 4\]\], columns\=\["col\_1", "col\_2"\])
\>>> time\_stamp \= pd.Timestamp(2000, 2, 29, 14, 21)
\>>> path \= "/My\_path/filename.dta"
\>>> variable\_labels \= {"col\_1": "This is an example"}
\>>> df.to\_stata(
...     path,
...     time\_stamp\=time\_stamp,
...     variable\_labels\=variable\_labels,
...     version\=None,
... )
\>>> with pd.io.stata.StataReader(path) as reader:
...     print(reader.variable\_labels())
{'index': '', 'col\_1': 'This is an example', 'col\_2': ''}
\>>> pd.read\_stata(path)
    index col\_1 col\_2
0       0    1    2
1       1    3    4

Copy to clipboard

On this page