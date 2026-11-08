[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.stata.StataWriter.write_file.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.io.stata.StataWriter.write_file.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.io.stata.StataWriter.write_file.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.io.stata.StataWriter.write_file.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.io.stata.StataWriter.write_file.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.io.stata.StataWriter.write_file.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.io.stata.StataWriter.write_file.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.io.stata.StataWriter.write_file.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.io.stata.StataWriter.write_file.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.io.stata.StataWriter.write_file.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.io.stata.StataWriter.write_file.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.io.stata.StataWriter.write_file.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.io.stata.StataWriter.write_file.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.io.stata.StataWriter.write_file.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.stata.StataWriter.write\_file[#](https://pandas.pydata.org/docs/reference/api/pandas.io.stata.StataWriter.write_file.html#pandas-io-stata-statawriter-write-file "Link to this heading")

===================================================================================================================================================================================================

StataWriter.write\_file()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/stata.py#L2906-L2997)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.stata.StataWriter.write_file.html#pandas.io.stata.StataWriter.write_file "Link to this definition")

Export DataFrame object to Stata dta format.

This method writes the contents of a pandas DataFrame to a .dta file compatible with Stata. It includes features for handling value labels, variable types, and metadata like timestamps and data labels. The output file can then be read and used in Stata or other compatible statistical tools.

See also

`read_stata`

Read Stata file into DataFrame.

`DataFrame.to_stata`

Export DataFrame object to Stata dta format.

`io.stata.StataWriter`

A class for writing Stata binary dta files.

Examples

\>>> df \= pd.DataFrame(
...     {
...         "fully\_labelled": \[1, 2, 3, 3, 1\],
...         "partially\_labelled": \[1.0, 2.0, np.nan, 9.0, np.nan\],
...         "Y": \[7, 7, 9, 8, 10\],
...         "Z": pd.Categorical(\["j", "k", "l", "k", "j"\]),
...     }
... )
\>>> path \= "/My\_path/filename.dta"
\>>> labels \= {
...     "fully\_labelled": {1: "one", 2: "two", 3: "three"},
...     "partially\_labelled": {1.0: "one", 2.0: "two"},
... }
\>>> writer \= pd.io.stata.StataWriter(
...     path, df, value\_labels\=labels
... )
\>>> writer.write\_file()
\>>> df \= pd.read\_stata(path)
\>>> df
    index fully\_labelled  partially\_labeled  Y  Z
0       0            one                one  7  j
1       1            two                two  7  k
2       2          three                NaN  9  l
3       3          three                9.0  8  k
4       4            one                NaN 10  j

Copy to clipboard

On this page