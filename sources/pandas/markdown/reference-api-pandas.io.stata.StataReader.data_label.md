[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.stata.StataReader.data_label.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.io.stata.StataReader.data_label.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.io.stata.StataReader.data_label.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.io.stata.StataReader.data_label.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.io.stata.StataReader.data_label.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.io.stata.StataReader.data_label.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.io.stata.StataReader.data_label.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.io.stata.StataReader.data_label.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.io.stata.StataReader.data_label.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.io.stata.StataReader.data_label.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.io.stata.StataReader.data_label.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.io.stata.StataReader.data_label.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.io.stata.StataReader.data_label.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.io.stata.StataReader.data_label.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.stata.StataReader.data\_label[#](https://pandas.pydata.org/docs/reference/api/pandas.io.stata.StataReader.data_label.html#pandas-io-stata-statareader-data-label "Link to this heading")

===================================================================================================================================================================================================

property StataReader.data\_label[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/stata.py#L2022-L2054)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.stata.StataReader.data_label.html#pandas.io.stata.StataReader.data_label "Link to this definition")

Return data label of Stata file.

The data label is a descriptive string associated with the dataset stored in the Stata file. This property provides access to that label, if one is present.

See also

`io.stata.StataReader.variable_labels`

Return a dict associating each variable name with corresponding label.

`DataFrame.to_stata`

Export DataFrame object to Stata dta format.

Examples

\>>> df \= pd.DataFrame(\[(1,)\], columns\=\["variable"\])
\>>> time\_stamp \= pd.Timestamp(2000, 2, 29, 14, 21)
\>>> data\_label \= "This is a data file."
\>>> path \= "/My\_path/filename.dta"
\>>> df.to\_stata(
...     path,
...     time\_stamp\=time\_stamp,
...     data\_label\=data\_label,
...     version\=None,
... )
\>>> with pd.io.stata.StataReader(path) as reader:
...     print(reader.data\_label)
This is a data file.

Copy to clipboard

On this page